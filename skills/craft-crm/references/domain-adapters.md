# Adapt the foundation to any CRM domain

These are original starting hypotheses, not validated domain specifications or a request to build every listed module. Confirm the actual work, terminology, relationships and permissions in the user's brief/project. Sources S04–S06/S32–S35 support flexible records, views, activities and staged workflows; they do not independently validate every domain below.

## Stable core, variable domain

Treat a CRM as a relationship system rather than a fixed sales dashboard:

| Core concept | Design contract |
| --- | --- |
| Record/object | Stable ID, human identity, permitted fields, lifecycle, source of truth |
| Relationship | Person-to-organization, record-to-opportunity, many-to-many roles; explicit cardinality |
| Activity | Actor, related records, type, happened/due time, outcome, next action |
| View | Query, sort, visible fields, layout, ownership and sharing scope |
| Workflow | Valid states/transitions, required information, responsible operator, recovery |
| Access | Workspace/team/record/field restrictions enforced by backend |
| History | Who changed what, when; distinguish communication from system activity |
| Configuration | Field types, labels, validation, allowed options and permissions; version safely |

A person can belong to several organizations with different roles. A record can have multiple relationships. Do not duplicate a person's identity merely to fit one company column. Do not expose every relationship in the default list.

## Domain starting points

| CRM context | Primary objects | Frequent work | Useful initial view | Special questions to resolve |
| --- | --- | --- | --- | --- |
| B2B sales | Accounts, contacts, opportunities, activities | Follow up, qualify, progress opportunities | Records + optional pipeline | Multi-contact deals, currencies, stage rules |
| Real estate | People, properties, inquiries, viewings, transactions | Match needs, arrange viewings, track interest | Searchable records + appointments | Many prospects per property, availability, media, location scope |
| Recruiting | Candidates, employers, roles, applications, interviews | Match, review applications, schedule interviews | Role/application queue | One person has multiple applications; evaluate each separately |
| Agency/professional services | Clients, contacts, engagements, requests | Client follow-up, scope handoff, service review | Client records + next actions | Sales-to-delivery boundary, account ownership, external collaborators |
| Customer success | Accounts, users/contacts, plans, renewals, tasks | Review adoption, resolve risks, prepare renewal | Prioritized account queue | Define health signals and renewal dates; no unexplained scores |
| Membership/community | People, households/organizations, memberships, events | Onboard, renew, communicate, record participation | Member records + renewal queue | Multiple membership roles, household ties, communication preferences |
| Fundraising/partnerships | People, organizations, relationships, commitments, activities | Steward relationships, follow up on commitments | Relationship records + next actions | Distinguish promise, receipt and relationship status; sensitive notes |
| Admissions/education | People, programs, applications, appointments | Review applications, request information, communicate | Application queue | One person may apply to several programs; separate application state |
| Field service | Customers, sites, assets, service requests, appointments | Prepare visit, log work, follow up | Today queue + customer/site detail | Mobile reachability, unreliable connectivity, location permissions |
| Support/service desk | People, organizations, cases, conversations | Triage, assign, reply, resolve | Queue + detail | Internal vs external audience, reply drafts, defined service targets |
| Relationship/network CRM | People, organizations, interactions, reminders | Recall context, reconnect, introduce | People list + follow-up queue | Private notes, relationship context, duplicate identities |
| Channel/vendor partnerships | Organizations, contacts, agreements, reviews | Onboard, review, coordinate renewals | Organization records + review queue | Multiple roles, shared documents, agreement lifecycle |

Use invoice operations only when billing is part of the brief. Use a pipeline only when a lifecycle has meaningful stages. Use maps only when spatial decisions matter and location handling is appropriate. Use calendars when scheduling is a primary task; provide an agenda/list alternative. Use charts only when a repeated decision needs aggregation.

## Adapter procedure

1. Name the operator and three repeated tasks in their language.
2. Identify primary objects and relationships, including many-to-many cases.
3. Write one realistic record and its next action. Include missing/long/ambiguous data.
4. Define lifecycle separately for each object: candidate ≠ application, person ≠ membership, account ≠ opportunity.
5. Choose list, pipeline, operations queue or split detail from the task; mix layouts across routes when justified.
6. Select columns, record sections, forms, filters and actions. Remove irrelevant example modules.
7. Declare data scope, sensitive fields, integration ownership, locale/timezone and supported devices.
8. Build a connected main workflow, then add modules required to complete it.
9. Verify object relationships, state transitions, aggregate scope and failure recovery.

If a domain is absent from the table, perform this procedure. Do not force it into the nearest sales template. Specialized legal, medical or financial requirements need appropriate current sources and project expertise; this UI skill does not supply compliance guarantees.

## Configuration without visual chaos

Custom fields have an explicit type, formatting, operator set, validation and visibility rule. A custom status must not silently inherit unrelated colors or workflow rules. Allow a useful default view and recoverable column settings. Preserve stable identifiers when labels change. Shared-view edits and changes to organization-wide field definitions need a clear scope.

Do not build a schema editor, automation builder or permissions console unless needed. Their existence in a general CRM platform does not make them required for a focused CRM.
