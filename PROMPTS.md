# PROMPTS.md — my key prompts log

Keep the handful of prompts that actually moved the build. Not every message — the ones that
mattered: the system/sub-agent prompts, the ones you iterated on, the "this finally worked"
moment. This shows how you direct an AI, which is graded (challenge brief section 08).

Format per entry:
- **Prompt** (paste it)
- **For:** what you were trying to do
- **Revised?** did you have to change it, and why

---

## Example (replace with your own)

- **Prompt:** "Extend seo/detector.py to detect redirect chains: build a map of {Address ->
  Redirect URL} for all 3xx rows, then a chain exists when a Redirect URL is itself a key in
  that map. Add a redirect_chain issue (High). Run python seo/detector.py and show counts."
- **For:** adding the redirect-chain detector
- **Revised?** Yes — first version flagged single redirects as chains; added the "target is
  also a redirecting URL" condition.

---

## My prompts
1.
- **Prompt:** "Record the previous output in a IntialReportingStatus.md"
- **For:** reporting the initial status of the project before I started building (for the judges to see the progress).
- **Revised?** No, it worked on the first try.
2.
- **Prompt:** "give analysis of the seo/detector.py . On what different parameters it is currently doing the analysis of the internal_all.csv file"   
- **For:** understanding the current state of the detector and how it works with the internal_all.csv file.
- **Revised?** No, it provided a clear analysis of the current state of the detector and how it processes the internal_all.csv file.
3.
- **Prompt:** "Implemet the functions for the Unhandled classes/categories in the detectorLacks.md in the
  section 2.A and 2.B"
- **For:** extending the detector to cover the missing functionality related to meta-description auditing and heading (H1) analysis.
- **Revised?** No, the implementation showed signs of working as number of issues increased in the output from 4 to 8.
4. - 
- **Prompt:** "Implement the function for the Unhandled classes/categories in the detectorLacks.md in the
  section 2.C, 2.D"
- **For:** further extending the detector to cover the remaining missing functionality related to page depth & indexing strategy, content quality, and advanced infrastructure & performance.
- **Revised?** No, the implementation was successful as the number of detected issues increased from 8 to 10.
5. - **Prompt:** "❯ Implemet the functions for the Unhandled classes/categories in the detectorLacks.md in the  
     section 2.E ,use and write advanced functions to call base llm model for anything which     
     needs analysis and reasoning to complete the function/detect the issue."
- **For:** completing the implementation of the detector to cover all the missing functionality, including advanced functions that require analysis and reasoning.
- **Revised?** Yes, the first version of the prompt was too vague and did not specify which advanced functions to implement. The revised prompt provided more clarity on the specific functions to implement and how to use the base LLM model for analysis and reasoning.



