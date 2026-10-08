# Execution and tool capability

## Select a real execution path

1. Discover actual MCP/browser tools, their schemas, and their authorization boundaries.
2. Prefer connected Firecrawl or ZenRows MCP for research, URL discovery, and extraction when available.
3. For journeys, choose a provider with real interaction, an authorized browser tool, or permitted local Playwright. Probe the chosen capability with a harmless scoped navigation.
4. Record supported and missing capabilities. Do not infer support for screenshots, keyboard input, network, console, traces, or geographic verification from the provider name.
5. Use the input budget and explicit case matrix. Stop or mark remaining cases when the budget is reached.

The package's Python helper validates structured data and renders exports. It is not an MCP client and does not execute browsing. The checked-in test driver is a separate synthetic demonstration harness. The agent must perform each campaign's actual interactions using the available authorized tools.

Public web research must follow the host's tool policy. Local Playwright is appropriate for the demonstration because that access is explicitly authorized. Its availability is not permission to bypass an MCP-only research policy or to browse a production site outside the requested scope.

## Capability ledger

Record whether the selected session actually supports:

- Extraction of rendered text/DOM and selected attributes.
- Navigation, clicks, typing, keyboard keys, and focus inspection.
- Screenshots and, separately, video/trace capture.
- Network responses, redirect information, failed requests, and JavaScript console/errors.
- Browser/version, viewport, locale, time zone, touch emulation, and physical-device access.
- Network exit-country verification tied to the site request's context.

A false capability means the corresponding absence cannot be asserted. For example, when console collection is unavailable, report that gap rather than “no JavaScript errors.”

## Authorized interaction

Build a scope guard from exact allowed origins and allowed/excluded paths before navigating. Check destinations, popups, and resource behavior as tools permit. Never submit secrets to a newly encountered domain. Respect access controls; an authentication wall is not permission to bypass it.

A browser route callback is not a complete network firewall. Redirect chains, service workers, WebSockets, and provider-side requests can have different interception semantics. If strict network containment cannot be established for the requested environment, disclose that limitation and use an adequately controlled environment. The demonstration is first-party loopback with no external resources.

Keep authentication references outside the public configuration. Resolve only the explicitly authorized mechanism in the current session. Never export storage state, cookies, authorization headers, or credentials as evidence.

## Geographic verification

Record requested country, actually verified country or null, time, evidence ID, and whether the proof pertains to the same network session/context as the website request. A provider parameter is an instruction, not the measurement.

With rotating proxies, a separate IP lookup can use another route. Without a reliable link to the site request, keep same_network_context false and geography BLOCKED/NOT_RUN. Browser coordinates, Accept-Language, time zone, localized content, and URL language are independent signals.

## Failure and retry policy

Use a small explicit retry budget, normally one retry for a plausible transient execution error. Record each attempt. Do not loop until the site appears to pass, retry purchases/submissions blindly, or turn retries into extra unannounced coverage.

When authentication, required capability, or product expectations are missing, preserve independent observations and mark dependent cases accurately. Keep tool incidents out of the website defect count unless separate evidence demonstrates a site problem.

Reference behavior was checked through official documentation: [Playwright networking](https://playwright.dev/python/docs/network) and [emulation](https://playwright.dev/python/docs/emulation). These explain capabilities; each campaign still needs an observed capability check.
