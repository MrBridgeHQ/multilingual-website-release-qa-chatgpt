#!/usr/bin/env python3
"""Serve the synthetic Atlas Studio fixture; no third-party dependency is needed."""

from __future__ import annotations

import argparse
import html
import json
import socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlencode, urlsplit


TEXT = {
    "en": {
        "home": "Welcome to Atlas Studio",
        "about": "About Atlas Studio",
        "search": "Search Atlas Studio",
        "contact": "Contact Atlas Studio",
        "offer": "Our offer",
        "home_nav": "Home",
        "about_nav": "About",
        "search_nav": "Search",
        "contact_nav": "Contact",
        "offer_nav": "Offer",
        "menu": "Menu",
        "switch": "Français",
        "intro": "A fictional studio with a fully local demonstration website.",
        "about_text": "Atlas Studio creates clear, accessible digital experiences.",
        "search_label": "Search terms",
        "search_button": "Search",
        "empty": "No results found.",
        "name": "Name",
        "email": "Email",
        "submit": "Send local request",
        "name_error": "Enter your name.",
        "email_error": "Enter a valid email address.",
        "confirmation": "Thank you, {name}. Your local request is confirmed.",
        "privacy": "This fictional form sends no message and stores no data.",
        "offer_title": "Starter plan",
        "offer_price": "€19.90 / month",
        "offer_date": "October 8, 2026",
        "offer_cta": "Contact us",
        "offer_description": "A clear starting point for your next website.",
        "skip": "Skip to content",
    },
    "fr": {
        "home": "Bienvenue chez Atlas Studio",
        "about": "À propos d’Atlas Studio",
        "search": "Rechercher chez Atlas Studio",
        "contact": "Contacter Atlas Studio",
        "offer": "Notre offre",
        "home_nav": "Accueil",
        "about_nav": "À propos",
        "search_nav": "Recherche",
        "contact_nav": "Contact",
        "offer_nav": "Offre",
        "menu": "Menu",
        "switch": "English",
        "intro": "Un studio fictif et un site de démonstration entièrement local.",
        "about_text": "Atlas Studio crée des expériences numériques claires et accessibles.",
        "search_label": "Termes de recherche",
        "search_button": "Rechercher",
        "empty": "Aucun résultat.",
        "name": "Nom",
        "email": "E-mail",
        "submit": "Envoyer la demande locale",
        "name_error": "Saisissez votre nom.",
        "email_error": "Saisissez une adresse e-mail valide.",
        "confirmation": "Merci, {name}. Votre demande locale est confirmée.",
        "privacy": "Ce formulaire fictif n’envoie aucun message et ne conserve aucune donnée.",
        "offer_title": "Offre Découverte",
        "offer_price": "19,90 € / mois",
        "offer_date": "8 octobre 2026",
        "offer_cta": "Contactez-nous",
        "offer_description": "Un point de départ clair pour votre prochain site web.",
        "skip": "Aller au contenu",
    },
}

STYLE = """
* { box-sizing: border-box; }
[hidden] { display: none !important; }
body { margin: 0; font: 17px/1.5 system-ui, sans-serif; color: #17324a; background: #f7fafc; }
a { color: #12588b; }
button, input { font: inherit; }
button, .button { border: 1px solid #12588b; border-radius: .35rem; padding: .7rem 1rem; background: #12588b; color: white; cursor: pointer; }
.button { display: inline-block; text-decoration: none; }
:focus-visible { outline: 3px solid #c34f00; outline-offset: 3px; }
header { background: white; border-bottom: 1px solid #c9d6df; padding: 1rem 1.5rem; }
.header-row { display: flex; gap: 1.2rem; align-items: center; flex-wrap: wrap; }
.brand { font-weight: 750; text-decoration: none; }
.desktop-nav { display: flex; gap: 1rem; }
#language-switch { margin-left: auto; }
#menu-toggle, #mobile-menu { display: none; }
main { max-width: 70rem; margin: 0 auto; padding: 2rem 1.5rem; }
h1 { line-height: 1.2; margin: 0 0 1.2rem; }
form { max-width: 35rem; }
.field { margin-bottom: 1.2rem; }
label { display: block; margin-bottom: .4rem; font-weight: 650; }
input { display: block; width: 100%; padding: .65rem; border: 1px solid #617889; border-radius: .25rem; }
.error { margin: .4rem 0 0; color: #a81824; }
#confirmation { background: #dcefe3; border: 1px solid #28744d; padding: 1rem; margin-top: 1rem; }
.offer-card { max-width: 38rem; padding: 1.5rem; border: 1px solid #bacddb; border-radius: .75rem; background: white; }
#offer-price { font-size: 1.8rem; font-weight: 700; }
#offer-cta { margin-top: 1rem; }
.search-result { padding: .75rem 0; }
.skip { position: absolute; left: -10000px; top: .4rem; background: white; padding: .5rem; z-index: 10; }
.skip:focus { left: .4rem; }
footer { padding: 2rem 1.5rem; color: #4c6374; }
@media (max-width: 640px) {
  header { padding: .8rem 1rem; }
  .header-row { gap: .7rem; }
  .brand { flex-basis: 100%; }
  .desktop-nav { display: none; }
  #menu-toggle { display: inline-block; }
  #mobile-menu { display: flex; flex-direction: column; gap: .8rem; padding: 1rem 0 .3rem; }
  #language-switch { margin-left: auto; }
  main { padding: 1.5rem 1rem; }
  h1 { font-size: 1.8rem; }
  .offer-card { padding: 1rem; }
  .wide-offer { width: 540px; min-width: 540px; }
}
"""

SCRIPT = r"""
const toggle = document.getElementById('menu-toggle');
const menu = document.getElementById('mobile-menu');
function closeMenu() {
  menu.hidden = true;
  toggle.setAttribute('aria-expanded', 'false');
}
toggle.addEventListener('click', () => {
  const opening = toggle.getAttribute('aria-expanded') !== 'true';
  menu.hidden = !opening;
  toggle.setAttribute('aria-expanded', String(opening));
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && !menu.hidden) {
    closeMenu();
    toggle.focus();
  }
});
const form = document.getElementById('contact-form');
if (form) {
  const copy = JSON.parse(document.getElementById('form-copy').textContent);
  const nameField = document.getElementById('contact-name');
  const emailField = document.getElementById('contact-email');
  const nameError = document.getElementById('name-error');
  const emailError = document.getElementById('email-error');
  const confirmation = document.getElementById('confirmation');
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const nameValid = nameField.value.trim().length > 0;
    const emailValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailField.value.trim());
    nameError.textContent = copy.name_error;
    emailError.textContent = copy.email_error;
    nameError.hidden = nameValid;
    emailError.hidden = emailValid;
    nameField.setAttribute('aria-invalid', String(!nameValid));
    emailField.setAttribute('aria-invalid', String(!emailValid));
    confirmation.hidden = !(nameValid && emailValid);
    if (nameValid && emailValid) {
      confirmation.textContent = copy.confirmation.replace('{name}', nameField.value.trim());
    }
  });
}
"""


def escape(value: str) -> str:
    return html.escape(value, quote=True)


def route(language: str, page: str) -> str:
    return f"/{language}/" if page == "home" else f"/{language}/{page}"


def document(language: str, page: str, query: str, base: str, variant: str) -> str:
    text = TEXT[language]
    baseline = variant == "baseline"
    other_language = "fr" if language == "en" else "en"
    about_path = route(language, "search" if baseline and language == "fr" else "about")
    switch_page = "home" if baseline and language == "en" and page == "about" else page
    switch_path = route(other_language, switch_page)
    if page == "search" and query:
        switch_path += "?" + urlencode({"q": query})
    navigation = []
    mobile_navigation = []
    for target in ("home", "about", "search", "contact", "offer"):
        destination = about_path if target == "about" else route(language, target)
        navigation.append(f'<a id="main-{target}" href="{escape(destination)}">{escape(text[target + "_nav"])}</a>')
        mobile_navigation.append(f'<a id="mobile-{target}" href="{route(language, target)}">{escape(text[target + "_nav"])}</a>')

    if page == "home":
        content = f'<p>{escape(text["intro"])}</p><p><a class="button" href="{route(language, "offer")}">{escape(text["offer_nav"])}</a></p>'
    elif page == "about":
        content = f'<p>{escape(text["about_text"])}</p>'
    elif page == "search":
        result = ""
        if query.strip().lower() == "atlas":
            result = f'<div class="search-result"><a id="result-about" href="{route(language, "about")}">{escape(text["about"])}</a></div>'
        elif query:
            result = f'<p id="empty-state">{escape(text["empty"])}</p>'
        content = f'''<form id="search-form" action="{route(language, "search")}" method="get">
<div class="field"><label for="search-query">{escape(text["search_label"])}</label>
<input id="search-query" name="q" type="search" value="{escape(query)}"></div>
<button id="search-submit" type="submit">{escape(text["search_button"])}</button></form>
<div id="search-results" aria-live="polite">{result}</div>'''
    elif page == "contact":
        error_copy = TEXT["en"] if baseline and language == "fr" else text
        form_copy = json.dumps({"name_error": error_copy["name_error"], "email_error": error_copy["email_error"], "confirmation": text["confirmation"]}, ensure_ascii=False).replace("<", "\\u003c")
        email_tabindex = ' tabindex="-1"' if baseline and language == "en" else ""
        content = f'''<p>{escape(text["privacy"])}</p>
<form id="contact-form" novalidate>
<div class="field"><label for="contact-name">{escape(text["name"])}</label>
<input id="contact-name" name="name" autocomplete="off" aria-describedby="name-error" aria-invalid="false">
<p class="error" id="name-error" role="alert" hidden></p></div>
<div class="field"><label for="contact-email">{escape(text["email"])}</label>
<input id="contact-email" name="email" type="email" autocomplete="off" aria-describedby="email-error" aria-invalid="false"{email_tabindex}>
<p class="error" id="email-error" role="alert" hidden></p></div>
<button id="contact-submit" type="submit">{escape(text["submit"])}</button>
</form><p id="confirmation" role="status" hidden></p>
<script type="application/json" id="form-copy">{form_copy}</script>'''
    elif page == "offer":
        wide_class = " wide-offer" if baseline and language == "fr" else ""
        content = f'''<section class="offer-card{wide_class}" aria-labelledby="offer-title">
<h2 id="offer-title">{escape(text["offer_title"])}</h2>
<p id="offer-price">{escape(text["offer_price"])}</p>
<p id="offer-date">{escape(text["offer_date"])}</p>
<p>{escape(text["offer_description"])}</p>
<a class="button" id="offer-cta" href="{route(language, "contact")}">{escape(text["offer_cta"])}</a>
</section>'''
    else:
        raise ValueError(f"Unknown page: {page}")

    canonical = base + route(language, page)
    alternates = "".join(f'<link rel="alternate" hreflang="{lang}" href="{base}{route(lang, page)}">' for lang in ("en", "fr"))
    return f'''<!doctype html>
<html lang="{language}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(text[page])}</title><link rel="canonical" href="{canonical}">{alternates}<style>{STYLE}</style></head>
<body><a class="skip" href="#main-content">{escape(text["skip"])}</a>
<header><div class="header-row"><a class="brand" href="{route(language, "home")}">Atlas Studio</a>
<nav class="desktop-nav" aria-label="{escape(text["menu"])}">{"".join(navigation)}</nav>
<button id="menu-toggle" type="button" aria-controls="mobile-menu" aria-expanded="false">{escape(text["menu"])}</button>
<a id="language-switch" href="{escape(switch_path)}" lang="{other_language}">{escape(text["switch"])}</a></div>
<nav id="mobile-menu" aria-label="{escape(text["menu"])}" hidden>{"".join(mobile_navigation)}</nav></header>
<main id="main-content"><h1 id="page-heading">{escape(text[page])}</h1>{content}</main>
<footer>Atlas Studio</footer><script>{SCRIPT}</script></body></html>'''


class FixtureServer(ThreadingHTTPServer):
    variant: str


class Handler(BaseHTTPRequestHandler):
    server: FixtureServer

    def log_message(self, format_string: str, *args: object) -> None:
        return

    def send_payload(self, status: int, payload: str, content_type: str = "text/html; charset=utf-8", extra: dict[str, str] | None = None) -> None:
        encoded = payload.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        for name, value in (extra or {}).items():
            self.send_header(name, value)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(encoded)

    def do_HEAD(self) -> None:
        self.do_GET()

    def do_GET(self) -> None:
        parsed = urlsplit(self.path)
        path = parsed.path
        if path == "/healthz":
            self.send_payload(200, json.dumps({"status": "ready", "variant": self.server.variant}), "application/json")
            return
        if path == "/favicon.ico":
            self.send_payload(204, "", "image/x-icon")
            return
        if path == "/auth-required":
            self.send_payload(401, "<!doctype html><html lang='en'><title>Authentication required</title><h1>Authentication required</h1><p>This local negative-test endpoint requires unavailable credentials.</p></html>", extra={"WWW-Authenticate": 'Basic realm="Synthetic fixture"'})
            return
        if path in ("/", "/en", "/fr"):
            destination = "/fr/" if path == "/fr" else "/en/"
            self.send_payload(302, "", extra={"Location": destination})
            return
        parts = path.strip("/").split("/")
        if len(parts) not in (1, 2) or parts[0] not in TEXT:
            self.send_payload(404, "<!doctype html><html lang='en'><title>Not found</title><h1>Not found</h1></html>")
            return
        language = parts[0]
        page = parts[1] if len(parts) == 2 else "home"
        if page == "legacy":
            destination_language = "en" if self.server.variant == "baseline" and language == "fr" else language
            self.send_payload(302, "", extra={"Location": route(destination_language, "about")})
            return
        if page not in ("home", "about", "search", "contact", "offer"):
            self.send_payload(404, "<!doctype html><html lang='en'><title>Not found</title><h1>Not found</h1></html>")
            return
        query = parse_qs(parsed.query).get("q", [""])[0][:200]
        base = f"http://127.0.0.1:{self.server.server_port}"
        self.send_payload(200, document(language, page, query, base, self.server.variant))

    def do_POST(self) -> None:
        self.send_payload(405, "Method not allowed. The local demo form has no network endpoint.", "text/plain; charset=utf-8", {"Allow": "GET, HEAD"})


def inspect_ports() -> dict[str, object]:
    ports = []
    for port in (39175, 39176):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
                probe.bind(("127.0.0.1", port))
            ports.append({"host": "127.0.0.1", "port": port, "available": True})
        except OSError as error:
            ports.append({"host": "127.0.0.1", "port": port, "available": False, "reason": str(error)})
    return {"fixture": "Atlas Studio", "dependencies": "Python standard library", "ports": ports}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", required=True, choices=("inspect", "serve"))
    parser.add_argument("--variant", choices=("baseline", "corrected"), default="baseline")
    parser.add_argument("--port", type=int)
    args = parser.parse_args()
    if args.mode == "inspect":
        print(json.dumps(inspect_ports(), indent=2))
        return
    port = args.port if args.port is not None else (39175 if args.variant == "baseline" else 39176)
    if not 1024 <= port <= 65535:
        parser.error("Choose a non-privileged TCP port between 1024 and 65535.")
    with FixtureServer(("127.0.0.1", port), Handler) as server:
        server.variant = args.variant
        print(json.dumps({"status": "listening", "url": f"http://127.0.0.1:{port}", "variant": args.variant}), flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("Server stopped; no fixture files were changed.", flush=True)


if __name__ == "__main__":
    main()
