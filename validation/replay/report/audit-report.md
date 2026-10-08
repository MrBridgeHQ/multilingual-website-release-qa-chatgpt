# Multilingual Website Release QA

## Scope and environment

- **Campaign:** independent-ticket-replay-20261008-a1
- **Environment:** LOCAL
- **Starting URL:** http://127.0.0.1:39175
- **Execution period:** 2026-10-08T12:10:30.223057Z → 2026-10-08T12:10:33.676519Z

### Observed tool capabilities

- extraction: true
- interaction: true
- screenshots: true
- network: true
- console: true
- traces: false
- geography: false

## Summary

- **Scoped verdict:** ISSUES_FOUND
- **Executed case outcomes / planned cases:** 6/6
- **Critical cases without a completed outcome:** None

This verdict applies only to the explicitly planned cases and observed environment.

| Status | n |
| --- | ---: |
| PASS | 0 |
| FAIL | 6 |
| BLOCKED | 0 |
| NOT_RUN | 0 |
| NOT_APPLICABLE | 0 |

## Test matrix

| Case | Journey | Language | Profile | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| REPLAY-QA-001 | REPLAY-QA-001 | fr | desktop | FAIL | [REPLAY-QA-001-a1-opened](evidence/REPLAY-QA-001-a1-opened.json), [REPLAY-QA-001-a1-destination](evidence/REPLAY-QA-001-a1-destination.json), [REPLAY-QA-001-a1-destination-viewport](evidence/REPLAY-QA-001-a1-destination-viewport.png), [REPLAY-QA-001-a1-network](evidence/REPLAY-QA-001-a1-network.json), [REPLAY-QA-001-a1-console](evidence/REPLAY-QA-001-a1-console.json) |
| REPLAY-QA-002 | REPLAY-QA-002 | en | desktop | FAIL | [REPLAY-QA-002-a1-opened](evidence/REPLAY-QA-002-a1-opened.json), [REPLAY-QA-002-a1-destination](evidence/REPLAY-QA-002-a1-destination.json), [REPLAY-QA-002-a1-destination-viewport](evidence/REPLAY-QA-002-a1-destination-viewport.png), [REPLAY-QA-002-a1-network](evidence/REPLAY-QA-002-a1-network.json), [REPLAY-QA-002-a1-console](evidence/REPLAY-QA-002-a1-console.json) |
| REPLAY-QA-003 | REPLAY-QA-003 | fr | desktop | FAIL | [REPLAY-QA-003-a1-opened](evidence/REPLAY-QA-003-a1-opened.json), [REPLAY-QA-003-a1-final-viewport](evidence/REPLAY-QA-003-a1-final-viewport.png), [REPLAY-QA-003-a1-network](evidence/REPLAY-QA-003-a1-network.json), [REPLAY-QA-003-a1-console](evidence/REPLAY-QA-003-a1-console.json) |
| REPLAY-QA-004 | REPLAY-QA-004 | fr | desktop | FAIL | [REPLAY-QA-004-a1-opened](evidence/REPLAY-QA-004-a1-opened.json), [REPLAY-QA-004-a1-validation](evidence/REPLAY-QA-004-a1-validation.json), [REPLAY-QA-004-a1-validation-viewport](evidence/REPLAY-QA-004-a1-validation-viewport.png), [REPLAY-QA-004-a1-network](evidence/REPLAY-QA-004-a1-network.json), [REPLAY-QA-004-a1-console](evidence/REPLAY-QA-004-a1-console.json) |
| REPLAY-QA-005 | REPLAY-QA-005 | en | desktop | FAIL | [REPLAY-QA-005-a1-opened](evidence/REPLAY-QA-005-a1-opened.json), [REPLAY-QA-005-a1-name-keyboard](evidence/REPLAY-QA-005-a1-name-keyboard.json), [REPLAY-QA-005-a1-after-one-tab](evidence/REPLAY-QA-005-a1-after-one-tab.json), [REPLAY-QA-005-a1-focus-viewport](evidence/REPLAY-QA-005-a1-focus-viewport.png), [REPLAY-QA-005-a1-network](evidence/REPLAY-QA-005-a1-network.json), [REPLAY-QA-005-a1-console](evidence/REPLAY-QA-005-a1-console.json) |
| REPLAY-QA-006 | REPLAY-QA-006 | fr | mobile | FAIL | [REPLAY-QA-006-a1-opened](evidence/REPLAY-QA-006-a1-opened.json), [REPLAY-QA-006-a1-offer-viewport](evidence/REPLAY-QA-006-a1-offer-viewport.png), [REPLAY-QA-006-a1-cta-destination](evidence/REPLAY-QA-006-a1-cta-destination.json), [REPLAY-QA-006-a1-contact-viewport](evidence/REPLAY-QA-006-a1-contact-viewport.png), [REPLAY-QA-006-a1-network](evidence/REPLAY-QA-006-a1-network.json), [REPLAY-QA-006-a1-console](evidence/REPLAY-QA-006-a1-console.json) |

## Detailed defect tickets

### QA-001 — French desktop About navigation opens Search

**User impact:** A French desktop visitor selecting À propos is taken to Search and cannot reach the intended information through that primary link.

**Severity:** MAJOR
**Severity rationale:** The French desktop primary About link reaches the wrong section. This replay does not establish the availability of alternate navigation routes.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/fr/", "http://127.0.0.1:39175/fr/search"], "languages": ["fr"], "profiles": ["desktop"]}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 1440 x 900 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

**Non-sensitive test data:** {}

**Reproduction steps**

1. Open http://127.0.0.1:39175/fr/ at 1440 × 900.
2. Click the visible À propos link #main-about.
3. Inspect the actual URL and #page-heading.

**Expected:** The destination is /fr/about, HTTP 200, html[lang]=fr, heading À propos d’Atlas Studio.

**Observed:** #main-about href=/fr/search; actual destination http://127.0.0.1:39175/fr/search. Final URL http://127.0.0.1:39175/fr/search; HTTP 200; html[lang]=fr; heading Rechercher chez Atlas Studio.

**Evidence:** [REPLAY-QA-001-a1-opened](evidence/REPLAY-QA-001-a1-opened.json), [REPLAY-QA-001-a1-destination](evidence/REPLAY-QA-001-a1-destination.json), [REPLAY-QA-001-a1-destination-viewport](evidence/REPLAY-QA-001-a1-destination-viewport.png), [REPLAY-QA-001-a1-network](evidence/REPLAY-QA-001-a1-network.json), [REPLAY-QA-001-a1-console](evidence/REPLAY-QA-001-a1-console.json)
**Related cases:** REPLAY-QA-001
**Reproduction frequency:** 1/1

**Correction hypothesis:** The observed desktop #main-about href points at the search route. Correcting its route binding to /fr/about is a hypothesis to verify in implementation; no source was inspected.

**Acceptance criteria**

- Clicking #main-about from /fr/ reaches /fr/about and the approved localized heading.
- The English desktop primary navigation continues to reach /en/about.
- The already working French mobile #mobile-about route remains /fr/about.

**Retest procedure**

1. Repeat the numbered reproduction for REPLAY-QA-001 against the corrected origin in a new campaign.
2. Execute the ticket's separate acceptance witness journeys; they were not part of this replay.

### QA-002 — Switching About from English to French loses the internal page

**User impact:** A visitor reading the English About page loses that page when selecting French and arrives at the French home page.

**Severity:** MAJOR
**Severity rationale:** The English About language switch loses the current page identity when reaching French home.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/en/about", "http://127.0.0.1:39175/fr/"], "languages": ["en"], "profiles": ["desktop"]}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 1440 x 900 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

**Non-sensitive test data:** {}

**Reproduction steps**

1. Open http://127.0.0.1:39175/en/about at 1440 × 900.
2. Click the Français control #language-switch.
3. Read the destination URL, html[lang] and #page-heading.

**Expected:** The destination is /fr/about with html[lang]=fr and heading À propos d’Atlas Studio.

**Observed:** #language-switch href=/fr/; actual destination http://127.0.0.1:39175/fr/. Final URL http://127.0.0.1:39175/fr/; HTTP 200; html[lang]=fr; heading Bienvenue chez Atlas Studio.

**Evidence:** [REPLAY-QA-002-a1-opened](evidence/REPLAY-QA-002-a1-opened.json), [REPLAY-QA-002-a1-destination](evidence/REPLAY-QA-002-a1-destination.json), [REPLAY-QA-002-a1-destination-viewport](evidence/REPLAY-QA-002-a1-destination-viewport.png), [REPLAY-QA-002-a1-network](evidence/REPLAY-QA-002-a1-network.json), [REPLAY-QA-002-a1-console](evidence/REPLAY-QA-002-a1-console.json)
**Related cases:** REPLAY-QA-002
**Reproduction frequency:** 1/1

**Correction hypothesis:** The rendered language switch appears to use the French entry route rather than the equivalent About route. Derive the alternate target from the current route; root cause has not been inspected.

**Acceptance criteria**

- EN About → Français reaches /fr/about, preserving page identity.
- FR About → English still reaches /en/about.
- Both destination headings and html languages match their target routes.

**Retest procedure**

1. Repeat the numbered reproduction for REPLAY-QA-002 against the corrected origin in a new campaign.
2. Execute the ticket's separate acceptance witness journeys; they were not part of this replay.

### QA-003 — French legacy redirect switches the visitor to English

**User impact:** A visitor following the French legacy URL receives the English About page and loses the requested language.

**Severity:** MAJOR
**Severity rationale:** The French legacy entry redirects to an English document, losing the requested language.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/fr/legacy", "http://127.0.0.1:39175/en/about"], "languages": ["fr"], "profiles": ["desktop"]}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 1440 x 900 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

**Non-sensitive test data:** {}

**Reproduction steps**

1. Open http://127.0.0.1:39175/fr/legacy at 1440 × 900.
2. Capture the redirect status and Location.
3. Inspect the final URL, document language and heading.

**Expected:** /fr/legacy returns HTTP 302 with Location /fr/about; the final page returns HTTP 200, html[lang]=fr and heading À propos d’Atlas Studio.

**Observed:** Legacy response HTTP 302; Location /en/about. Final URL http://127.0.0.1:39175/en/about; HTTP 200; html[lang]=en; heading About Atlas Studio.

**Evidence:** [REPLAY-QA-003-a1-opened](evidence/REPLAY-QA-003-a1-opened.json), [REPLAY-QA-003-a1-final-viewport](evidence/REPLAY-QA-003-a1-final-viewport.png), [REPLAY-QA-003-a1-network](evidence/REPLAY-QA-003-a1-network.json), [REPLAY-QA-003-a1-console](evidence/REPLAY-QA-003-a1-console.json)
**Related cases:** REPLAY-QA-003
**Reproduction frequency:** 1/1

**Correction hypothesis:** The redirect Location is visibly bound to the English route. Preserve the incoming language when selecting the About target; this implementation hypothesis has not been source-verified.

**Acceptance criteria**

- French legacy returns HTTP 302 to /fr/about, followed by a 200 French About document.
- English legacy still returns HTTP 302 to /en/about, followed by a 200 English About document.

**Retest procedure**

1. Repeat the numbered reproduction for REPLAY-QA-003 against the corrected origin in a new campaign.
2. Execute the ticket's separate acceptance witness journeys; they were not part of this replay.

### QA-004 — French form validation errors are displayed in English

**User impact:** French visitors receive English instructions for correcting missing name and email fields.

**Severity:** MINOR
**Severity rationale:** The empty form is rejected and invalid fields are identified, but the French document shows English correction messages.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/fr/contact"], "languages": ["fr"], "profiles": ["desktop"]}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 1440 x 900 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

**Non-sensitive test data:** {"name": "", "email": ""}

**Reproduction steps**

1. Open http://127.0.0.1:39175/fr/contact at 1440 × 900.
2. Leave #contact-name and #contact-email empty.
3. Click #contact-submit once.
4. Read #name-error and #email-error.

**Expected:** Visible messages are Saisissez votre nom. and Saisissez une adresse e-mail valide.; both fields have aria-invalid=true and confirmation stays hidden.

**Observed:** contact-name aria-invalid=true; contact-email aria-invalid=true; confirmation candidates=[{'id': 'confirmation', 'visible': False}]. #name-error='Enter your name.'; visible=True; #email-error='Enter a valid email address.'; visible=True.

**Evidence:** [REPLAY-QA-004-a1-opened](evidence/REPLAY-QA-004-a1-opened.json), [REPLAY-QA-004-a1-validation](evidence/REPLAY-QA-004-a1-validation.json), [REPLAY-QA-004-a1-validation-viewport](evidence/REPLAY-QA-004-a1-validation-viewport.png), [REPLAY-QA-004-a1-network](evidence/REPLAY-QA-004-a1-network.json), [REPLAY-QA-004-a1-console](evidence/REPLAY-QA-004-a1-console.json)
**Related cases:** REPLAY-QA-004
**Reproduction frequency:** 1/1

**Correction hypothesis:** The validation messages may be selected independently of the document language. Bind missing-name and missing/invalid-email copy to the active French locale; no validation source was read.

**Acceptance criteria**

- Empty French submission displays both exact approved French messages.
- Invalid fields remain marked aria-invalid=true; confirmation remains hidden.
- English empty validation and the French valid keyboard submission continue to work.

**Retest procedure**

1. Repeat the numbered reproduction for REPLAY-QA-004 against the corrected origin in a new campaign.
2. Execute the ticket's separate acceptance witness journeys; they were not part of this replay.

### QA-005 — English contact form skips the required email field during keyboard entry

**User impact:** The contracted forward keyboard sequence cannot enter the required email, preventing English keyboard-only completion.

**Severity:** MAJOR
**Severity rationale:** The required email field is skipped in the specified forward keyboard sequence, stopping completion of that sequence.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/en/contact"], "languages": ["en"], "profiles": ["desktop"]}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 1440 x 900 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

**Non-sensitive test data:** {"name": "Alex Test", "email": "alex@example.test"}

**Reproduction steps**

1. Open http://127.0.0.1:39175/en/contact at 1440 × 900.
2. Focus #contact-name and type Alex Test using keyboard input.
3. Press Tab exactly once.
4. Inspect document.activeElement.id and the visible focus outline. Do not click or fill the skipped email field.

**Expected:** The first Tab reaches #contact-email with a visible outline; after typing alex@example.test, the next Tab reaches #contact-submit and Enter displays the approved English confirmation.

**Observed:** Active element after one Tab is #contact-submit. Active element #contact-submit; outline={'style': 'solid', 'width': '3px', 'color': 'rgb(195, 79, 0)', 'offset': '3px'}; email value=''; email tabIndex=-1. Not run because the first Tab did not reach the email field. No click or direct fill was used to bypass the failed transition.

**Evidence:** [REPLAY-QA-005-a1-opened](evidence/REPLAY-QA-005-a1-opened.json), [REPLAY-QA-005-a1-name-keyboard](evidence/REPLAY-QA-005-a1-name-keyboard.json), [REPLAY-QA-005-a1-after-one-tab](evidence/REPLAY-QA-005-a1-after-one-tab.json), [REPLAY-QA-005-a1-focus-viewport](evidence/REPLAY-QA-005-a1-focus-viewport.png), [REPLAY-QA-005-a1-network](evidence/REPLAY-QA-005-a1-network.json), [REPLAY-QA-005-a1-console](evidence/REPLAY-QA-005-a1-console.json)
**Related cases:** REPLAY-QA-005
**Reproduction frequency:** 1/1

**Correction hypothesis:** The observed tabindex=-1 on #contact-email is consistent with exclusion from forward Tab order. Restore a normal focusable order and verify the visible focus indicator and complete keyboard submission; application source was not inspected.

**Acceptance criteria**

- The forward order is contact-name → contact-email → contact-submit.
- The focused email field and submit control have visible focus indications.
- Typing the supplied synthetic data and pressing Enter shows Thank you, Alex Test. Your local request is confirmed. without visible validation errors.
- The French keyboard form remains functional.

**Retest procedure**

1. Repeat the numbered reproduction for REPLAY-QA-005 against the corrected origin in a new campaign.
2. Execute the ticket's separate acceptance witness journeys; they were not part of this replay.

### QA-006 — French mobile offer overflows horizontally and clips its description

**User impact:** At 390 CSS pixels, the offer card extends beyond the viewport and its description is clipped until the visitor scrolls horizontally.

**Severity:** MINOR
**Severity rationale:** The mobile-width presentation overflows and clips content while the visible CTA still reaches French Contact.
**Diagnostic confidence:** HIGH

**Observed scope:** {"pages": ["http://127.0.0.1:39175/fr/offer", "http://127.0.0.1:39175/fr/contact"], "languages": ["fr"], "profiles": ["mobile"]}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 390 x 844 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

**Non-sensitive test data:** {}

**Reproduction steps**

1. Open http://127.0.0.1:39175/fr/offer with a 390 × 844 Chromium viewport.
2. Compare document.documentElement.scrollWidth with window.innerWidth.
3. Inspect the right edge of the offer card and description before interacting.
4. Click #offer-cta and record whether it remains visible and reaches French Contact.

**Expected:** scrollWidth is no greater than innerWidth + 1, the offer content fits without horizontal scrolling, and the visible CTA reaches /fr/contact.

**Observed:** scrollWidth=556; innerWidth=390; overflow=166 CSS pixels. Visible content boxes extending beyond the right viewport edge: [{'id': '', 'text': 'Offre Découverte\n19,90 € / mois\n8 octobre 2026\nUn point de départ clair pour votre prochain site web.\nContactez-nous', 'right': 556}, {'id': 'offer-title', 'text': 'Offre Découverte', 'right': 539}, {'id': 'offer-price', 'text': '19,90 € / mois', 'right': 539}, {'id': 'offer-date', 'text': '8 octobre 2026', 'right': 539}, {'id': '', 'text': 'Un point de départ clair pour votre prochain site web.', 'right': 539}]. CTA initially visible=True; within horizontal viewport=True; final URL http://127.0.0.1:39175/fr/contact; html[lang]=fr; heading Contacter Atlas Studio.

**Evidence:** [REPLAY-QA-006-a1-opened](evidence/REPLAY-QA-006-a1-opened.json), [REPLAY-QA-006-a1-offer-viewport](evidence/REPLAY-QA-006-a1-offer-viewport.png), [REPLAY-QA-006-a1-cta-destination](evidence/REPLAY-QA-006-a1-cta-destination.json), [REPLAY-QA-006-a1-contact-viewport](evidence/REPLAY-QA-006-a1-contact-viewport.png), [REPLAY-QA-006-a1-network](evidence/REPLAY-QA-006-a1-network.json), [REPLAY-QA-006-a1-console](evidence/REPLAY-QA-006-a1-console.json)
**Related cases:** REPLAY-QA-006
**Reproduction frequency:** 1/1

**Correction hypothesis:** An offer-card width or minimum-width constraint may exceed the French mobile container. Constrain the card/content to available viewport width and allow wrapping; the CSS implementation was not inspected.

**Acceptance criteria**

- At 390 × 844, document scrollWidth <= innerWidth + 1 and the full description fits without horizontal page scrolling.
- Approved French title, price and date remain unchanged.
- The CTA remains inside the viewport, can be clicked and reaches /fr/contact.
- English offer layout and CTA continue to pass.

**Retest procedure**

1. Repeat the numbered reproduction for REPLAY-QA-006 against the corrected origin in a new campaign.
2. Execute the ticket's separate acceptance witness journeys; they were not part of this replay.

## Case execution details

### REPLAY-QA-001 — Independent replay: French desktop About navigation opens Search

- URL: http://127.0.0.1:39175/fr/search
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T12:10:30.852725Z → 2026-10-08T12:10:31.363985Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No network-country requirement was specified for this loopback replay."}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 1440 x 900 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open http://127.0.0.1:39175/fr/ at 1440 × 900. | The specified page loads in the requested language and viewport. | HTTP 200; actual URL http://127.0.0.1:39175/fr/; html[lang]=fr; viewport {'width': 1440, 'height': 900}. | PASS | [REPLAY-QA-001-a1-opened](evidence/REPLAY-QA-001-a1-opened.json) |
| 2 | Click the visible À propos link #main-about. | The control reaches /fr/about. | #main-about href=/fr/search; actual destination http://127.0.0.1:39175/fr/search. | FAIL | [REPLAY-QA-001-a1-opened](evidence/REPLAY-QA-001-a1-opened.json), [REPLAY-QA-001-a1-destination](evidence/REPLAY-QA-001-a1-destination.json), [REPLAY-QA-001-a1-destination-viewport](evidence/REPLAY-QA-001-a1-destination-viewport.png) |
| 3 | Inspect the actual URL and #page-heading. | The destination is /fr/about, HTTP 200, html[lang]=fr, heading À propos d’Atlas Studio. | Final URL http://127.0.0.1:39175/fr/search; HTTP 200; html[lang]=fr; heading Rechercher chez Atlas Studio. | FAIL | [REPLAY-QA-001-a1-destination](evidence/REPLAY-QA-001-a1-destination.json), [REPLAY-QA-001-a1-destination-viewport](evidence/REPLAY-QA-001-a1-destination-viewport.png) |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "#main-about href=/fr/search; actual destination http://127.0.0.1:39175/fr/search. Final URL http://127.0.0.1:39175/fr/search; HTTP 200; html[lang]=fr; heading Rechercher chez Atlas Studio.", "evidence_ids": ["REPLAY-QA-001-a1-opened", "REPLAY-QA-001-a1-destination", "REPLAY-QA-001-a1-destination-viewport", "REPLAY-QA-001-a1-network", "REPLAY-QA-001-a1-console"]}]

**Limitations**

None

**Uncertainties**

None

### REPLAY-QA-002 — Independent replay: Switching About from English to French loses the internal page

- URL: http://127.0.0.1:39175/fr/
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T12:10:31.364674Z → 2026-10-08T12:10:31.883847Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No network-country requirement was specified for this loopback replay."}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 1440 x 900 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open http://127.0.0.1:39175/en/about at 1440 × 900. | The specified page loads in the requested language and viewport. | HTTP 200; actual URL http://127.0.0.1:39175/en/about; html[lang]=en; viewport {'width': 1440, 'height': 900}. | PASS | [REPLAY-QA-002-a1-opened](evidence/REPLAY-QA-002-a1-opened.json) |
| 2 | Click the Français control #language-switch. | The control reaches /fr/about. | #language-switch href=/fr/; actual destination http://127.0.0.1:39175/fr/. | FAIL | [REPLAY-QA-002-a1-opened](evidence/REPLAY-QA-002-a1-opened.json), [REPLAY-QA-002-a1-destination](evidence/REPLAY-QA-002-a1-destination.json), [REPLAY-QA-002-a1-destination-viewport](evidence/REPLAY-QA-002-a1-destination-viewport.png) |
| 3 | Read the destination URL, html[lang] and #page-heading. | The destination is /fr/about with html[lang]=fr and heading À propos d’Atlas Studio. | Final URL http://127.0.0.1:39175/fr/; HTTP 200; html[lang]=fr; heading Bienvenue chez Atlas Studio. | FAIL | [REPLAY-QA-002-a1-destination](evidence/REPLAY-QA-002-a1-destination.json), [REPLAY-QA-002-a1-destination-viewport](evidence/REPLAY-QA-002-a1-destination-viewport.png) |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "#language-switch href=/fr/; actual destination http://127.0.0.1:39175/fr/. Final URL http://127.0.0.1:39175/fr/; HTTP 200; html[lang]=fr; heading Bienvenue chez Atlas Studio.", "evidence_ids": ["REPLAY-QA-002-a1-opened", "REPLAY-QA-002-a1-destination", "REPLAY-QA-002-a1-destination-viewport", "REPLAY-QA-002-a1-network", "REPLAY-QA-002-a1-console"]}]

**Limitations**

- The case language records the requested starting language; evidence records the actual final document language fr.

**Uncertainties**

None

### REPLAY-QA-003 — Independent replay: French legacy redirect switches the visitor to English

- URL: http://127.0.0.1:39175/en/about
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T12:10:31.884608Z → 2026-10-08T12:10:32.264545Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No network-country requirement was specified for this loopback replay."}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 1440 x 900 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open http://127.0.0.1:39175/fr/legacy at 1440 × 900. | The supplied French legacy URL initiates navigation. | Requested http://127.0.0.1:39175/fr/legacy; final document HTTP 200. | PASS | [REPLAY-QA-003-a1-opened](evidence/REPLAY-QA-003-a1-opened.json) |
| 2 | Capture the redirect status and Location. | HTTP 302 with Location /fr/about. | Legacy response HTTP 302; Location /en/about. | FAIL | [REPLAY-QA-003-a1-opened](evidence/REPLAY-QA-003-a1-opened.json), [REPLAY-QA-003-a1-network](evidence/REPLAY-QA-003-a1-network.json) |
| 3 | Inspect the final URL, document language and heading. | Final /fr/about returns HTTP 200, html[lang]=fr and heading À propos d’Atlas Studio. | Final URL http://127.0.0.1:39175/en/about; HTTP 200; html[lang]=en; heading About Atlas Studio. | FAIL | [REPLAY-QA-003-a1-opened](evidence/REPLAY-QA-003-a1-opened.json), [REPLAY-QA-003-a1-final-viewport](evidence/REPLAY-QA-003-a1-final-viewport.png), [REPLAY-QA-003-a1-network](evidence/REPLAY-QA-003-a1-network.json) |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "Legacy response HTTP 302; Location /en/about. Final URL http://127.0.0.1:39175/en/about; HTTP 200; html[lang]=en; heading About Atlas Studio.", "evidence_ids": ["REPLAY-QA-003-a1-opened", "REPLAY-QA-003-a1-final-viewport", "REPLAY-QA-003-a1-network", "REPLAY-QA-003-a1-console"]}]

**Limitations**

- The case language records the requested starting language; evidence records the actual final document language en.

**Uncertainties**

None

### REPLAY-QA-004 — Independent replay: French form validation errors are displayed in English

- URL: http://127.0.0.1:39175/fr/contact
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T12:10:32.265176Z → 2026-10-08T12:10:32.689701Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No network-country requirement was specified for this loopback replay."}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 1440 x 900 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open http://127.0.0.1:39175/fr/contact at 1440 × 900. | The specified page loads in the requested language and viewport. | HTTP 200; actual URL http://127.0.0.1:39175/fr/contact; html[lang]=fr; viewport {'width': 1440, 'height': 900}. | PASS | [REPLAY-QA-004-a1-opened](evidence/REPLAY-QA-004-a1-opened.json) |
| 2 | Leave #contact-name and #contact-email empty. | Name and email remain empty. | contact-name value=''; contact-email value=''. | PASS | [REPLAY-QA-004-a1-opened](evidence/REPLAY-QA-004-a1-opened.json) |
| 3 | Click #contact-submit once. | Empty values are rejected, both fields are invalid, and confirmation remains hidden. | contact-name aria-invalid=true; contact-email aria-invalid=true; confirmation candidates=[{'id': 'confirmation', 'visible': False}]. | PASS | [REPLAY-QA-004-a1-validation](evidence/REPLAY-QA-004-a1-validation.json) |
| 4 | Read #name-error and #email-error. | Visible messages are Saisissez votre nom. and Saisissez une adresse e-mail valide. | #name-error='Enter your name.'; visible=True; #email-error='Enter a valid email address.'; visible=True. | FAIL | [REPLAY-QA-004-a1-validation](evidence/REPLAY-QA-004-a1-validation.json), [REPLAY-QA-004-a1-validation-viewport](evidence/REPLAY-QA-004-a1-validation-viewport.png) |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "contact-name aria-invalid=true; contact-email aria-invalid=true; confirmation candidates=[{'id': 'confirmation', 'visible': False}]. #name-error='Enter your name.'; visible=True; #email-error='Enter a valid email address.'; visible=True.", "evidence_ids": ["REPLAY-QA-004-a1-opened", "REPLAY-QA-004-a1-validation", "REPLAY-QA-004-a1-validation-viewport", "REPLAY-QA-004-a1-network", "REPLAY-QA-004-a1-console"]}]

**Limitations**

None

**Uncertainties**

None

### REPLAY-QA-005 — Independent replay: English contact form skips the required email field during keyboard entry

- URL: http://127.0.0.1:39175/en/contact
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T12:10:32.690080Z → 2026-10-08T12:10:33.079232Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No network-country requirement was specified for this loopback replay."}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 1440 x 900 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open http://127.0.0.1:39175/en/contact at 1440 × 900. | The specified page loads in the requested language and viewport. | HTTP 200; actual URL http://127.0.0.1:39175/en/contact; html[lang]=en; viewport {'width': 1440, 'height': 900}. | PASS | [REPLAY-QA-005-a1-opened](evidence/REPLAY-QA-005-a1-opened.json) |
| 2 | Focus #contact-name and type Alex Test using keyboard input. | #contact-name is focused and contains Alex Test. | Active element contact-name; name value='Alex Test'. | PASS | [REPLAY-QA-005-a1-name-keyboard](evidence/REPLAY-QA-005-a1-name-keyboard.json) |
| 3 | Press Tab exactly once. | Exactly one Tab moves focus to #contact-email. | Active element after one Tab is #contact-submit. | FAIL | [REPLAY-QA-005-a1-after-one-tab](evidence/REPLAY-QA-005-a1-after-one-tab.json), [REPLAY-QA-005-a1-focus-viewport](evidence/REPLAY-QA-005-a1-focus-viewport.png) |
| 4 | Inspect document.activeElement.id and the visible focus outline. Do not click or fill the skipped email field. | The email field has visible keyboard focus; inspect without clicking or filling the skipped field. | Active element #contact-submit; outline={'style': 'solid', 'width': '3px', 'color': 'rgb(195, 79, 0)', 'offset': '3px'}; email value=''; email tabIndex=-1. | FAIL | [REPLAY-QA-005-a1-after-one-tab](evidence/REPLAY-QA-005-a1-after-one-tab.json), [REPLAY-QA-005-a1-focus-viewport](evidence/REPLAY-QA-005-a1-focus-viewport.png) |
| 5 | Continue the expected keyboard completion only after the email focus transition succeeds. | Type alex@example.test, Tab to #contact-submit, press Enter, and observe Thank you, Alex Test. Your local request is confirmed. | Not run because the first Tab did not reach the email field. No click or direct fill was used to bypass the failed transition. | NOT_RUN | [REPLAY-QA-005-a1-after-one-tab](evidence/REPLAY-QA-005-a1-after-one-tab.json) |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "Active element after one Tab is #contact-submit. Active element #contact-submit; outline={'style': 'solid', 'width': '3px', 'color': 'rgb(195, 79, 0)', 'offset': '3px'}; email value=''; email tabIndex=-1. Not run because the first Tab did not reach the email field. No click or direct fill was used to bypass the failed transition.", "evidence_ids": ["REPLAY-QA-005-a1-opened", "REPLAY-QA-005-a1-name-keyboard", "REPLAY-QA-005-a1-after-one-tab", "REPLAY-QA-005-a1-focus-viewport", "REPLAY-QA-005-a1-network", "REPLAY-QA-005-a1-console"]}]

**Limitations**

- Email entry, submission and confirmation were not executed after the failed required focus transition.

**Uncertainties**

None

### REPLAY-QA-006 — Independent replay: French mobile offer overflows horizontally and clips its description

- URL: http://127.0.0.1:39175/fr/contact
- **Browser:** Chromium 151.0.7922.34
- **Execution period:** 2026-10-08T12:10:33.079878Z → 2026-10-08T12:10:33.675861Z
- **Geographic verification:** {"requested": null, "verified": null, "status": "NOT_APPLICABLE", "same_network_context": false, "evidence_ids": [], "note": "No network-country requirement was specified for this loopback replay."}

**Preconditions**

- Fresh isolated browser context; Chromium 151.0.7922.34; locale en-GB; time zone UTC.
- Viewport 390 x 844 CSS pixels.
- Synthetic local baseline on port 39175; no login.
- The sole business input is tickets-reviewed.json; no application source or prior case evidence was read.

| # | Action | Expected | Observed | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Open http://127.0.0.1:39175/fr/offer with a 390 × 844 Chromium viewport. | The specified page loads in the requested language and viewport. | HTTP 200; actual URL http://127.0.0.1:39175/fr/offer; html[lang]=fr; viewport {'width': 390, 'height': 844}. | PASS | [REPLAY-QA-006-a1-opened](evidence/REPLAY-QA-006-a1-opened.json) |
| 2 | Compare document.documentElement.scrollWidth with window.innerWidth. | scrollWidth <= innerWidth + 1. | scrollWidth=556; innerWidth=390; overflow=166 CSS pixels. | FAIL | [REPLAY-QA-006-a1-opened](evidence/REPLAY-QA-006-a1-opened.json), [REPLAY-QA-006-a1-offer-viewport](evidence/REPLAY-QA-006-a1-offer-viewport.png) |
| 3 | Inspect the right edge of the offer card and description before interacting. | The offer card and full description fit in the viewport without horizontal scrolling. | Visible content boxes extending beyond the right viewport edge: [{'id': '', 'text': 'Offre Découverte\n19,90 € / mois\n8 octobre 2026\nUn point de départ clair pour votre prochain site web.\nContactez-nous', 'right': 556}, {'id': 'offer-title', 'text': 'Offre Découverte', 'right': 539}, {'id': 'offer-price', 'text': '19,90 € / mois', 'right': 539}, {'id': 'offer-date', 'text': '8 octobre 2026', 'right': 539}, {'id': '', 'text': 'Un point de départ clair pour votre prochain site web.', 'right': 539}]. | FAIL | [REPLAY-QA-006-a1-opened](evidence/REPLAY-QA-006-a1-opened.json), [REPLAY-QA-006-a1-offer-viewport](evidence/REPLAY-QA-006-a1-offer-viewport.png) |
| 4 | Click #offer-cta and record whether it remains visible and reaches French Contact. | The CTA remains visible and reaches /fr/contact in French. | CTA initially visible=True; within horizontal viewport=True; final URL http://127.0.0.1:39175/fr/contact; html[lang]=fr; heading Contacter Atlas Studio. | PASS | [REPLAY-QA-006-a1-opened](evidence/REPLAY-QA-006-a1-opened.json), [REPLAY-QA-006-a1-cta-destination](evidence/REPLAY-QA-006-a1-cta-destination.json), [REPLAY-QA-006-a1-contact-viewport](evidence/REPLAY-QA-006-a1-contact-viewport.png) |

**Attempts:** [{"number": 1, "status": "FAIL", "observed": "scrollWidth=556; innerWidth=390; overflow=166 CSS pixels. Visible content boxes extending beyond the right viewport edge: [{'id': '', 'text': 'Offre Découverte\\n19,90 € / mois\\n8 octobre 2026\\nUn point de départ clair pour votre prochain site web.\\nContactez-nous', 'right': 556}, {'id': 'offer-title', 'text': 'Offre Découverte', 'right': 539}, {'id': 'offer-price', 'text': '19,90 € / mois', 'right': 539}, {'id': 'offer-date', 'text': '8 octobre 2026', 'right': 539}, {'id': '', 'text': 'Un point de départ clair pour votre prochain site web.', 'right': 539}]. CTA initially visible=True; within horizontal viewport=True; final URL http://127.0.0.1:39175/fr/contact; html[lang]=fr; heading Contacter Atlas Studio.", "evidence_ids": ["REPLAY-QA-006-a1-opened", "REPLAY-QA-006-a1-offer-viewport", "REPLAY-QA-006-a1-cta-destination", "REPLAY-QA-006-a1-contact-viewport", "REPLAY-QA-006-a1-network", "REPLAY-QA-006-a1-console"]}]

**Limitations**

- Mobile profile is a 390 by 844 desktop Chromium viewport, not a physical device; touch/mobile user-agent settings were not specified by the ticket.

**Uncertainties**

None

## Limitations

- Ticket-only replay of six specified defects; application source, product oracle and prior case evidence were not read.
- One fresh isolated browser context and one attempt per ticket; original reproduction counts were not reused.
- Only local port 39175 was visited. Corrected port 39176 and acceptance witness journeys were not tested.
- All profiles and evidence are retained. Mobile means the stated viewport, without a physical-device claim.
- Raw screenshots require visual reviewer inspection in addition to the DOM measurements.

## Recommended next work

Triage demonstrated defects, resolve product questions, and rerun fixed or blocked critical cases in a new campaign. This report does not certify other devices, countries, security, or legal compliance.
