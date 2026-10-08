# Website Release QA Report

Campaign: {{campaign_id}}
Environment: {{environment}}
Started / finished: {{timestamps}}
Report language: {{output_language}}

## Scope and conditions

{{allowed_scope_languages_profiles_browser_versions_and_explicit_exclusions}}

## Capability and coverage

{{observed_capabilities_and_missing_capabilities}}

| State | Case count |
| --- | ---: |
| PASS | {{pass_count}} |
| FAIL | {{fail_count}} |
| BLOCKED | {{blocked_count}} |
| NOT_RUN | {{not_run_count}} |
| NOT_APPLICABLE | {{not_applicable_count}} |

Coverage: {{named_numerator}} / {{named_denominator}}.
Critical journeys not covered: {{critical_gaps}}.
Scoped verdict: {{verdict_and_limitations}}.

## Priority findings

{{observed_impact_severity_and_ticket_links}}

## Case matrix

{{case_id_journey_language_profile_country_status_and_evidence}}

## Detailed tickets

{{tickets_rendered_from_results_json}}

## Product questions and tooling incidents

{{unresolved_expectations_inconsistencies_and_tool_failures}}

## Limits and next actions

{{retest_plan_missing_coverage_and_decisions}}

This is an editorial template. Generate counts and case/ticket tables from results.json; do not maintain a second manually counted report.
