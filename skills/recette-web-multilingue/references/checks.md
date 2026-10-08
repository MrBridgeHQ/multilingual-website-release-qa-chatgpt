# Choose observable checks

Use explicit acceptance criteria and the features actually present. Keep the matrix small enough to finish within the agreed budget. Record static observations separately from interacted journeys.

| Area | Useful observation | Important boundary |
| --- | --- | --- |
| Navigation | Click primary links and menus; inspect actual destination, redirect chain, and load state | A valid href alone does not demonstrate navigation |
| Search/filter | Enter a known term, submit, inspect matching results; exercise a known empty result | Do not invent ranking or business filtering rules |
| Forms | Exercise invalid input, field errors, keyboard entry, submit, and local confirmation | Sending a real message or creating a record requires explicit authorization |
| Language switching | Switch from an internal page; verify equivalent page and intended state | Home-page switching alone is insufficient |
| Redirect language | Follow a known redirect and check actual final language and equivalent destination | A localized starting URL proves nothing about the destination |
| Localization | Check agreed copy, untranslated fragments, date/number/currency formatting, and content parity | Keep approved brand names, quotes, and intentional loanwords |
| Layout | Measure horizontal overflow; inspect clipped content, obstructed controls, overlays, and dialogs | Geometry suggests a defect; pair it with visible impact and evidence |
| Keyboard/accessibility | Tab order, focused element, visible focus, form labels, dialog name/closing behavior | DOM labels alone do not establish full accessibility |
| Technical | Console errors, failed requests, response status, missing resources | Distinguish a request failure from an HTTP error response; collect only if supported |
| Multilingual structure | html lang, canonical URL, alternate hreflang values and targets | A functional observation, not a complete SEO audit |

For a partially executed case, retain successful steps and mark later unexecuted steps NOT_RUN. Choose the overall result from the actual obstacle or demonstrated failure. Use NOT_APPLICABLE only with a concrete reason, not to hide missing capability.

For a keyboard case, focus the initial element through keyboard navigation where practical, then use actual keys and inspect the active element after transitions. Filling every field directly through an API does not exercise keyboard order. Record visible focus separately from the identity of the focused element.

For mobile emulation, record viewport, touch/isMobile settings if used, browser, operating context, and limitations. At least one desktop and one mobile profile does not cover every device.

If content differs by country, create geography-specific checks with explicit network proof. Do not infer country from site language, URL prefix, browser locale, coordinates, or the provider's requested-country parameter.

Optional performance observations must include tool/version, network/CPU conditions, cache state, profile, run count, and distribution where measured. Do not convert one local run into a production performance guarantee.
