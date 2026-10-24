#!/usr/bin/env python3
"""Score evidence supplied by a reviewer; never inspect or certify a UI."""
import argparse
import json
import sys

GATES = {f"G{i:02d}" for i in range(1, 8)}
WEIGHTS = dict(workflow=25, architecture=15, composition=20,
               consistency=15, accessibility=15, resilience=10)
STATUSES = {"pass", "fail", "unknown", "not_applicable"}

def has_text(value):
    return isinstance(value, str) and bool(value.strip())

def evaluate(data):
    if not isinstance(data, dict):
        raise ValueError("audit must be an object")
    if not has_text(data.get("scope")):
        raise ValueError("scope is required")
    gates = data.get("gates", [])
    dimensions = data.get("dimensions", [])
    if not isinstance(gates, list) or not all(isinstance(g, dict) for g in gates):
        raise ValueError("gates must be a list of objects")
    if not isinstance(dimensions, list) or not all(isinstance(d, dict) for d in dimensions):
        raise ValueError("dimensions must be a list of objects")
    if len(gates) != 7 or {g.get("id") for g in gates} != GATES:
        raise ValueError("exactly G01–G07 are required, without duplicates")
    if len(dimensions) != 6 or {d.get("id") for d in dimensions} != set(WEIGHTS):
        raise ValueError("all six dimensions are required, without duplicates")
    blockers = []
    applicable_gates = 0
    for gate in gates:
        status = gate.get("status")
        if not isinstance(status, str) or status not in STATUSES:
            raise ValueError(f"{gate['id']}: invalid status")
        if status == "not_applicable":
            if not has_text(gate.get("reason")):
                raise ValueError(f"{gate['id']}: not_applicable requires reason")
            continue
        applicable_gates += 1
        if status in {"pass", "fail"} and not has_text(gate.get("evidence")):
            raise ValueError(f"{gate['id']}: {status} requires evidence")
        if status != "pass":
            blockers.append(f"{gate['id']}: {status}")
    if applicable_gates == 0:
        raise ValueError("at least one critical gate must apply")
    weighted = covered = applicable = 0
    for dim in dimensions:
        key = dim["id"]
        if type(dim.get("applicable")) is not bool:
            raise ValueError(f"{key}: applicable must be boolean")
        if dim.get("weight") != WEIGHTS[key]:
            raise ValueError(f"{key}: weight must be {WEIGHTS[key]}")
        if not dim["applicable"]:
            if not has_text(dim.get("reason")):
                raise ValueError(f"{key}: exclusion requires reason")
            if dim.get("score") is not None:
                raise ValueError(f"{key}: excluded dimension must have null score")
            continue
        applicable += WEIGHTS[key]
        score = dim.get("score")
        if score is None:
            blockers.append(f"{key}: unverified")
            continue
        if type(score) is not int or not 0 <= score <= 4:
            raise ValueError(f"{key}: score must be integer 0–4 or null")
        if not has_text(dim.get("evidence")):
            raise ValueError(f"{key}: score requires evidence")
        covered += WEIGHTS[key]
        weighted += WEIGHTS[key] * score / 4
    if applicable == 0:
        raise ValueError("at least one scored dimension must apply")
    score = round(weighted / applicable * 100, 1)
    if score < 85:
        blockers.append("weighted score below the heuristic threshold of 85")
    return {
        "status": "ready" if not blockers else "not_ready",
        "scope": data["scope"],
        "score": score,
        "evidence_coverage_percent": round(covered / applicable * 100, 1),
        "applicable_weight": applicable,
        "ready_within_reviewed_scope": not blockers,
        "blockers": blockers,
        "limitations": data.get("limitations", []),
        "notice": "Reviewer-supplied evidence only; no automated UI or accessibility certification."
    }

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", help="Completed audit JSON file")
    parser.add_argument("--format", choices=("json", "text"), default="json",
                        help="JSON for automation (default), or a readable review summary")
    args = parser.parse_args(argv)
    try:
        with open(args.audit, encoding="utf-8") as file:
            result = evaluate(json.load(file))
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        label = "READY WITHIN REVIEWED SCOPE" if result["ready_within_reviewed_scope"] else "NOT READY"
        print(f"{label} — {result['score']}/100")
        print(f"Scope: {result['scope']}")
        print(f"Evidence coverage: {result['evidence_coverage_percent']}%")
        for blocker in result["blockers"]:
            print(f"- {blocker}")
        if not result["ready_within_reviewed_scope"]:
            print("Valid review processed successfully. Exit 1 indicates findings, not a script crash.")
        print(result["notice"])
    return 0 if result["ready_within_reviewed_scope"] else 1

if __name__ == "__main__":
    sys.exit(main())
