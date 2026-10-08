#!/usr/bin/env python3
"""Independent ticket-only browser replay. All artifact writes exclusively create files."""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.metadata
import json
import socket
import subprocess
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
TICKETS = ROOT / "validation/baseline/source/tickets-reviewed.json"
BASE = "http://127.0.0.1:39175"
STAMP = "20261008-a1"
SOURCE = ROOT / "validation/replay/source"
WORK = ROOT / (".work/replay-ticket-run-" + STAMP)
PORT = 39180

SNAPSHOT = r"""() => {
  const visible = e => { const r=e.getBoundingClientRect(), s=getComputedStyle(e);
    return r.width>0 && r.height>0 && s.display!=='none' && s.visibility!=='hidden'; };
  const record = e => { const r=e.getBoundingClientRect(), s=getComputedStyle(e);
    return {id:e.id, tag:e.tagName, text:e.textContent.trim(), value:('value' in e)?e.value:null,
      href:e.getAttribute('href'), tabIndex:e.tabIndex,
      ariaInvalid:e.getAttribute('aria-invalid'), hidden:e.hidden, visible:visible(e),
      role:e.getAttribute('role'), rect:{x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom},
      outline:{style:s.outlineStyle,width:s.outlineWidth,color:s.outlineColor,offset:s.outlineOffset},
      overflowX:s.overflowX, whiteSpace:s.whiteSpace, width:s.width, minWidth:s.minWidth};
  };
  return {url:location.href, language:document.documentElement.lang,
    title:document.title, heading:document.querySelector('#page-heading')?.textContent.trim()||null,
    readyState:document.readyState, viewport:{width:innerWidth,height:innerHeight},
    scrollWidth:document.documentElement.scrollWidth, scrollX, scrollY,
    navigatorLanguage:navigator.language, timezone:Intl.DateTimeFormat().resolvedOptions().timeZone,
    activeElement:record(document.activeElement), bodyText:document.body.innerText,
    elements:[...document.querySelectorAll('[id]')].map(record),
    paragraphs:[...document.querySelectorAll('main p, main h1, main h2, article, main section')].map(record),
    confirmationCandidates:[...document.querySelectorAll('[role="status"], [id*="confirm"], [id*="success"]')].map(record)};
}"""

def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")

def create_bytes(path, content):
    with path.open("xb") as handle:
        handle.write(content)

def create_json(path, value):
    create_bytes(path, encode(value))

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def aggregate(steps):
    states = {step["status"] for step in steps}
    for state in ("FAIL", "BLOCKED", "NOT_RUN", "PASS"):
        if state in states:
            return state
    return "NOT_APPLICABLE"

def element(state, ident):
    return next((item for item in state["elements"] if item["id"] == ident), {})

def path_of(state):
    return urlsplit(state["url"]).path

class Recorder:
    def __init__(self, source, browser_version):
        self.source = source
        self.browser_version = browser_version
        self.evidence = []

    def save(self, ident, kind, value, page, profile, description, binary=False):
        captured_at = now()
        if binary:
            content = value
            extension = ".png"
        else:
            content = encode({"captured_at":captured_at, "actual_url":page.url,
                "actual_language":page.locator("html").get_attribute("lang"),
                "profile":profile, "browser_version":self.browser_version,
                "playwright_version":importlib.metadata.version("playwright"),
                "description":description, "data":value})
            extension = ".json"
        relative = "evidence/" + ident + extension
        create_bytes(self.source / relative, content)
        item = {"id":ident, "path":relative, "sha256":hashlib.sha256(content).hexdigest(),
            "kind":kind, "captured_at":captured_at,
            "description":description + " | URL " + page.url + " | language " +
                str(page.locator("html").get_attribute("lang")) + " | profile " +
                profile["id"] + " " + str(profile["viewport"]["width"]) + "x" +
                str(profile["viewport"]["height"]) + " | Chromium " +
                self.browser_version + " | captured " + captured_at}
        self.evidence.append(item)
        return ident

    def state(self, ident, page, profile, description):
        state = page.evaluate(SNAPSHOT)
        self.save(ident, "DOM", state, page, profile, description)
        return state, ident

    def screenshot(self, ident, page, profile, description):
        image = page.screenshot(full_page=False, timeout=20000)
        return self.save(ident, "SCREENSHOT", image, page, profile, description, binary=True)

def replay_ticket(ticket, browser, recorder):
    ident = "REPLAY-" + ticket["id"]
    mobile = "mobile" in ticket["scope"]["profiles"]
    viewport = {"width":390, "height":844} if mobile else {"width":1440, "height":900}
    profile = {"id":"mobile" if mobile else "desktop",
        "device_class":"MOBILE_EMULATION" if mobile else "DESKTOP",
        "viewport":viewport, "browser":{"name":"Chromium","version":recorder.browser_version},
        "locale":"en-GB", "timezone":"UTC", "physical_device":False}
    started = now()
    context = browser.new_context(viewport=viewport, locale="en-GB", timezone_id="UTC",
        device_scale_factor=1, is_mobile=False, has_touch=False, service_workers="block")
    denied = []
    def route_request(route):
        if urlsplit(route.request.url).scheme in ("data", "about"):
            route.continue_()
        elif route.request.url.startswith(BASE + "/"):
            route.continue_()
        else:
            denied.append({"url":route.request.url,"reason":"Outside authorized loopback baseline"})
            route.abort()
    context.route("**/*", route_request)
    page = context.new_page()
    page.set_default_timeout(10000)
    documents, console = [], []
    def record_response(response):
        if response.request.is_navigation_request() and response.request.frame == page.main_frame:
            documents.append({"captured_at":now(), "url":response.url,
                "status":response.status, "location":response.headers.get("location"),
                "redirected_from":response.request.redirected_from.url if response.request.redirected_from else None})
    page.on("response", record_response)
    page.on("console", lambda msg: console.append({"captured_at":now(),"type":msg.type,"text":msg.text}))
    page.on("pageerror", lambda error: console.append({"captured_at":now(),"type":"pageerror","text":str(error)}))
    refs, steps, limitations, uncertainties, facts = [], [], [], [], []
    source_url = ticket["scope"]["pages"][0]
    initial, current = None, None
    def state(suffix, description):
        nonlocal current
        current, ref = recorder.state(ident + "-a1-" + suffix, page, profile, description)
        refs.append(ref)
        return current, ref
    def shot(suffix, description):
        ref = recorder.screenshot(ident + "-a1-" + suffix, page, profile, description)
        refs.append(ref)
        return ref
    def step(action, expected, observed, passed=None, evidence=(), status=None):
        steps.append({"number":len(steps)+1,"action":action,"expected":expected,
            "observed":observed,"status":status or ("PASS" if passed else "FAIL"),
            "evidence_ids":list(evidence)})
    def open_page():
        response = page.goto(source_url, wait_until="domcontentloaded", timeout=15000)
        initial_state, ref = state("opened", "Initial document after the ticket's opening navigation.")
        return initial_state, ref, response.status if response else None
    try:
        initial, opened_ref, status = open_page()
        if ticket["id"] == "QA-003":
            step(ticket["steps"][0], "The supplied French legacy URL initiates navigation.",
                "Requested " + source_url + "; final document HTTP " + str(status) + ".",
                bool(documents), [opened_ref])
        else:
            lang = "en" if "/en/" in source_url else "fr"
            step(ticket["steps"][0], "The specified page loads in the requested language and viewport.",
                "HTTP " + str(status) + "; actual URL " + initial["url"] + "; html[lang]=" +
                initial["language"] + "; viewport " + str(initial["viewport"]) + ".",
                status == 200 and initial["url"] == source_url and initial["language"] == lang and initial["viewport"] == viewport,
                [opened_ref])

        if ticket["id"] in ("QA-001", "QA-002"):
            selector = "#main-about" if ticket["id"] == "QA-001" else "#language-switch"
            link = element(initial, selector[1:])
            page.locator(selector).click()
            page.wait_for_load_state("domcontentloaded")
            destination, dest_ref = state("destination", "Rendered destination after activating " + selector + ".")
            screen_ref = shot("destination-viewport", "Viewport after activating " + selector + ".")
            step(ticket["steps"][1], "The control reaches /fr/about.",
                selector + " href=" + str(link.get("href")) + "; actual destination " + destination["url"] + ".",
                path_of(destination) == "/fr/about", [opened_ref, dest_ref, screen_ref])
            good = destination["language"] == "fr" and destination["heading"] == "À propos d’Atlas Studio"
            if ticket["id"] == "QA-001":
                good = good and bool(documents and documents[-1]["status"] == 200)
            step(ticket["steps"][2], ticket["expected"],
                "Final URL " + destination["url"] + "; HTTP " +
                str(documents[-1]["status"] if documents else None) + "; html[lang]=" +
                destination["language"] + "; heading " + str(destination["heading"]) + ".",
                good and path_of(destination) == "/fr/about", [dest_ref,screen_ref])
            facts.append(steps[-2]["observed"] + " " + steps[-1]["observed"])

        elif ticket["id"] == "QA-003":
            redirect = next((item for item in documents if item["url"] == source_url), {})
            screen_ref = shot("final-viewport", "Final page after the French legacy redirect.")
            step(ticket["steps"][1], "HTTP 302 with Location /fr/about.",
                "Legacy response HTTP " + str(redirect.get("status")) + "; Location " + str(redirect.get("location")) + ".",
                redirect.get("status") == 302 and redirect.get("location") == "/fr/about", [opened_ref])
            step(ticket["steps"][2], "Final /fr/about returns HTTP 200, html[lang]=fr and heading À propos d’Atlas Studio.",
                "Final URL " + initial["url"] + "; HTTP " + str(status) + "; html[lang]=" +
                initial["language"] + "; heading " + str(initial["heading"]) + ".",
                status == 200 and path_of(initial) == "/fr/about" and initial["language"] == "fr" and
                initial["heading"] == "À propos d’Atlas Studio", [opened_ref,screen_ref])
            facts.extend([steps[-2]["observed"],steps[-1]["observed"]])

        elif ticket["id"] == "QA-004":
            name, email = element(initial,"contact-name"), element(initial,"contact-email")
            step(ticket["steps"][1], "Name and email remain empty.",
                "contact-name value=" + repr(name.get("value")) + "; contact-email value=" + repr(email.get("value")) + ".",
                name.get("value") == "" and email.get("value") == "", [opened_ref])
            page.locator("#contact-submit").click()
            result, result_ref = state("validation", "Validation state after one empty submission.")
            screen_ref = shot("validation-viewport", "Visible field errors after one empty submission.")
            name, email = element(result,"contact-name"), element(result,"contact-email")
            confirmations = result["confirmationCandidates"]
            hidden = bool(confirmations) and all(not item["visible"] for item in confirmations)
            step(ticket["steps"][2], "Empty values are rejected, both fields are invalid, and confirmation remains hidden.",
                "contact-name aria-invalid=" + str(name.get("ariaInvalid")) +
                "; contact-email aria-invalid=" + str(email.get("ariaInvalid")) +
                "; confirmation candidates=" + str([{"id":item["id"],"visible":item["visible"]} for item in confirmations]) + ".",
                name.get("ariaInvalid") == "true" and email.get("ariaInvalid") == "true" and hidden, [result_ref])
            name_error, email_error = element(result,"name-error"), element(result,"email-error")
            expected = "Visible messages are Saisissez votre nom. and Saisissez une adresse e-mail valide."
            step(ticket["steps"][3], expected,
                "#name-error=" + repr(name_error.get("text")) + "; visible=" + str(name_error.get("visible")) +
                "; #email-error=" + repr(email_error.get("text")) + "; visible=" + str(email_error.get("visible")) + ".",
                name_error.get("visible") and email_error.get("visible") and
                name_error.get("text") == "Saisissez votre nom." and email_error.get("text") == "Saisissez une adresse e-mail valide.",
                [result_ref,screen_ref])
            if not confirmations:
                uncertainties.append("The ticket does not supply a confirmation selector; no status/confirmation candidate was discoverable.")
            facts.extend([steps[-2]["observed"],steps[-1]["observed"]])

        elif ticket["id"] == "QA-005":
            page.locator("#contact-name").focus()
            page.keyboard.type(ticket["test_data"]["name"])
            typed, typed_ref = state("name-keyboard", "Keyboard name entry before the single Tab press.")
            step(ticket["steps"][1], "#contact-name is focused and contains Alex Test.",
                "Active element " + typed["activeElement"]["id"] + "; name value=" +
                repr(element(typed,"contact-name").get("value")) + ".",
                typed["activeElement"]["id"] == "contact-name" and element(typed,"contact-name").get("value") == "Alex Test",
                [typed_ref])
            page.keyboard.press("Tab")
            focus, focus_ref = state("after-one-tab", "Focus and field state after exactly one Tab.")
            screen_ref = shot("focus-viewport", "Visible focus outline after exactly one Tab from the name field.")
            step(ticket["steps"][2], "Exactly one Tab moves focus to #contact-email.",
                "Active element after one Tab is #" + focus["activeElement"]["id"] + ".",
                focus["activeElement"]["id"] == "contact-email", [focus_ref,screen_ref])
            email = element(focus,"contact-email")
            outline = focus["activeElement"]["outline"]
            step(ticket["steps"][3], "The email field has visible keyboard focus; inspect without clicking or filling the skipped field.",
                "Active element #" + focus["activeElement"]["id"] + "; outline=" + str(outline) +
                "; email value=" + repr(email.get("value")) + "; email tabIndex=" + str(email.get("tabIndex")) + ".",
                focus["activeElement"]["id"] == "contact-email" and outline["style"] != "none" and outline["width"] != "0px",
                [focus_ref,screen_ref])
            if focus["activeElement"]["id"] != "contact-email":
                step("Continue the expected keyboard completion only after the email focus transition succeeds.",
                    "Type alex@example.test, Tab to #contact-submit, press Enter, and observe Thank you, Alex Test. Your local request is confirmed.",
                    "Not run because the first Tab did not reach the email field. No click or direct fill was used to bypass the failed transition.",
                    evidence=[focus_ref], status="NOT_RUN")
                limitations.append("Email entry, submission and confirmation were not executed after the failed required focus transition.")
            else:
                page.keyboard.type(ticket["test_data"]["email"])
                page.keyboard.press("Tab")
                submit, submit_ref = state("submit-focus", "Submit focus after keyboard email entry.")
                step("Type the supplied email and press Tab once.", "Focus reaches #contact-submit with a visible outline.",
                    "Active element #" + submit["activeElement"]["id"] + "; outline=" + str(submit["activeElement"]["outline"]) + ".",
                    submit["activeElement"]["id"] == "contact-submit", [submit_ref])
                if submit["activeElement"]["id"] == "contact-submit":
                    page.keyboard.press("Enter")
                    confirmed, confirmation_ref = state("confirmation", "State after keyboard form submission.")
                    step("Press Enter.", "Thank you, Alex Test. Your local request is confirmed. is visible.",
                        "Visible document text: " + confirmed["bodyText"],
                        "Thank you, Alex Test. Your local request is confirmed." in confirmed["bodyText"], [confirmation_ref])
            facts.extend([s["observed"] for s in steps[2:]])

        elif ticket["id"] == "QA-006":
            screen_ref = shot("offer-viewport", "Offer card and description before any interaction at 390 by 844 CSS pixels.")
            difference = initial["scrollWidth"] - initial["viewport"]["width"]
            step(ticket["steps"][1], "scrollWidth <= innerWidth + 1.",
                "scrollWidth=" + str(initial["scrollWidth"]) + "; innerWidth=" +
                str(initial["viewport"]["width"]) + "; overflow=" + str(difference) + " CSS pixels.",
                difference <= 1, [opened_ref,screen_ref])
            clipped = [item for item in initial["paragraphs"] if item["visible"] and item["rect"]["right"] > viewport["width"] + 1]
            step(ticket["steps"][2], "The offer card and full description fit in the viewport without horizontal scrolling.",
                "Visible content boxes extending beyond the right viewport edge: " +
                str([{"id":item["id"],"text":item["text"],"right":item["rect"]["right"]} for item in clipped]) + ".",
                difference <= 1 and not clipped, [opened_ref,screen_ref])
            cta = element(initial,"offer-cta")
            inside = cta.get("visible") and cta["rect"]["x"] >= 0 and cta["rect"]["right"] <= viewport["width"]
            page.locator("#offer-cta").click()
            page.wait_for_load_state("domcontentloaded")
            contact, contact_ref = state("cta-destination", "French Contact destination after the visible offer CTA was clicked.")
            contact_screen_ref = shot("contact-viewport", "Destination viewport after the offer CTA click.")
            step(ticket["steps"][3], "The CTA remains visible and reaches /fr/contact in French.",
                "CTA initially visible=" + str(cta.get("visible")) + "; within horizontal viewport=" +
                str(inside) + "; final URL " + contact["url"] + "; html[lang]=" + contact["language"] +
                "; heading " + str(contact["heading"]) + ".",
                inside and path_of(contact) == "/fr/contact" and contact["language"] == "fr",
                [opened_ref,contact_ref,contact_screen_ref])
            limitations.append("Mobile profile is a 390 by 844 desktop Chromium viewport, not a physical device; touch/mobile user-agent settings were not specified by the ticket.")
            facts.extend([s["observed"] for s in steps[1:]])
        else:
            raise ValueError("Unexpected ticket ID " + ticket["id"])
    except Exception as error:
        limitation = type(error).__name__ + ": " + str(error)
        limitations.append("Replay tooling incident: " + limitation)
        try:
            _, incident_ref = state("incident", "State retained when a replay tooling exception occurred.")
            incident_refs = [incident_ref]
        except Exception:
            incident_refs = []
        step("Continue the ticket replay.", "All specified actions and observations can be performed.",
             "Tooling incident: " + limitation, evidence=incident_refs, status="BLOCKED")
        facts.append("Tooling incident interrupted this attempt: " + limitation)
    network_ref = recorder.save(ident + "-a1-network", "NETWORK",
        {"main_document_responses":documents, "denied_requests":denied},
        page, profile, "Main-document responses from this replay attempt, including redirect status and Location.")
    refs.append(network_ref)
    console_ref = recorder.save(ident + "-a1-console", "CONSOLE", console,
        page, profile, "Console and page-error observations from this replay attempt.")
    refs.append(console_ref)
    if ticket["id"] == "QA-003":
        for recorded_step in steps:
            if recorded_step["number"] in (2,3):
                recorded_step["evidence_ids"].append(network_ref)
    outcome = aggregate(steps)
    classification = "DEFECT" if outcome == "FAIL" else ("TOOLING_INCIDENT" if outcome == "BLOCKED" else "NONE")
    final_language = page.locator("html").get_attribute("lang")
    if final_language != ticket["scope"]["languages"][0]:
        limitations.append("The case language records the requested starting language; evidence records the actual final document language " + str(final_language) + ".")
    condition = "Fresh isolated browser context; Chromium " + recorder.browser_version + "; locale en-GB; time zone UTC."
    preconditions = [condition, "Viewport " + str(viewport["width"]) + " x " + str(viewport["height"]) + " CSS pixels.",
        "Synthetic local baseline on port 39175; no login.",
        "The sole business input is tickets-reviewed.json; no application source or prior case evidence was read."]
    observed = " ".join(facts) or "No conclusive observation was completed."
    case = {"id":ident, "journey_id":"REPLAY-" + ticket["id"],
        "title":"Independent replay: " + ticket["title"], "critical":ticket["severity"] in ("MAJOR","BLOCKER"),
        "started_at":started, "finished_at":now(), "url":page.url,
        "language":ticket["scope"]["languages"][0], "profile":profile,
        "preconditions":preconditions, "test_data":ticket["test_data"], "steps":steps,
        "status":outcome, "classification":classification,
        "attempts":[{"number":1,"status":outcome,"observed":observed,"evidence_ids":refs}],
        "country":{"requested":None,"verified":None,"status":"NOT_APPLICABLE",
            "same_network_context":False,"evidence_ids":[],"note":"No network-country requirement was specified for this loopback replay."},
        "evidence_ids":refs, "limitations":limitations, "uncertainties":uncertainties}
    create_json(recorder.source / (ident + "-attempt-1.json"), case)
    return case, observed

def create_campaign():
    source_parent = SOURCE.parent
    if source_parent.exists() or WORK.exists():
        raise FileExistsError("Replay and work destinations must both be new; no cleanup is performed.")
    source_parent.mkdir()
    SOURCE.mkdir()
    (SOURCE / "evidence").mkdir()
    WORK.mkdir()
    profile_path = WORK / "chromium-profile"
    profile_path.mkdir()
    cache_path = WORK / "chromium-cache"
    cache_path.mkdir()
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", PORT))
    tickets = read_json(TICKETS)
    started = now()
    from playwright.sync_api import sync_playwright
    with sync_playwright() as playwright:
        command = [playwright.chromium.executable_path, "--headless=new", "--no-sandbox",
            "--disable-dev-shm-usage", "--disable-background-networking", "--disable-component-update",
            "--disable-default-apps", "--no-first-run", "--no-default-browser-check",
            "--disable-sync", "--disable-extensions", "--metrics-recording-only",
            "--safebrowsing-disable-auto-update", "--password-store=basic", "--use-mock-keychain",
            "--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE localhost, EXCLUDE 127.0.0.1",
            "--remote-debugging-address=127.0.0.1", "--remote-debugging-port=" + str(PORT),
            "--user-data-dir=" + str(profile_path), "--disk-cache-dir=" + str(cache_path), "about:blank"]
        log = (WORK / "chromium.log").open("xb")
        process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        create_json(WORK / "browser-launch.json", {"started_at":now(),"pid":process.pid,
            "command":command,"profile":str(profile_path),"cdp_port":PORT,
            "policy":"Profile, cache and all evidence are retained. No deletion or overwrite is performed."})
        browser = None
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            try:
                browser = playwright.chromium.connect_over_cdp("http://127.0.0.1:" + str(PORT), timeout=1000)
                break
            except Exception:
                if process.poll() is not None:
                    raise RuntimeError("Chromium exited; retained log: " + str(WORK / "chromium.log"))
                time.sleep(0.2)
        if browser is None:
            raise RuntimeError("Chromium CDP did not become available; profile and logs retained.")
        recorder = Recorder(SOURCE, browser.version)
        cases, derived_tickets, assessment = [], [], []
        for ticket in tickets:
            case, observed = replay_ticket(ticket, browser, recorder)
            cases.append(case)
            missing = []
            ambiguity = []
            if ticket["id"] == "QA-004":
                missing.append("A confirmation-element selector is not stated; the replay inspected rendered status/confirmation candidates.")
            if ticket["id"] == "QA-006":
                missing.append("Device scale factor, mobile user agent, touch capability and is_mobile setting are not specified.")
                ambiguity.append("The requested dimensions can be reproduced, but 'mobile' does not identify a physical device or complete emulation profile.")
            # Inherited acceptance witnesses and workaround claims are not replay evidence.
            limitations = ["Acceptance-criterion witness journeys outside the numbered reproduction were not executed.",
                "Original reproduction counts and original evidence references were not used as replay proof."]
            status = "reproduced" if case["status"] == "FAIL" else ("not_reproduced" if case["status"] == "PASS" else "ambiguous")
            assessment.append({"ticket_id":ticket["id"],"case_id":case["id"],"assessment":status,
                "reproduced":sum(a["status"] == "FAIL" for a in case["attempts"]),
                "attempted":len(case["attempts"]), "missing_details":missing,
                "ambiguities":ambiguity, "observed_facts":[step["observed"] for step in case["steps"]],
                "limitations":limitations + case["limitations"], "artifact_references":[
                    item["path"] for item in recorder.evidence if item["id"] in case["evidence_ids"]]})
            if case["status"] == "FAIL":
                derived = copy.deepcopy(ticket)
                derived["case_ids"] = [case["id"]]
                derived["evidence_ids"] = case["evidence_ids"]
                derived["reproduction"] = {"reproduced":sum(a["status"] == "FAIL" for a in case["attempts"]),
                    "attempted":len(case["attempts"])}
                derived["preconditions"] = case["preconditions"]
                derived["observed"] = observed
                derived["scope"] = {"pages":list(dict.fromkeys([ticket["scope"]["pages"][0],case["url"]])),
                    "languages":[case["language"]],"profiles":[case["profile"]["id"]]}
                derived["severity_rationale"] = {
                    "QA-001":"The French desktop primary About link reaches the wrong section. This replay does not establish the availability of alternate navigation routes.",
                    "QA-002":"The English About language switch loses the current page identity when reaching French home.",
                    "QA-003":"The French legacy entry redirects to an English document, losing the requested language.",
                    "QA-004":"The empty form is rejected and invalid fields are identified, but the French document shows English correction messages.",
                    "QA-005":"The required email field is skipped in the specified forward keyboard sequence, stopping completion of that sequence.",
                    "QA-006":"The mobile-width presentation overflows and clips content while the visible CTA still reaches French Contact."
                }[ticket["id"]]
                derived["retest_steps"] = ["Repeat the numbered reproduction for " + case["id"] +
                    " against the corrected origin in a new campaign.",
                    "Execute the ticket's separate acceptance witness journeys; they were not part of this replay."]
                derived_tickets.append(derived)
            print(json.dumps({"ticket_id":ticket["id"],"case_id":case["id"],"status":case["status"],
                "assessment":status,"reproduction":str(assessment[-1]["reproduced"])+"/"+str(assessment[-1]["attempted"]),
                "observed":observed}, ensure_ascii=False), flush=True)
        finished = now()
        campaign = {"schema_version":"1.0","campaign":{"id":"independent-ticket-replay-" + STAMP,
            "started_at":started,"finished_at":finished,"base_url":BASE,"environment":"LOCAL",
            "output_language":"en",
            "capabilities":{"extraction":True,"interaction":True,"screenshots":True,"network":True,
                "console":True,"traces":False,"geography":False},
            "limitations":["Ticket-only replay of six specified defects; application source, product oracle and prior case evidence were not read.",
                "One fresh isolated browser context and one attempt per ticket; original reproduction counts were not reused.",
                "Only local port 39175 was visited. Corrected port 39176 and acceptance witness journeys were not tested.",
                "All profiles and evidence are retained. Mobile means the stated viewport, without a physical-device claim.",
                "Raw screenshots require visual reviewer inspection in addition to the DOM measurements."]},
            "cases":cases,"evidence":recorder.evidence,"tickets":[]}
        create_json(SOURCE / "observations.json", campaign)
        create_json(SOURCE / "tickets.json", derived_tickets)
        report = {"schema_version":"1.0","frozen_at":now(),
            "business_input":{"path":str(TICKETS),"sha256":hashlib.sha256(TICKETS.read_bytes()).hexdigest()},
            "browser_version":browser.version,"playwright_version":importlib.metadata.version("playwright"),
            "campaign_id":campaign["campaign"]["id"], "assessments":assessment}
        create_json(SOURCE / "replay-assessment.json", report)
        lines = ["# Independent ticket replay assessment","",
            "Business input: tickets-reviewed.json only. No application source, product oracle or earlier case evidence was inspected.",
            "", "Frozen at: " + report["frozen_at"],"",
            "| Ticket | Case | Assessment | Actual replay frequency |","| --- | --- | --- | ---: |"]
        for item in assessment:
            lines.append("| " + item["ticket_id"] + " | " + item["case_id"] + " | " + item["assessment"] +
                " | " + str(item["reproduced"]) + "/" + str(item["attempted"]) + " |")
        for item in assessment:
            lines += ["","## " + item["ticket_id"],"","Observed facts:"]
            lines += ["- " + fact for fact in item["observed_facts"]]
            lines += ["","Missing details:"] + ["- " + fact for fact in (item["missing_details"] or ["None needed to execute the numbered reproduction."])]
            lines += ["","Ambiguities:"] + ["- " + fact for fact in (item["ambiguities"] or ["No ambiguity prevented the numbered reproduction."])]
            lines += ["","Limits:"] + ["- " + fact for fact in item["limitations"]]
            lines += ["","Artifacts:"] + ["- [" + Path(path).name + "](" + path + ")" for path in item["artifact_references"]]
        create_bytes(SOURCE / "replay-assessment.md", ("\n".join(lines) + "\n").encode("utf-8"))
        receipt = {"finished_at":now(),"command":sys.argv,"source":str(SOURCE),"work":str(WORK),
            "browser_pid":process.pid,"cdp_port":PORT,"browser_version":browser.version,
            "playwright_version":importlib.metadata.version("playwright"),
            "case_count":len(cases),"ticket_count":len(derived_tickets),
            "evidence_file_count":len(recorder.evidence),
            "statuses":{status:sum(case["status"] == status for case in cases) for status in ("PASS","FAIL","BLOCKED","NOT_RUN","NOT_APPLICABLE")},
            "frozen_artifacts":{str(path.relative_to(SOURCE)):hashlib.sha256(path.read_bytes()).hexdigest()
                for path in [SOURCE/"observations.json",SOURCE/"tickets.json",SOURCE/"replay-assessment.json",SOURCE/"replay-assessment.md"]}}
        create_json(WORK / "execution-receipt.json", receipt)
        print(json.dumps(receipt, ensure_ascii=False, indent=2), flush=True)
        # Exiting Playwright disconnects its transport. The manually launched browser,
        # its profile and every context remain retained; no explicit cleanup runs.

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("inspect","create"))
    args = parser.parse_args()
    if args.mode == "inspect":
        print(json.dumps({"business_input":str(TICKETS),"new_source":str(SOURCE),
            "new_work":str(WORK),"target_origin":BASE,"cdp_port":PORT,
            "ticket_ids":[ticket["id"] for ticket in read_json(TICKETS)],
            "source_parent_exists":SOURCE.parent.exists(),"work_exists":WORK.exists(),
            "playwright_version":importlib.metadata.version("playwright")}, indent=2))
        return 0
    create_campaign()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
