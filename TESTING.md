# Test craft-crm on an existing project

Release: **0.1.0**. Use a test branch or disposable checkout so you can review changes.

## Install and discover

From your project root, choose one:

```sh
npx skills add Audran-wol/craft-crm --skill craft-crm -a claude-code
npx skills add Audran-wol/craft-crm --skill craft-crm -a codex
```

Add `--copy` to copy instead of linking. No global installation is needed. For an extracted ZIP replace the repository source with the extracted `craft-crm` folder path. Start a **new session in that project** after installation; this matters for skill discovery, including Claude Code.

Use `/craft-crm` in Claude Code or `$craft-crm` in Codex. If discovery is unavailable, point the agent explicitly to the installed `SKILL.md`. Keep its references, assets, scripts, metadata and license together.

## A focused implementation trial

Supply a route/screen name if the app has several dashboards. This asks for implementation, not a report-only audit:

```text
Use craft-crm to polish this project's existing CRM dashboard.
Inspect the repository and current app, then implement focused improvements
in hierarchy, filters, custom dropdowns and responsive layout.
Keep the existing framework, routes, data contracts, authentication and
working business logic. Reuse existing components and tokens.
Verify affected filters, metric/drill-down scope, record navigation and editing.
Check open pop-outs, keyboard navigation, Escape and modal placement.
Capture the same screen/data before and after at desktop and phone widths.
Report changed files, executed checks, and anything unverified.
```

Prefix with `/craft-crm` or use `$craft-crm` as appropriate. For a search-results page use that screen instead; do not invent a dashboard just for the test.

## Feedback

Include release version, agent/model, project stack, route, before/after screenshots and the exact sequence that worked or failed. Assess visual hierarchy/density, query/count correctness, save/error behavior, preserved features, keyboard focus and narrow-screen/open-popup reachability. A personal 1–10 rating is useful with concrete reasons.

Do not publish private customer data, credentials, internal URLs or application screenshots without the relevant permission. A sanitized reproduction is usually more useful than a complete private transcript.
