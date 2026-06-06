import os
import json
import sys
from pathlib import Path

# Add project root to sys.path to allow importing seo.detector
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

try:
    from seo import detector
except ImportError:
    print("Error: Could not import seo.detector. Ensure you are running from the project root.")
    sys.exit(1)

DATA_STORE_FILE = "testDataStore.md"
EXPORT_DIR = "sample-export"
SCHEMA_FILE = "report.schema.json"

def validate_schema(issues, summary):
    """
    Manual structural verification against report.schema.json
    since we can't assume jsonschema is installed.
    """
    errors = []

    # Validate Summary
    if not isinstance(summary, dict):
        errors.append("Summary must be an object")
    else:
        if "total_issues" not in summary or not isinstance(summary["total_issues"], int):
            errors.append("Summary missing total_issues (int)")
        if "by_severity" not in summary or not isinstance(summary["by_severity"], dict):
            errors.append("Summary missing by_severity (object)")

    # Validate Issues
    if not isinstance(issues, list):
        errors.append("Issues must be an array")
    else:
        for i, issue in enumerate(issues):
            if not isinstance(issue, dict):
                errors.append(f"Issue {i} is not an object")
                continue

            required = ["type", "severity", "affected_urls", "count"]
            for req in required:
                if req not in issue:
                    errors.append(f"Issue {i} missing required field: {req}")

            if "severity" in issue and issue["severity"] not in ["High", "Medium", "Low"]:
                errors.append(f"Issue {i} has invalid severity: {issue['severity']}")

            if "affected_urls" in issue and not isinstance(issue["affected_urls"], list):
                errors.append(f"Issue {i} affected_urls must be a list")

    return errors

def load_previous_state():
    if not os.path.exists(DATA_STORE_FILE):
        return None

    with open(DATA_STORE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the last JSON block in the file
    import re
    json_blocks = re.findall(r'```json\n(.*?)\n```', content, re.DOTALL)
    if not json_blocks:
        return None

    try:
        return json.loads(json_blocks[-1])
    except json.JSONDecodeError:
        return None

def save_state(current_results, comparison):
    # The state we store is just the list of issue types and their counts
    state = {issue["type"]: issue["count"] for issue in current_results}

    # Generate the Markdown report
    report = f"# Detector Test Report\n\n"
    report += f"## Comparison Results\n{comparison}\n\n"
    report += f"## Current State (Raw Data)\n"
    report += f"```json\n{json.dumps(state, indent=2)}\n```\n"

    with open(DATA_STORE_FILE, "w", encoding="utf-8") as f:
        f.write(report)

def main():
    print("Running Detector Testing Agent...")

    # 1. Run Detection
    try:
        rows = detector.load_rows(EXPORT_DIR)
        issues = detector.detect(rows)
        summary = detector.summarize(issues)
    except Exception as e:
        print("Detection failed: {e}")
        sys.exit(1)

    # 2. Validate Schema
    schema_errors = validate_schema(issues, summary)
    if schema_errors:
        print("Schema Validation Failed:")
        for err in schema_errors:
            print(f"  - {err}")
        sys.exit(1)
    print("Schema Validation Passed")

    # 3. Compare with Previous State
    prev_state = load_previous_state()
    current_state = {issue["type"]: issue["count"] for issue in issues}

    if prev_state is None:
        comparison = "No previous data found. This is the baseline run."
    else:
        diffs = []
        for issue_type, count in current_state.items():
            prev_count = prev_state.get(issue_type, 0)
            if prev_count != count:
                diffs.append(f"- `{issue_type}`: {prev_count} ➡️ {count}")

        # Check for issues that disappeared
        for issue_type in prev_state:
            if issue_type not in current_state:
                diffs.append(f"- `{issue_type}`: {prev_state[issue_type]} ➡️ 0 (Removed)")

        comparison = "\n".join(diffs) if diffs else "No changes in issue counts detected."

    # 4. Persist
    save_state(issues, comparison)
    print(f"Results stored in {DATA_STORE_FILE}")
    print(f"Summary: {summary['total_issues']} issue types detected.")

if __name__ == "__main__":
    main()
