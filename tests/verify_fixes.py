import os
import json
import sys
from pathlib import Path

# Add mcp directory to sys.path to import server directly
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, os.path.join(project_root, "mcp"))

try:
    import server
except ImportError as e:
    print(f"Error importing server: {e}")
    sys.exit(1)

def test_redirect_map():
    print("Testing Redirect Map logic...")

    # 1. Initialize state
    server.seo_load("sample-export")
    server.seo_detect()

    # 2. Simulate a model-generated redirect map
    test_redirects = [
        {"from": "http://nmgtechnologies.com/old-page", "to": "http://nmgtechnologies.com/new-page", "reason": "Content migrated"},
        {"from": "http://nmgtechnologies.com/about-us-old", "to": "http://nmgtechnologies.com/about", "reason": "URL simplification"}
    ]

    print(f"Applying test redirect map with {len(test_redirects)} entries...")
    server.seo_set_fixes(redirect_map=test_redirects)

    # 3. Export report
    server.seo_report()

    # 4. Verify output file
    report_path = "outputs/report.json"
    if not os.path.exists(report_path):
        print("Error: report.json not found")
        return

    with open(report_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    fixes = data.get("fixes", {})
    redirect_map = fixes.get("redirect_map", [])

    if len(redirect_map) == len(test_redirects) and redirect_map[0]["from"] == test_redirects[0]["from"]:
        print("SUCCESS: Redirect map correctly persisted to report.json")
        print(f"Proof: Found {len(redirect_map)} redirects in output.")
        print(json.dumps(redirect_map, indent=2))
    else:
        print("FAILURE: Redirect map does not match expected input")
        print(f"Expected {len(test_redirects)}, found {len(redirect_map)}")

if __name__ == "__main__":
    test_redirect_map()
