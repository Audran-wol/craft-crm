# Worked briefs and invocation recipes

## One-prompt new build

Prompt:
“Use $craft-crm to build a CRM for a small B2B agency. We manage companies, contacts, opportunities and follow-ups. Use the existing React stack, a light gray canvas and white work surfaces. Choose the best direction and build with synthetic data; no questions unless blocked.”

Expected handling:
Choose A with an optional B view because comparison and follow-up are frequent. Build company list, detail, creation/editing and next activity before analytics. Include company, owner, stage, next action, and last contact; use readable neutral icons. Define whether data persists. Do not fill navigation with unrelated HR/payroll modules.

## Existing CRM revamp

Prompt:
“Use $craft-crm to revamp this CRM. Fix the crowded header, floating search, team dropdown, table alignment and double scrollbars. Keep business logic and routes.”

Expected handling:
Inspect existing shell and overflow/portal behavior; capture baseline; consolidate tokens/gutters; repair toolbar/menu/table. Verify route/query/selection/edit behavior survived. Do not rewrite the backend or migrate libraries for visual repair.

## Options before building

Prompt:
“Use $craft-crm for a real estate CRM. Show three directions using the same property, buyer and viewing data before implementation.”

Expected handling:
Show records-first, pipeline-first, and operations-first compositions with equivalent data and scale. Explain tradeoffs in one line each. Treat property and person as distinct objects. Avoid a generic sales dashboard whose only customization is a house icon.

## Recruiting CRM

Prompt:
“Use $craft-crm to build a recruiting CRM for candidates, employers, open roles and interviews. Start with a searchable candidate list and a role-specific application view.”

Expected handling:
Separate candidate identity from each application. Reuse common table, filter, record and form components. Show employer/role context for an application; stage belongs to that application, not globally to the person. Calendar/agenda views serve interview scheduling when required. Do not inherit invoice or sales revenue widgets.

## Membership CRM

Prompt:
“Use $craft-crm to revamp our community membership CRM for people, organizations, renewals and participation. Keep our existing branding.”

Expected handling:
Preserve the member/organization relationship model, shared household roles where supported, and renewal rules. Choose records plus a renewal/follow-up queue. Use the same responsive, icon, table and form standards as any other CRM. Keep communication preferences visible to authorized operators and preserve existing routes and behavior.

## Optional invoice operations

Prompt:
“Use $craft-crm to build an invoice workspace with overdue filters, customer details and reminder previews.”

Expected handling:
Apply A/C. Define currency and due-date semantics. Tie filtered count and sum to the list. Preview reminders; do not send unless authorized. Paid/partial/overdue states follow the chosen backend model.

## Dense expert tool

Prompt:
“Use $craft-crm to improve a 30-column enterprise CRM for keyboard-heavy account managers. Preserve information density.”

Expected handling:
Do not enlarge all rows or hide necessary columns to look minimal. Choose compact density, column controls, pinned identity if useful, keyboard flows and clear query context. Profile large-data behavior. Native table remains preferable unless composite-grid interaction is needed.

## Screenshot-only audit

Prompt:
“Use $craft-crm to audit these screenshots and give the team fixes.”

Expected handling:
Return observed layout/hierarchy/readability issues with acceptance checks. Label navigation/save/performance/security behavior unverified. Do not claim implementation changes or test results.

## Localization and constraints

Prompt:
“Use $craft-crm for a bilingual French/English field-sales CRM on phones and intermittent mobile internet.”

Expected handling:
Prioritize phone workflows, larger hit areas, long translated labels, locale numbers/dates, explicit sync status and retained drafts. Do not promise offline mutations without an implemented storage/reconciliation model.

## Extension rule

When a request has domain-specific rules outside the corpus, research those separately. Use this skill for UI composition and workflows; do not invent medical, legal, accounting, or regulatory requirements.
