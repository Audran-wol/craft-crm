# Revamp an existing CRM

## Baseline

Inspect routes, package manifest/lockfile, tokens, shell, representative list/record/form code, data contracts, and permissions. Inspect live/local UI when possible. Keep before images internal unless deliverables are requested; do not expose private customer data.

Inventory route/task, component owner, data/query state, permissions, save mechanism, observed defect, inferred risk, preserved behavior, proposed change, acceptance check.
Screenshots establish appearance, not backend defects. Code establishes implementation, not verified rendering. If code is absent, give actionable guidance and ask for it only when needed for implementation.

## Prioritize

P0: data exposure/loss, blocked primary workflow, inaccessible required action.
P1: confusing hierarchy/scope, broken navigation, clipping, unusable responsive layout.
P2: spacing/icon/radius/color inconsistency and avoidable truncation.
P3: optional refinements.
Do not hide P0/P1 behind polish or invent security findings from screenshots.

## Sequence

1. Consolidate tokens and canvas/work surfaces.
2. Unify shell/header/gutters/scroll ownership.
3. Align toolbar and separate query from record actions.
4. Improve columns, density, selection, numbers, statuses.
5. Clarify record hierarchy while retaining list context.
6. Fix forms, overlays, validation, focus.
7. Reuse patterns on other routes.
8. Verify targeted regressions and visuals.

Use an isolated change set. Do not migrate frameworks, replace the component library, redesign databases, or rename routes solely to fix UI.

| Symptom | Investigate | Prove |
| --- | --- | --- |
| White everywhere | Surface tokens | Clear hierarchy without extra card wrappers |
| Floating toolbar | Parent containers/gutters | Controls align with data |
| Double scrollbar | Root height, overflow, minimums | Intentional keyboard-accessible scroll |
| Team dropdown obscures content | Portal/anchor/clipping/max height | Fits viewport and returns focus |
| Misaligned metric actions | Fixed offsets/header layout | Works with long labels |
| Five buttons on one row | Frequency/scope | Action hierarchy without lost functions |
| Better table, inconsistent header | Duplicate shells | Shared header across routes |
| Empty after filtering | Page/query coupling | Reset/clamp page; honest errors |
| “Saved” after failure | Mutation lifecycle | Confirmed success or rollback with retained draft |

Report before/after route/viewport, preserved task, component change, checks, and untested states. Do not claim measured conversion or task-time gains without data.
