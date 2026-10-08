# Independent ticket replay assessment

Business input: tickets-reviewed.json only. No application source, product oracle or earlier case evidence was inspected.

Frozen at: 2026-10-08T12:10:33.679391Z

| Ticket | Case | Assessment | Actual replay frequency |
| --- | --- | --- | ---: |
| QA-001 | REPLAY-QA-001 | reproduced | 1/1 |
| QA-002 | REPLAY-QA-002 | reproduced | 1/1 |
| QA-003 | REPLAY-QA-003 | reproduced | 1/1 |
| QA-004 | REPLAY-QA-004 | reproduced | 1/1 |
| QA-005 | REPLAY-QA-005 | reproduced | 1/1 |
| QA-006 | REPLAY-QA-006 | reproduced | 1/1 |

## QA-001

Observed facts:
- HTTP 200; actual URL http://127.0.0.1:39175/fr/; html[lang]=fr; viewport {'width': 1440, 'height': 900}.
- #main-about href=/fr/search; actual destination http://127.0.0.1:39175/fr/search.
- Final URL http://127.0.0.1:39175/fr/search; HTTP 200; html[lang]=fr; heading Rechercher chez Atlas Studio.

Missing details:
- None needed to execute the numbered reproduction.

Ambiguities:
- No ambiguity prevented the numbered reproduction.

Limits:
- Acceptance-criterion witness journeys outside the numbered reproduction were not executed.
- Original reproduction counts and original evidence references were not used as replay proof.

Artifacts:
- [REPLAY-QA-001-a1-opened.json](report/evidence/REPLAY-QA-001-a1-opened.json)
- [REPLAY-QA-001-a1-destination.json](report/evidence/REPLAY-QA-001-a1-destination.json)
- [REPLAY-QA-001-a1-destination-viewport.png](report/evidence/REPLAY-QA-001-a1-destination-viewport.png)
- [REPLAY-QA-001-a1-network.json](report/evidence/REPLAY-QA-001-a1-network.json)
- [REPLAY-QA-001-a1-console.json](report/evidence/REPLAY-QA-001-a1-console.json)

## QA-002

Observed facts:
- HTTP 200; actual URL http://127.0.0.1:39175/en/about; html[lang]=en; viewport {'width': 1440, 'height': 900}.
- #language-switch href=/fr/; actual destination http://127.0.0.1:39175/fr/.
- Final URL http://127.0.0.1:39175/fr/; HTTP 200; html[lang]=fr; heading Bienvenue chez Atlas Studio.

Missing details:
- None needed to execute the numbered reproduction.

Ambiguities:
- No ambiguity prevented the numbered reproduction.

Limits:
- Acceptance-criterion witness journeys outside the numbered reproduction were not executed.
- Original reproduction counts and original evidence references were not used as replay proof.
- The case language records the requested starting language; evidence records the actual final document language fr.

Artifacts:
- [REPLAY-QA-002-a1-opened.json](report/evidence/REPLAY-QA-002-a1-opened.json)
- [REPLAY-QA-002-a1-destination.json](report/evidence/REPLAY-QA-002-a1-destination.json)
- [REPLAY-QA-002-a1-destination-viewport.png](report/evidence/REPLAY-QA-002-a1-destination-viewport.png)
- [REPLAY-QA-002-a1-network.json](report/evidence/REPLAY-QA-002-a1-network.json)
- [REPLAY-QA-002-a1-console.json](report/evidence/REPLAY-QA-002-a1-console.json)

## QA-003

Observed facts:
- Requested http://127.0.0.1:39175/fr/legacy; final document HTTP 200.
- Legacy response HTTP 302; Location /en/about.
- Final URL http://127.0.0.1:39175/en/about; HTTP 200; html[lang]=en; heading About Atlas Studio.

Missing details:
- None needed to execute the numbered reproduction.

Ambiguities:
- No ambiguity prevented the numbered reproduction.

Limits:
- Acceptance-criterion witness journeys outside the numbered reproduction were not executed.
- Original reproduction counts and original evidence references were not used as replay proof.
- The case language records the requested starting language; evidence records the actual final document language en.

Artifacts:
- [REPLAY-QA-003-a1-opened.json](report/evidence/REPLAY-QA-003-a1-opened.json)
- [REPLAY-QA-003-a1-final-viewport.png](report/evidence/REPLAY-QA-003-a1-final-viewport.png)
- [REPLAY-QA-003-a1-network.json](report/evidence/REPLAY-QA-003-a1-network.json)
- [REPLAY-QA-003-a1-console.json](report/evidence/REPLAY-QA-003-a1-console.json)

## QA-004

Observed facts:
- HTTP 200; actual URL http://127.0.0.1:39175/fr/contact; html[lang]=fr; viewport {'width': 1440, 'height': 900}.
- contact-name value=''; contact-email value=''.
- contact-name aria-invalid=true; contact-email aria-invalid=true; confirmation candidates=[{'id': 'confirmation', 'visible': False}].
- #name-error='Enter your name.'; visible=True; #email-error='Enter a valid email address.'; visible=True.

Missing details:
- A confirmation-element selector is not stated; the replay inspected rendered status/confirmation candidates.

Ambiguities:
- No ambiguity prevented the numbered reproduction.

Limits:
- Acceptance-criterion witness journeys outside the numbered reproduction were not executed.
- Original reproduction counts and original evidence references were not used as replay proof.

Artifacts:
- [REPLAY-QA-004-a1-opened.json](report/evidence/REPLAY-QA-004-a1-opened.json)
- [REPLAY-QA-004-a1-validation.json](report/evidence/REPLAY-QA-004-a1-validation.json)
- [REPLAY-QA-004-a1-validation-viewport.png](report/evidence/REPLAY-QA-004-a1-validation-viewport.png)
- [REPLAY-QA-004-a1-network.json](report/evidence/REPLAY-QA-004-a1-network.json)
- [REPLAY-QA-004-a1-console.json](report/evidence/REPLAY-QA-004-a1-console.json)

## QA-005

Observed facts:
- HTTP 200; actual URL http://127.0.0.1:39175/en/contact; html[lang]=en; viewport {'width': 1440, 'height': 900}.
- Active element contact-name; name value='Alex Test'.
- Active element after one Tab is #contact-submit.
- Active element #contact-submit; outline={'style': 'solid', 'width': '3px', 'color': 'rgb(195, 79, 0)', 'offset': '3px'}; email value=''; email tabIndex=-1.
- Not run because the first Tab did not reach the email field. No click or direct fill was used to bypass the failed transition.

Missing details:
- None needed to execute the numbered reproduction.

Ambiguities:
- No ambiguity prevented the numbered reproduction.

Limits:
- Acceptance-criterion witness journeys outside the numbered reproduction were not executed.
- Original reproduction counts and original evidence references were not used as replay proof.
- Email entry, submission and confirmation were not executed after the failed required focus transition.

Artifacts:
- [REPLAY-QA-005-a1-opened.json](report/evidence/REPLAY-QA-005-a1-opened.json)
- [REPLAY-QA-005-a1-name-keyboard.json](report/evidence/REPLAY-QA-005-a1-name-keyboard.json)
- [REPLAY-QA-005-a1-after-one-tab.json](report/evidence/REPLAY-QA-005-a1-after-one-tab.json)
- [REPLAY-QA-005-a1-focus-viewport.png](report/evidence/REPLAY-QA-005-a1-focus-viewport.png)
- [REPLAY-QA-005-a1-network.json](report/evidence/REPLAY-QA-005-a1-network.json)
- [REPLAY-QA-005-a1-console.json](report/evidence/REPLAY-QA-005-a1-console.json)

## QA-006

Observed facts:
- HTTP 200; actual URL http://127.0.0.1:39175/fr/offer; html[lang]=fr; viewport {'width': 390, 'height': 844}.
- scrollWidth=556; innerWidth=390; overflow=166 CSS pixels.
- Visible content boxes extending beyond the right viewport edge: [{'id': '', 'text': 'Offre Découverte\n19,90 € / mois\n8 octobre 2026\nUn point de départ clair pour votre prochain site web.\nContactez-nous', 'right': 556}, {'id': 'offer-title', 'text': 'Offre Découverte', 'right': 539}, {'id': 'offer-price', 'text': '19,90 € / mois', 'right': 539}, {'id': 'offer-date', 'text': '8 octobre 2026', 'right': 539}, {'id': '', 'text': 'Un point de départ clair pour votre prochain site web.', 'right': 539}].
- CTA initially visible=True; within horizontal viewport=True; final URL http://127.0.0.1:39175/fr/contact; html[lang]=fr; heading Contacter Atlas Studio.

Missing details:
- Device scale factor, mobile user agent, touch capability and is_mobile setting are not specified.

Ambiguities:
- The requested dimensions can be reproduced, but 'mobile' does not identify a physical device or complete emulation profile.

Limits:
- Acceptance-criterion witness journeys outside the numbered reproduction were not executed.
- Original reproduction counts and original evidence references were not used as replay proof.
- Mobile profile is a 390 by 844 desktop Chromium viewport, not a physical device; touch/mobile user-agent settings were not specified by the ticket.

Artifacts:
- [REPLAY-QA-006-a1-opened.json](report/evidence/REPLAY-QA-006-a1-opened.json)
- [REPLAY-QA-006-a1-offer-viewport.png](report/evidence/REPLAY-QA-006-a1-offer-viewport.png)
- [REPLAY-QA-006-a1-cta-destination.json](report/evidence/REPLAY-QA-006-a1-cta-destination.json)
- [REPLAY-QA-006-a1-contact-viewport.png](report/evidence/REPLAY-QA-006-a1-contact-viewport.png)
- [REPLAY-QA-006-a1-network.json](report/evidence/REPLAY-QA-006-a1-network.json)
- [REPLAY-QA-006-a1-console.json](report/evidence/REPLAY-QA-006-a1-console.json)

## Visual evidence review

All seven registered screenshots were inspected by the independent replay reviewer. They show the Search, French home, and English About destinations; the English field errors on French Contact; the orange focus outline around the English submit control; and the clipped French offer description. The mobile title, price, date and CTA remain readable. The CTA destination screenshot shows French Contact.

The original source assessment was frozen before any additional business input. The screenshot review confirmed its observations. The public portable driver differs from the executed retained driver only in the ROOT assignment.
