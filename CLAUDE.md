# CLAUDE.md — project memory for the SEO Command Center build




## What we are building
A Claude Code plugin that ingests a Screaming Frog SEO export (`internal_all.csv` + issue
CSVs), audits it against the rulebook, prioritizes issues, writes fixes, serves a live
dashboard at localhost:7700, and outputs `outputs/report.json` + `outputs/report.html`.

## Hard rules (the agent must follow these)
- Detect issues in **plain Python** (csv/pandas). Use the model only for judgment
  (rewriting titles/metas, choosing redirect targets). Never feed raw crawl rows to the model.
- `outputs/report.json` MUST match `report.schema.json`. Validate before declaring done.
- Filter to `text/html` + indexable pages before title/meta checks (see `rulebook.md`).
- Do not hard-code anything to the sample export — it must work on an unseen export.
- Keep model calls small and few (free-tier quota). One page per fix call.
- Do not add emojis in the print statements/code. Keep all the code simple.

## Architecture 
- `skills/seo-audit/SKILL.md` orchestrates. Sub-agents: ingest, auditor, fixer, reporter.
- `seo/detector.py` = deterministic detectors (extend to the full rulebook — biggest score).
- `mcp/server.py` = MCP tools + the live dashboard.
- `agents` = testing agent to check number of detects after each iteration of changes to seo/detector.py.

## Conventions
- Commit after each working step with a real message.
- Run `python run.py sample-export/` to test end to end.

## Things I have learned during the build (update this as you go)
- (e.g. "SF leaves Title 1 blank on redirected URLs — must filter Status Code 200 first")
- Needed to install `jq` for parsing session
- Current detectors cover missing titles, duplicate titles, and broken internal links. Next steps:
  - Add missing meta descriptions (filtering to indexable HTML first)
  - Add short/long title/meta detectors (with pixel/char limits)
  - Add more issue types from the rulebook
  - Add the fixer agent to write title/meta fixes and a redirect map for broken links
