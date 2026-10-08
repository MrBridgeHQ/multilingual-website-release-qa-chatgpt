#!/usr/bin/env python3
"""Independent, contract-driven browser audit. Does not read the fixture or oracle."""
import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import time
from datetime import datetime, timezone
from urllib.parse import urlsplit, urlunsplit

from playwright.sync_api import sync_playwright

TITLES = ["Open the requested home page", "Follow primary navigation", "Switch language from an internal page", "Follow a language-preserving redirect", "Search with a matching result", "Search with no matching result", "Submit an invalid local form", "Complete the local form using the keyboard", "Open, use, and close the mobile menu", "Read a localized offer on mobile"]
STEPS = [
    [("Open /{language}/", "HTTP 200 and the requested home URL"), ("Inspect language and heading", "Requested language and approved localized home heading"), ("Inspect canonical and alternate links", "Current-route canonical without query and equivalent en/fr routes")],
    [("Open /{language}/", "HTTP 200 home page"), ("Click #main-about", "Navigation actually occurs"), ("Inspect the destination", "Same-language /about, HTTP 200 and localized About heading")],
    [("Open /{language}/about", "HTTP 200 and localized About page"), ("Click #language-switch", "Navigation actually occurs"), ("Inspect destination route", "Other-language /about route retains internal page"), ("Inspect destination language and heading", "Other-language document and localized About heading")],
    [("Open /{language}/legacy", "Redirect occurs"), ("Inspect the final document", "Same-language /about and localized About heading"), ("Inspect redirect response", "Initial HTTP 302, Location to same-language /about, final HTTP 200")],
    [("Open /{language}/search", "HTTP 200 search page"), ("Type atlas in #search-query and click #search-submit", "Submitted query stays visible"), ("Inspect search results", "Exactly one localized result and no empty state"), ("Click #result-about", "Same-language /about and localized About heading")],
    [("Open /{language}/search", "HTTP 200 search page"), ("Type zzzz-no-match and click #search-submit", "Submitted query stays visible"), ("Inspect the empty state", "Zero results, visible approved localized empty-state text")],
    [("Open /{language}/contact", "HTTP 200 and both fields empty"), ("Click #contact-submit", "Local validation runs"), ("Inspect field validity and confirmation", "Both errors visible, aria-invalid true on both fields, confirmation hidden"), ("Read validation errors", "Both approved error messages use the page language")],
    [("Open /{language}/contact", "HTTP 200 with visible associated labels"), ("Focus #contact-name, type Alex Test and press Tab once", "Actual keyboard input and Tab event"), ("Inspect focus", "#contact-email focused with a visible outline"), ("Type alex@example.test, press Tab once and Enter", "#contact-submit focused before Enter"), ("Inspect confirmation", "Approved localized confirmation visible with no visible validation errors")],
    [("Open /{language}/ at 390 by 844", "Toggle visible, panel hidden, aria-expanded false"), ("Click #menu-toggle", "Panel visible and aria-expanded true"), ("Click #mobile-about", "Same-language /about with localized heading and closed menu"), ("Reopen menu and press Escape", "Panel hidden, aria-expanded false, focus returns to toggle")],
    [("Open /{language}/offer at 390 by 844", "HTTP 200 offer page"), ("Read offer title, price, date and CTA", "Approved localized offer strings"), ("Measure horizontal page overflow", "Document scrollWidth <= window.innerWidth + 1"), ("Click #offer-cta", "CTA visible within viewport, actually clickable, reaches same-language /contact")]
]
COPY = {
    "en": {"home": "Welcome to Atlas Studio", "about": "About Atlas Studio", "empty": "No results found.", "name_error": "Enter your name.", "email_error": "Enter a valid email address.", "confirmation": "Thank you, Alex Test. Your local request is confirmed.", "offer-title": "Starter plan", "offer-price": "€19.90 / month", "offer-date": "October 8, 2026", "offer-cta": "Contact us"},
    "fr": {"home": "Bienvenue chez Atlas Studio", "about": "À propos d’Atlas Studio", "empty": "Aucun résultat.", "name_error": "Saisissez votre nom.", "email_error": "Saisissez une adresse e-mail valide.", "confirmation": "Merci, Alex Test. Votre demande locale est confirmée.", "offer-title": "Offre Découverte", "offer-price": "19,90 € / mois", "offer-date": "8 octobre 2026", "offer-cta": "Contactez-nous"}}
SNAPSHOT = """() => {
 const ids = ['page-heading','main-about','language-switch','menu-toggle','mobile-menu','mobile-about','main-content','search-query','search-submit','search-results','empty-state','result-about','contact-name','contact-email','contact-submit','name-error','email-error','confirmation','offer-title','offer-price','offer-date','offer-cta'];
 const visible = e => {const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none' && s.visibility!=='hidden' && Number(s.opacity)!==0 && r.width>0 && r.height>0;};
 const elements = Object.fromEntries(ids.map(id => {const e=document.getElementById(id); if(!e)return [id,{present:false}]; const r=e.getBoundingClientRect(),s=getComputedStyle(e); return [id,{present:true,text:e.innerText||'',value:('value' in e?e.value:null),visible:visible(e),href:e.getAttribute('href'),aria_invalid:e.getAttribute('aria-invalid'),aria_expanded:e.getAttribute('aria-expanded'),tabindex:e.getAttribute('tabindex'),disabled:!!e.disabled,rect:{x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom},outline:{style:s.outlineStyle,width:s.outlineWidth,color:s.outlineColor},box_shadow:s.boxShadow,labels:e.labels?[...e.labels].map(l=>({text:l.innerText,visible:visible(l),for:l.htmlFor})):[]}];}));
 return {url:location.href,title:document.title,html_lang:document.documentElement.lang,heading:document.getElementById('page-heading')?.innerText||'',canonical:document.querySelector('link[rel="canonical"]')?.href||null,alternates:[...document.querySelectorAll('link[rel="alternate"][hreflang]')].map(e=>({language:e.hreflang,url:e.href})),active_id:document.activeElement?.id||null,active_tag:document.activeElement?.tagName||null,scroll_width:document.documentElement.scrollWidth,inner_width:innerWidth,inner_height:innerHeight,scroll_x:scrollX,scroll_y:scrollY,result_count:document.querySelectorAll('#search-results .search-result').length,body_text:document.body.innerText.slice(0,6000),elements};
}"""

def utc():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")

def write_json(path, value):
    with Path(path).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

def profile(mobile, version=None):
    return {"id": "mobile" if mobile else "desktop", "device_class": "MOBILE_EMULATION" if mobile else "DESKTOP", "viewport": {"width": 390 if mobile else 1440, "height": 844 if mobile else 900}, "browser": {"name": "Chromium", "version": version}, "locale": "en-GB", "timezone": "UTC", "physical_device": False}

def create_config(args):
    base=args.base_url.rstrip("/")
    journeys=[]
    for n,title in enumerate(TITLES, 1):
        journeys.append({"id":f"J{n:02}","title":title,"critical":True,"priority":"P1","preconditions":["Fresh browser context; authorized local synthetic site."],"test_data":{"name":"Alex Test","email":"alex@example.test","matching_query":"atlas","empty_query":"zzzz-no-match"},"steps":[{"number":i,"action":a,"expected":e,"expectation_basis":"SUPPLIED"} for i,(a,e) in enumerate(STEPS[n-1],1)]})
    cfg={"schema_version":"1.0","campaign_id":args.campaign_id,"start_url":base+"/en/","environment":"LOCAL","scope":{"allowed_origins":[base],"allowed_paths":[f"/{language}/{route}" for language in ("en","fr") for route in ("","about","search","contact","offer","legacy")]+["/favicon.ico"],"excluded_origins":[],"excluded_paths":["/auth-required"]},"languages":[{"code":language,"entry_url":base+f"/{language}/","browser_locale":"en-GB"} for language in ("en","fr")],"url_mappings":[{"id":route or "home","urls":{language:base+f"/{language}/{route}" for language in ("en","fr")}} for route in ("","about","search","contact","offer","legacy")],"countries":[],"profiles":[profile(False),profile(True)],"journeys":journeys,"cases":[{"id":f"J{n:02}-{language}","journey_id":f"J{n:02}","language":language,"profile_id":"mobile" if n>=9 else "desktop","country":None} for n in range(1,11) for language in ("en","fr")],"authentication":{"mode":"NONE","reference":None,"authorization_note":"Public contract authorizes loopback fixture navigation and synthetic local form interactions."},"authorized_actions":[{"action":"navigate, click, type, keyboard, local form submit","scope":base+"/en/ and "+base+"/fr/ documented routes","authorization":"Explicit user delegation and public business contract."}],"budgets":{"time_seconds":1200,"max_pages":180,"max_requests":600,"max_retries":1},"output":{"directory":str(Path(args.delivery).resolve()),"formats":["JSON","MARKDOWN","CSV"],"output_language":"en"},"assumptions":["All public-contract journeys are treated as critical for coverage; this is an auditor planning assumption, not a production release gate.","Browser locale remains en-GB for both site languages; timezone UTC, is_mobile false, has_touch false. Mobile means narrow viewport only.","The campaign does not test physical phones, geography, authenticated access, performance or comprehensive accessibility/SEO."]}
    target=Path(args.output).resolve()
    target.parent.mkdir(parents=True,exist_ok=True)
    write_json(target,cfg)
    print(json.dumps({"config":str(target),"planned_cases":len(cfg["cases"])}),flush=True)

class Audit:
    def __init__(self,args):
        self.args=args
        self.config=json.loads(Path(args.config).read_text(encoding="utf-8"))
        self.base=self.config["start_url"].rsplit("/en/",1)[0]
        if self.base not in ("http://127.0.0.1:39175","http://127.0.0.1:39176"):
            raise ValueError("Only the explicitly authorized local fixtures are accepted.")
        self.out=Path(args.output).resolve()
        self.out.mkdir(parents=True,exist_ok=False)
        (self.out/"evidence").mkdir()
        self.session=Path(args.session_dir).resolve()
        self.session.mkdir(parents=True,exist_ok=False)
        self.started=utc(); self.clock=time.monotonic(); self.requests=0; self.navigations=0
        self.evidence=[]; self.cases=[]; self.outside=[]; self.responses=[]; self.console=[]; self.current_steps=[]
        self.browser=None

    def budget(self):
        limits=self.config["budgets"]
        if time.monotonic()-self.clock>limits["time_seconds"] or self.requests>=limits["max_requests"] or self.navigations>=limits["max_pages"]:
            raise RuntimeError("Campaign execution budget reached.")

    def guard(self,route):
        url=route.request.url; parts=urlsplit(url)
        origin=f"{parts.scheme}://{parts.netloc}"
        if origin!=self.base or parts.path not in self.config["scope"]["allowed_paths"]:
            self.outside.append({"at":utc(),"url":url,"decision":"aborted before routing"})
            route.abort(); return
        try:self.budget()
        except RuntimeError:route.abort();return
        route.continue_()

    def request(self,request):
        if request.url.startswith(self.base+"/"):
            self.requests+=1
            if request.is_navigation_request():self.navigations+=1

    def response(self,response):
        self.responses.append({"at":utc(),"url":response.url,"status":response.status,"resource_type":response.request.resource_type,"location":response.headers.get("location"),"redirected_from":response.request.redirected_from.url if response.request.redirected_from else None})

    def save(self,name,kind,payload,description):
        rel="evidence/"+name
        data=payload if isinstance(payload,bytes) else (json.dumps(payload,ensure_ascii=False,indent=2)+"\n").encode()
        with (self.out/rel).open("xb") as f:f.write(data)
        evidence={"id":name.rsplit(".",1)[0],"path":rel,"sha256":hashlib.sha256(data).hexdigest(),"kind":kind,"captured_at":utc(),"description":description}
        self.evidence.append(evidence)
        return evidence["id"]

    def state(self):
        return self.page.evaluate(SNAPSHOT)

    def element(self,state,name):
        return state["elements"][name]

    def exact(self,label,actual,expected):
        return {"check":label,"passed":actual==expected,"expected":expected,"actual":actual}

    def record(self,number,checks=None,details=None,status=None):
        action,expected=STEPS[self.journey-1][number-1]
        action=action.replace("{language}",self.language)
        checks=checks or []
        state=self.state()
        status=status or ("PASS" if all(c["passed"] for c in checks) else "FAIL")
        prefix=f"{self.case_id}-a{self.attempt}-s{number}"
        payload={"at":utc(),"case_id":self.case_id,"attempt":self.attempt,"step":number,"action":action,"expected":expected,"status":status,"checks":checks,"details":details or {},"state":state}
        refs=[self.save(prefix+"-state.json","DOM",payload,f"Rendered state and actual checks after {action}.")]
        refs.append(self.save(prefix+"-viewport.png","SCREENSHOT",self.page.screenshot(full_page=False),f"Actual {self.case_id} attempt {self.attempt} step {number} viewport."))
        observed=json.dumps({"url":state["url"],"checks":checks,"details":details or {},"active_id":state["active_id"]},ensure_ascii=False)
        self.current_steps.append({"number":number,"action":action,"expected":expected,"observed":observed,"status":status,"evidence_ids":refs})
        print(json.dumps({"case":self.case_id,"attempt":self.attempt,"step":number,"status":status,"failed_checks":[c for c in checks if not c["passed"]]},ensure_ascii=False),flush=True)
        return state

    def skip(self,number,reason):
        action,expected=STEPS[self.journey-1][number-1]
        self.current_steps.append({"number":number,"action":action.replace("{language}",self.language),"expected":expected,"observed":reason,"status":"NOT_RUN","evidence_ids":[]})

    def click(self,selector):
        self.page.locator(selector).click()
        self.page.wait_for_load_state("load")

    def goto(self,route):
        self.budget()
        response=self.page.goto(self.base+f"/{self.language}/"+route,wait_until="load")
        return response.status if response else None

    def page_checks(self,language,route,heading=None):
        state=self.state()
        checks=[self.exact("URL",state["url"],self.base+f"/{language}/"+route),self.exact("html language",state["html_lang"],language)]
        if heading is not None:checks.append(self.exact("localized heading",state["heading"],heading))
        documents=[r for r in self.responses if r["resource_type"]=="document"]
        if documents:checks.append(self.exact("last document HTTP status",documents[-1]["status"],200))
        return checks

    def run_steps(self):
        j=self.journey;l=self.language;c=COPY[l];other="fr" if l=="en" else "en"
        if j==1:
            status=self.goto("");self.record(1,[self.exact("HTTP status",status,200),self.exact("home URL",self.page.url,self.base+f"/{l}/")])
            self.record(2,self.page_checks(l,"",c["home"]))
            s=self.state();alternates={x["language"]:x["url"] for x in s["alternates"]}
            self.record(3,[self.exact("canonical",s["canonical"],self.base+f"/{l}/")]+[self.exact("alternate "+lang,alternates.get(lang),self.base+f"/{lang}/") for lang in ("en","fr")])
        elif j==2:
            status=self.goto("");self.record(1,[self.exact("HTTP status",status,200)])
            before=self.page.url;self.click("#main-about");self.record(2,[self.exact("navigation occurred",self.page.url!=before,True)])
            self.record(3,self.page_checks(l,"about",c["about"]))
        elif j==3:
            self.goto("about");self.record(1,self.page_checks(l,"about",c["about"]))
            before=self.page.url;self.click("#language-switch");self.record(2,[self.exact("navigation occurred",self.page.url!=before,True)])
            self.record(3,[self.exact("equivalent other-language route",self.page.url,self.base+f"/{other}/about")])
            self.record(4,self.page_checks(other,"about",COPY[other]["about"]))
        elif j==4:
            self.goto("legacy");redirects=[r for r in self.responses if r["url"]==self.base+f"/{l}/legacy"]
            self.record(1,[self.exact("redirect response captured",bool(redirects),True)],{"redirects":redirects})
            self.record(2,self.page_checks(l,"about",c["about"]))
            first=redirects[0] if redirects else {}
            location=first.get("location");absolute=self.base+location if location and location.startswith("/") else location
            self.record(3,[self.exact("redirect HTTP status",first.get("status"),302),self.exact("redirect Location",absolute,self.base+f"/{l}/about")],{"redirects":redirects})
        elif j in (5,6):
            status=self.goto("search");self.record(1,[self.exact("HTTP status",status,200)])
            query="atlas" if j==5 else "zzzz-no-match"
            self.page.locator("#search-query").fill(query);self.click("#search-submit")
            s=self.state();self.record(2,[self.exact("query retained",s["elements"]["search-query"]["value"],query)])
            s=self.state();e=s["elements"]
            if j==5:
                self.record(3,[self.exact("result count",s["result_count"],1),self.exact("empty state absent",e["empty-state"]["present"],False),self.exact("result title",e["result-about"].get("text"),c["about"])])
                self.click("#result-about");self.record(4,self.page_checks(l,"about",c["about"]))
            else:
                self.record(3,[self.exact("result count",s["result_count"],0),self.exact("query retained",e["search-query"]["value"],query),self.exact("empty state visible",e["empty-state"].get("visible"),True),self.exact("localized empty message",e["empty-state"].get("text"),c["empty"])])
        elif j==7:
            status=self.goto("contact");s=self.state();e=s["elements"]
            self.record(1,[self.exact("HTTP status",status,200)]+[self.exact(name+" initially empty",e[name].get("value"),"") for name in ("contact-name","contact-email")])
            self.click("#contact-submit");self.record(2,details={"actual_action":"Clicked local form submit once with empty fields."})
            e=self.state()["elements"]
            self.record(3,[self.exact(name+" visible",e[name].get("visible"),True) for name in ("name-error","email-error")]+[self.exact(name+" aria-invalid",e[name].get("aria_invalid"),"true") for name in ("contact-name","contact-email")]+[self.exact("confirmation hidden",e["confirmation"].get("visible"),False)])
            self.record(4,[self.exact("name error copy",e["name-error"].get("text"),c["name_error"]),self.exact("email error copy",e["email-error"].get("text"),c["email_error"])])
        elif j==8:
            status=self.goto("contact");e=self.state()["elements"]
            self.record(1,[self.exact("HTTP status",status,200)]+[self.exact(name+" has visible associated label",any(label["visible"] and label["text"] for label in e[name].get("labels",[])),True) for name in ("contact-name","contact-email")])
            self.page.locator("#contact-name").focus();self.page.keyboard.type("Alex Test");self.page.keyboard.press("Tab")
            self.record(2,details={"key_sequence":["focus #contact-name","type Alex Test","Tab"]})
            s=self.state();outline=s["elements"]["contact-email"].get("outline",{});width=outline.get("width","0px")
            visible_outline=outline.get("style") not in (None,"none","hidden") and float(width.replace("px",""))>0 and outline.get("color") not in ("transparent","rgba(0, 0, 0, 0)")
            self.record(3,[self.exact("active element after first Tab",s["active_id"],"contact-email"),self.exact("email visible focus outline",visible_outline and s["active_id"]=="contact-email",True)],{"email_outline":outline})
            if s["active_id"]!="contact-email":
                self.skip(4,"Not executed: the first Tab skipped the required email field. No direct fill or click workaround was used.")
                self.skip(5,"Not executed: the contracted keyboard submission could not continue after the failed focus transition.")
                return
            self.page.keyboard.type("alex@example.test");self.page.keyboard.press("Tab");active=self.state()["active_id"]
            if active=="contact-submit":self.page.keyboard.press("Enter")
            self.record(4,[self.exact("active element after second Tab",active,"contact-submit")],{"key_sequence":["type alex@example.test","Tab"]+(["Enter"] if active=="contact-submit" else []),"active_before_enter":active})
            if active!="contact-submit":self.skip(5,"Not executed: the second Tab did not reach the submit button.");return
            e=self.state()["elements"]
            self.record(5,[self.exact("confirmation visible",e["confirmation"].get("visible"),True),self.exact("localized confirmation",e["confirmation"].get("text"),c["confirmation"])]+[self.exact(name+" hidden",e[name].get("visible"),False) for name in ("name-error","email-error")])
        elif j==9:
            self.goto("");e=self.state()["elements"]
            self.record(1,[self.exact("toggle visible",e["menu-toggle"].get("visible"),True),self.exact("panel hidden",e["mobile-menu"].get("visible"),False),self.exact("aria-expanded",e["menu-toggle"].get("aria_expanded"),"false")])
            self.click("#menu-toggle");e=self.state()["elements"]
            self.record(2,[self.exact("panel visible",e["mobile-menu"].get("visible"),True),self.exact("aria-expanded",e["menu-toggle"].get("aria_expanded"),"true")])
            self.click("#mobile-about");e=self.state()["elements"]
            self.record(3,self.page_checks(l,"about",c["about"])+[self.exact("panel closed after navigation",e["mobile-menu"].get("visible"),False)])
            opened_by_click=False
            if not self.page.locator("#mobile-menu").is_visible():self.click("#menu-toggle");opened_by_click=True
            before=self.state();self.page.keyboard.press("Escape");s=self.state();e=s["elements"]
            self.record(4,[self.exact("panel hidden after Escape",e["mobile-menu"].get("visible"),False),self.exact("aria-expanded after Escape",e["menu-toggle"].get("aria_expanded"),"false"),self.exact("focus returned to toggle",s["active_id"],"menu-toggle")],{"reopened_with_toggle":opened_by_click,"before_escape_panel_visible":before["elements"]["mobile-menu"].get("visible"),"keys":["Escape"]})
        elif j==10:
            status=self.goto("offer");self.record(1,[self.exact("HTTP status",status,200)])
            s=self.state();self.record(2,[self.exact(field,s["elements"][field].get("text"),c[field]) for field in ("offer-title","offer-price","offer-date","offer-cta")])
            s=self.state();self.record(3,[{"check":"horizontal overflow","passed":s["scroll_width"]<=s["inner_width"]+1,"expected":"scrollWidth <= innerWidth + 1","actual":{"scrollWidth":s["scroll_width"],"innerWidth":s["inner_width"]}}])
            s=self.state();e=s["elements"]["offer-cta"];r=e["rect"]
            within=e.get("visible") and r["x"]>=0 and r["y"]>=0 and r["right"]<=s["inner_width"] and r["bottom"]<=s["inner_height"]
            self.click("#offer-cta")
            self.record(4,[self.exact("CTA initially within viewport",within,True)]+self.page_checks(l,"contact"),{"cta_before_click":e,"viewport_before_click":{"width":s["inner_width"],"height":s["inner_height"]},"actual_click":True})

    def attempt_case(self,spec,number):
        self.attempt=number;self.case_id=spec["id"];self.journey=int(spec["journey_id"][1:]);self.language=spec["language"]
        self.responses=[];self.console=[];self.current_steps=[]
        cfg_profile=profile(spec["profile_id"]=="mobile",self.browser.version)
        context=self.browser.new_context(viewport=cfg_profile["viewport"],locale="en-GB",timezone_id="UTC",is_mobile=False,has_touch=False,service_workers="block")
        context.route("**/*",self.guard)
        self.page=context.new_page();self.page.set_default_timeout(5000);self.page.set_default_navigation_timeout(8000)
        self.page.on("request",self.request);self.page.on("response",self.response)
        self.page.on("console",lambda msg:self.console.append({"at":utc(),"type":msg.type,"text":msg.text}))
        self.page.on("pageerror",lambda exc:self.console.append({"at":utc(),"type":"pageerror","text":str(exc)}))
        self.page.on("requestfailed",lambda req:self.responses.append({"at":utc(),"url":req.url,"request_failed":req.failure,"resource_type":req.resource_type}))
        started=utc();incident=None
        try:self.run_steps()
        except Exception as exc:
            incident=type(exc).__name__+": "+str(exc)
            n=len(self.current_steps)+1
            if n<=len(STEPS[self.journey-1]):
                try:self.record(n,details={"tooling_incident":incident},status="BLOCKED")
                except Exception:
                    action,expected=STEPS[self.journey-1][n-1]
                    self.current_steps.append({"number":n,"action":action,"expected":expected,"observed":"Browser/driver incident: "+incident,"status":"BLOCKED","evidence_ids":[]})
            for later in range(len(self.current_steps)+1,len(STEPS[self.journey-1])+1):self.skip(later,"Not executed after the browser/driver incident.")
        statuses=[x["status"] for x in self.current_steps]
        status=next((x for x in ("FAIL","BLOCKED","NOT_RUN","PASS","NOT_APPLICABLE") if x in statuses),"NOT_RUN")
        prefix=f"{self.case_id}-a{number}"
        network=self.save(prefix+"-network.json","NETWORK",{"case_id":self.case_id,"attempt":number,"responses":self.responses},"Sanitized response status, redirect Location and request-failure observations; no bodies, cookies or request headers.")
        console=self.save(prefix+"-console.json","CONSOLE",{"case_id":self.case_id,"attempt":number,"messages":self.console},"Console and page-error observations captured for this attempt.")
        record={"case_id":self.case_id,"attempt":number,"started_at":started,"finished_at":utc(),"status":status,"incident":incident,"steps":self.current_steps,"final_url":self.page.url}
        attempt_record=self.save(prefix+"-attempt.json","TEXT",record,"Ordered actual steps and partial states for this complete recorded attempt.")
        evidence_ids=[eid for step in self.current_steps for eid in step["evidence_ids"]]+[network,console,attempt_record]
        return {"number":number,"status":status,"observed":("Browser/driver incident: "+incident if incident else "Actual step outcomes: "+", ".join(f"{s['number']} {s['status']}" for s in self.current_steps)),"evidence_ids":evidence_ids},record,cfg_profile

    def run(self):
        with sync_playwright() as p:
            stdout=(self.session/"chromium.log").open("xb")
            exe=p.chromium.executable_path
            command=[exe,"--headless=new","--no-sandbox","--disable-dev-shm-usage","--disable-background-networking","--disable-component-update","--disable-default-apps","--no-first-run","--no-default-browser-check","--disable-sync","--metrics-recording-only","--password-store=basic","--use-mock-keychain",f"--remote-debugging-port={self.args.browser_port}","--remote-debugging-address=127.0.0.1",f"--user-data-dir={self.session/'profile'}","about:blank"]
            process=subprocess.Popen(command,stdout=stdout,stderr=subprocess.STDOUT,start_new_session=True)
            write_json(self.session/"process.json",{"pid":process.pid,"command":command,"started_at":utc(),"retained":True})
            last_error=None
            for i in range(40):
                try:self.browser=p.chromium.connect_over_cdp(f"http://127.0.0.1:{self.args.browser_port}",timeout=1000);break
                except Exception as exc:last_error=str(exc);time.sleep(.25)
            if self.browser is None:raise RuntimeError("Could not attach to retained Chromium: "+str(last_error))
            write_json(self.out/"environment.json",{"browser":"Chromium","version":self.browser.version,"playwright":importlib.metadata.version("playwright"),"python":os.sys.version,"os":os.uname().sysname,"pid":process.pid,"session":str(self.session),"is_mobile":False,"has_touch":False,"browser_locale":"en-GB","timezone":"UTC","start_at":self.started})
            for spec in self.config["cases"]:
                self.budget();attempts=[];records=[];all_evidence=[]
                for number in range(1,self.config["budgets"]["max_retries"]+2):
                    attempt,record,cfg_profile=self.attempt_case(spec,number)
                    attempts.append(attempt);records.append(record);all_evidence.extend(attempt["evidence_ids"])
                    if attempt["status"]=="PASS":break
                final=records[-1]
                case={"id":spec["id"],"journey_id":spec["journey_id"],"title":TITLES[int(spec["journey_id"][1:])-1],"critical":True,"started_at":records[0]["started_at"],"finished_at":final["finished_at"],"url":final["final_url"],"language":spec["language"],"profile":cfg_profile,"preconditions":["Fresh browser context for each recorded attempt.","Authorized loopback synthetic fixture; no authentication."],"test_data":self.config["journeys"][int(spec["journey_id"][1:])-1]["test_data"],"steps":final["steps"],"status":final["status"],"classification":"DEFECT" if final["status"]=="FAIL" else "TOOLING_INCIDENT" if final["incident"] else "NONE","attempts":attempts,"country":{"requested":None,"verified":None,"status":"NOT_APPLICABLE","same_network_context":False,"evidence_ids":[],"note":"No geographic verification requested."},"evidence_ids":all_evidence,"limitations":["Mobile profile is viewport emulation only; is_mobile false and has_touch false."] if spec["profile_id"]=="mobile" else [],"uncertainties":[]}
                if any(r["incident"] for r in records):case["limitations"].append("One or more attempts encountered a browser/driver incident; inspect preserved attempt evidence.")
                self.cases.append(case)
                write_json(self.out/f"case-{spec['id']}.json",case)
                print(json.dumps({"completed_case":spec["id"],"status":case["status"],"attempts":len(attempts)},ensure_ascii=False),flush=True)
            finished=utc()
            limitations=["Synthetic local demo only; no production-readiness claim.","Only Chromium with desktop 1440x900 and narrow 390x844 viewports; no physical mobile device.","No geography verification or traces collected; no performance or comprehensive accessibility/SEO audit.","Scope interception restricts target requests; browser-level background traffic is not independently firewall-verified.","Retained Chromium process and profile avoid driver cleanup; each attempt used a fresh context."]
            obs={"schema_version":"1.0","campaign":{"id":self.config["campaign_id"],"started_at":self.started,"finished_at":finished,"base_url":self.base,"environment":"LOCAL","output_language":"en","capabilities":{"extraction":True,"interaction":True,"screenshots":True,"network":True,"console":True,"traces":False,"geography":False},"limitations":limitations},"evidence":self.evidence,"cases":self.cases,"tickets":[]}
            write_json(self.out/"observations.json",obs)
            write_json(self.out/"execution-budget.json",{"started_at":self.started,"finished_at":finished,"elapsed_seconds":round(time.monotonic()-self.clock,3),"planned_cases":len(self.config["cases"]),"recorded_cases":len(self.cases),"attempts":sum(len(c["attempts"]) for c in self.cases),"page_navigations":self.navigations,"first_party_requests":self.requests,"blocked_out_of_scope":self.outside,"limits":self.config["budgets"],"retained_browser_pid":process.pid})
            print(json.dumps({"observations":str(self.out/"observations.json"),"cases":len(self.cases),"evidence_files":len(self.evidence),"page_navigations":self.navigations,"requests":self.requests,"browser_pid":process.pid}),flush=True)
        # Do not stop the manually launched browser or remove any artifact.

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest="mode",required=True)
    create=sub.add_parser("create-config")
    create.add_argument("--base-url",required=True);create.add_argument("--campaign-id",required=True);create.add_argument("--output",required=True);create.add_argument("--delivery",required=True)
    run=sub.add_parser("run")
    run.add_argument("--config",required=True);run.add_argument("--output",required=True);run.add_argument("--session-dir",required=True);run.add_argument("--browser-port",type=int,required=True)
    args=parser.parse_args()
    if args.mode=="create-config":create_config(args)
    else:Audit(args).run()

if __name__=="__main__":main()
