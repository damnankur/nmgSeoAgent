# DECISIONS.md — decision & learnings log

A short running note of the real choices you made: what you tried, what failed and why, what
you changed. This is your engineering judgement on the record — it is what separates a builder
from a button-presser, and it is graded (challenge brief section 08).

Append a 1–2 line entry whenever you make a real decision or hit/fix a wall. Add a timestamp.

Format:
`[HH:MM] <decision or problem> → <what you did and why>`

---

## Example (replace with your own)
- `[10:20]` Chose plain-csv parsing over pandas → fewer deps, fast enough for 5k rows, model
  quota saved for the fixer.
- `[11:05]` Title detector over-counted duplicates → realized non-indexable pages were
  included; added an indexable+200 filter (per rulebook).
- `[12:40]` Dashboard wasn't updating live → MCP tool wasn't emitting the SSE event; added
  `_emit("issue", row)` in extract.

---

## My log
- `[12:09]` The Settings.json file had some issues with the commands, resolved by claude agent.
- `[01:03]` Installed a missing library named jq for proper parsing of session logs.
- `[02:26]` Did analysis of Current seo/detector.py and found that it was only covering a few issue types vs all the issues in rulebook.md.
- `[03:10]` Implemented the functions for the Unhandled classes/categories in the detectorLacks.md in the section 2.A and 2.B related to meta-description auditing and heading (H1) analysis.
- `[03:15]` Implemented the function for the Unhandled classes/categories in the detectorLacks.md in the section 2.C, 2.D related to page depth & indexing strategy, content quality, and advanced infrastructure & performance.
- `[03:29]` Implemented the function for the Unhandled classes/categories in the detectorLacks.md in the section 2.E related to advanced infrastructure & performance, including advanced functions that require analysis and reasoning.
- 
- 