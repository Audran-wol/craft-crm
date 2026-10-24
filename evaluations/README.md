# Behavioral evaluation

The three original trial prompts and a follow-up custom-control request are recorded in tasks.json. The legacy fixture is deliberately defective, and the sales example is synthetic.

For a fresh trial, provide a clean agent with the skill path, one task prompt, a disposable output directory, and only the raw fixture if required. Do not supply expected observations or saved conclusions to the generating agent. Afterwards compare actual artifacts with the task's expected observations. Distinguish source inspection, a logic harness, browser interaction, screenshots and assistive-technology checks.

Repairs with known findings are follow-up repairs, not blind first-run successes. A controlled improvement claim would require matched trials without the skill, repeated runs, fixed model/tool conditions and independent judging; that experiment has not been performed.

From the repository root:

```sh
node evaluations/verify_audit.cjs
node examples/sales/verify_storage.cjs
```

The first command reproduces six known defects with document stubs, not a browser. The second checks the exact embedded example storage engine with an in-memory adapter. Passing the defective fixture's reproduction harness does not mean the fixture is usable. See RESULTS.md for scoped evidence and its limits.
