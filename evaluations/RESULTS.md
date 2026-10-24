# Evaluation record

## Local trials — 22 October 2026

Three independent agent trials used the original skill with only the relevant task/fixture:

- A bilingual sales prototype implemented search/filter/sort, pagination, record detail/edit/create, linked activities, company summaries and opportunity stage changes. Browser review found modal-focus and completed-task due-label issues, followed by storage validation/recovery and rerender-focus gaps. Targeted repair passes corrected these. The maintainer then requested custom dropdowns; keyboard, Escape, outside dismissal, saved form choices, stage reload and 320/390px modal popups were exercised.
- A recruiting implementation plan preserved an existing Vue stack and specified per-role applications, concurrent edit recovery, interview scheduling and legacy-data boundaries. No real Vue app/backend was supplied, so this establishes planning output, not runtime integration correctness.
- A report-only audit found the six known defect areas in the synthetic legacy fixture: failed-save draft loss/false success, query/count/page disagreement, accessible naming/focus, width/overflow, unsafe HTML insertion and memory-only persistence. Six Node logic probes reproduced the defects. These probes are not browser tests.

The public synthetic example and captures are in examples/sales/. Its 33 storage checks exercise the exact embedded engine with a fixed clock and an in-memory adapter. They do not test browser quota behavior, rendered accessibility or backend authorization. The palette suite checks 22 token pairs, not complete screens.

## Maintainer-provided existing-project feedback — 24 October 2026

The maintainer supplied feedback from a real existing-project trial. The report describes an audit followed by two staged updates to a filter-heavy results page, with preserved behavior and browser checks. It credits concrete focus/filter/label requirements and the observed-versus-inferred evidence distinction. It also reports a sibling-pop-out keyboard bug discovered during testing.

This is reported field evidence, not an independently replayed production audit. No application source, customer data, private screenshots, account details, local filesystem logs or full private transcript is distributed. No measured task-time gain or universally applicable quality score is claimed.

Release changes based on that feedback include selective search-results and pop-out references, balanced Claude Code/Codex installation examples, fresh-session guidance, clearer scorer status/readable output, canonical craft-crm release naming and an MIT license selected by the maintainer.

## Verification and limits

Run Python tests, the bundle validator, the six fixture probes and the 33 example storage checks using RELEASE.md. Public-release installation is smoke-tested for project-scoped copies to both Codex and Claude Code directories; running a live Claude session is a separate unverified step. Windows/physical phone/screen-reader and integrated-backend behavior remain unverified. No matched control experiment against an agent without the skill was performed. The historical 52-resource catalog retains its original inspection limitations.
