# Synthetic multilingual product contract

This public business contract defines the expected behavior of a fictitious Atlas Studio website. It is the auditor's input. Read this contract and the installed skill; do not inspect the demo implementation or the separate oracle while producing a blind audit.

## Environment and authorization

- Baseline base URL: `http://127.0.0.1:39175`.
- Corrected base URL for later retesting: `http://127.0.0.1:39176`.
- Allowed network origins are these two loopback origins only. No external services, accounts, cookies, or payments are involved.
- Authorization covers reading pages, navigation, searches, typing the fictional data below, and submitting the local contact form. The form updates the page only; it sends no message and persists no user data.
- Site languages are `en` and `fr`. Output language is independently configurable and defaults to `en`.
- No country verification is requested. Do not infer a network country from language or loopback access.
- Desktop profile: Chromium, viewport 1440 × 900 CSS pixels. Mobile profile: the same Chromium engine, viewport 390 × 844 CSS pixels. This is a narrow viewport, not a physical-phone test.
- Each case starts in a fresh browser context. Record the actual browser version and UTC execution time.
- Budget: twenty baseline cases, at most two attempts per case, 180 page navigations, 600 first-party requests, and 20 minutes per campaign. A retest is a separate campaign.
- Test data: name `Alex Test`; email `alex@example.test`; successful search `atlas`; empty search `zzzz-no-match`.
- `Atlas Studio`, `Atlas`, and the fictional test name/email are intentional retained terms, not translation defects.

Use identifiers `J01-en` through `J10-en` and `J01-fr` through `J10-fr`. Run the ten journey definitions once per language: exactly twenty planned journey–language pairs. Assign one profile per journey as stated below; do not silently multiply devices or countries.

## Routes and shared expectations

The home routes are `/en/` and `/fr/`. Internal routes are `/<language>/about`, `/<language>/search`, `/<language>/contact`, and `/<language>/offer`. `/<language>/legacy` is a redirect entrypoint and must preserve the requested language while redirecting to that language's `/about` page.

All ordinary document routes return HTTP 200. `/<language>/legacy` returns HTTP 302 and then the target document returns HTTP 200. `/auth-required` deliberately returns HTTP 401 and requires unavailable credentials; it is used only by a separate negative-capability test. Its authentication block is not a defect in the twenty-case campaign.

Each ordinary page declares its actual language on `html[lang]`; includes a same-origin canonical link for the current route, without the search query; and includes `link[rel="alternate"][hreflang="en"]` and `link[rel="alternate"][hreflang="fr"]` pointing to the corresponding route in each language. The page title and heading identify the current page and language. No external resources are expected.

Shared selectors:

| Purpose | Selector |
| --- | --- |
| Page heading | `#page-heading` |
| Desktop About navigation | `#main-about` |
| Language switch | `#language-switch` |
| Mobile menu toggle | `#menu-toggle` |
| Mobile menu panel | `#mobile-menu` |
| About link inside mobile menu | `#mobile-about` |
| Main content | `#main-content` |

## J01 — Open the requested home page

Profile: **desktop**.

1. Open `/<language>/`.
2. Verify HTTP 200, the requested URL path, `html[lang]`, and `#page-heading`.
3. Check the canonical and both language-alternate links against the shared expectations.

Expected headings: English `Welcome to Atlas Studio`; French `Bienvenue chez Atlas Studio`.

## J02 — Follow primary navigation to an internal page

Profile: **desktop**.

1. Open `/<language>/`.
2. Click `#main-about`.
3. Verify the destination is `/<language>/about`, HTTP 200, the same document language, and the localized About heading.

Expected headings: English `About Atlas Studio`; French `À propos d’Atlas Studio`.

## J03 — Switch language from an internal page

Profile: **desktop**.

1. Open `/<language>/about` directly.
2. Click `#language-switch`.
3. Verify the destination is the other language's `/about` route, retaining the internal page rather than returning home.
4. Verify the destination document language and its localized About heading.

Starting `en` must reach `/fr/about`; starting `fr` must reach `/en/about`.

## J04 — Follow a redirect while preserving language

Profile: **desktop**.

1. Open `/<language>/legacy` and capture its redirect response if the browser exposes it.
2. Verify the final route is `/<language>/about`, the language is unchanged, and the localized About heading is present.
3. Record the redirect's HTTP status and Location when available; lack of network instrumentation must be reported separately.

## J05 — Search with a matching result

Profile: **desktop**.

1. Open `/<language>/search`.
2. Fill `#search-query` with `atlas` and submit using `#search-submit`.
3. Verify the query remains visible, `#search-results` contains exactly one `.search-result`, and `#empty-state` is absent.
4. Click `#result-about` and verify `/<language>/about` and its localized heading.

The result title is the localized About heading. Search must preserve the starting language.

## J06 — Search with no matching result

Profile: **desktop**.

1. Open `/<language>/search`.
2. Fill `#search-query` with `zzzz-no-match` and submit using `#search-submit`.
3. Verify no `.search-result` appears, the query remains visible, and `#empty-state` is visible.

Expected empty text: English `No results found.`; French `Aucun résultat.`. Do not report an empty result as a defect when this state is correctly displayed.

## J07 — Submit an invalid local form

Profile: **desktop**.

1. Open `/<language>/contact` with both fields empty.
2. Click `#contact-submit`.
3. Verify `#name-error` and `#email-error` are visible, each field has `aria-invalid="true"`, and `#confirmation` is hidden.
4. Verify the errors are in the page language. The exact approved strings are below.

| Error | English | French |
| --- | --- | --- |
| Missing name | `Enter your name.` | `Saisissez votre nom.` |
| Missing or invalid email | `Enter a valid email address.` | `Saisissez une adresse e-mail valide.` |

## J08 — Complete the local form using the keyboard

Profile: **desktop**.

1. Open `/<language>/contact`.
2. Focus `#contact-name`, type `Alex Test`, and press Tab once.
3. Verify focus is on `#contact-email` and that a visible focus outline is present.
4. Type `alex@example.test`, press Tab once, verify focus is on `#contact-submit`, and press Enter.
5. Verify `#confirmation` is visible, no validation errors remain visible, and its localized text matches below.

The expected forward sequence is `contact-name → contact-email → contact-submit`. Both fields have visible associated labels. A skipped required field is a failed keyboard step; do not silently click around it and claim the keyboard journey passed. Unexecuted later steps retain their own status.

Expected confirmation: English `Thank you, Alex Test. Your local request is confirmed.`; French `Merci, Alex Test. Votre demande locale est confirmée.`.

## J09 — Open, use, and close the mobile menu

Profile: **mobile**.

1. Open `/<language>/` at the mobile viewport. Verify `#menu-toggle` is visible and the menu starts hidden with `aria-expanded="false"`.
2. Click `#menu-toggle`; verify the panel is visible and `aria-expanded="true"`.
3. Click `#mobile-about`; verify `/<language>/about`, its localized heading, and the menu is closed after navigation.
4. Reopen the menu; press Escape; verify the panel is hidden, `aria-expanded="false"`, and focus returns to `#menu-toggle`.

Verify that the toggle and About link can actually be clicked in the viewport; a static page extraction is insufficient for this journey.

## J10 — Read a localized offer on mobile

Profile: **mobile**.

1. Open `/<language>/offer` at the mobile viewport.
2. Verify `#offer-title`, `#offer-price`, and `#offer-date` against the table.
3. Verify `document.documentElement.scrollWidth <= window.innerWidth + 1`, with no horizontal page overflow.
4. Verify `#offer-cta` is visible within the viewport, can be clicked, and reaches `/<language>/contact` without changing language.

| Field | English | French |
| --- | --- | --- |
| `#offer-title` | `Starter plan` | `Offre Découverte` |
| `#offer-price` | `€19.90 / month` | `19,90 € / mois` |
| `#offer-date` | `October 8, 2026` | `8 octobre 2026` |
| `#offer-cta` | `Contact us` | `Contactez-nous` |

## Evidence and decision boundaries

Capture actual screenshots or text excerpts at observed failures, and preserve requested versus actual URLs, relevant attributes, and step outcomes. A screenshot alone does not prove the entire journey. Retain original French or English evidence text even when report prose uses another language.

Record console/network observations only if collected. Absence of collection does not mean absence of errors. Distinguish inaccessible tools from website defects. A product expectation missing from this contract is an explicit assumption or product question, not an invented release requirement.

Use `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, and `NOT_APPLICABLE`. A partially executed case is not a pass. Report coverage as a numerator and denominator; the baseline denominator is twenty planned cases. Do not make a general production-readiness claim about this synthetic demo.
