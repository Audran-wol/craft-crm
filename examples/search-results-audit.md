# Worked audit: a synthetic results page

This example explains an audit output, not a before/after production case study. Its input is `evaluations/fixtures/legacy-crm.html`; `node evaluations/verify_audit.cjs` reproduces the six known logic outcomes.

| Priority | Observed issue | Proposed focused correction | Acceptance check |
| --- | --- | --- | --- |
| P0 | Rejected save resets the draft and displays Saved | Confirm success only after commit; retain draft on failure | Reject an edit, verify the text remains and no success is announced; retry and verify list/detail agreement |
| P1 | One filtered row but count still says seven | Derive rows/count/page bounds from one normalized query | Combine owner + name and verify row count, visible count and pagination agree |
| P1 | Last-page filter change produces empty rows | Reset/clamp page when criteria change | Filter from the last page and return to the first valid result page |
| P1 | Editor fields/actions lack names and focus ownership | Label fields/actions and choose an explicit dialog contract | Run keyboard/assistive-technology checks; source inspection alone does not establish the rendered result |
| P1 | Fixed width and hidden overflow threaten reachability | Responsive query bar and deliberate scrolling | Render open editor/filters at desktop and 390/320px with long labels |
| P1 | Edited values flow into raw HTML and memory-only edits look durable | Escaped text and an explicit persistence boundary | Show markup-like text literally; prove the chosen reload/save-failure contract |

A useful report keeps observed logic, source risks and unverified rendering separate. It can propose staged work: save/query correctness first, then layout and overlays, then optional refinements. Mark a stage complete only with the actual changed behavior and checks. Do not fabricate an after-score or label all gates passed from a plan.
