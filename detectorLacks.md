# Analysis of Gaps: `seo/detector.py` vs `rulebook.md`

This document details the missing functionality in the current `seo/detector.py` implementation when compared to the project's official SEO Detection Rulebook.

## 1. Missing Issue Types and Severities
The current detector handles 7 out of the 17 rules. The following 10 rules are **not yet implemented**:

| Type | Rule | Severity | Category |
| :--- | :--- | :--- | :--- |
| `title_too_short` | `Title 1 Length` < 30 (and not empty) | Low | Metadata |
| `missing_meta_description` | `Meta Description 1` empty, indexable 200 page | Medium | Metadata |
| `duplicate_meta_description` | same `Meta Description 1` on 2+ indexable URLs | Medium | Metadata |
| `meta_description_too_long` | `Meta Description 1 Length` > 155 | Low | Metadata |
| `missing_h1` | `H1-1` empty on a 200 page | Medium | Content |
| `duplicate_h1` | same `H1-1` on 2+ indexable URLs | Low | Content |
| `thin_content` | `Word Count` < 200 on an indexable page | Low | Content |
| `redirect_chain` | a redirect whose `Redirect URL` is itself a redirecting URL | High | Infrastructure |
| `non_indexable_but_linked` | `Indexability` = Non-Indexable AND `Inlinks` > 0 | Medium | Infrastructure |
| `slow_page` | `Response Time` > 1.0 | Low | Performance |

---

## 2. Analysis of Unhandled Classes/Categories

### A. Meta-Description Auditing (Complete Gap)
The detector does not access `Meta Description 1` or `Meta Description 1 Length`. It cannot detect missing, duplicate, or oversized meta descriptions.

### B. Heading (H1) Analysis (Complete Gap)
The detector does not monitor the `H1-1` column. It is unable to determine if a page is missing its primary heading or if multiple pages share the same H1.

### C. Page Depth & Indexing Strategy (Partial Gap)
While orphan pages are caught, the detector fails to identify **"Non-indexable but linked"** pages—where internal link equity is wasted on pages marked as non-indexable.

### D. Content Quality (Complete Gap)
There is no check for **Thin Content**. The `Word Count` column is ignored, meaning pages with insufficient text are not flagged.

### E. Advanced Infrastructure & Performance (Complete Gap)
- **Redirect Chains**: The detector lacks the mapping logic (`Address` $\rightarrow$ `Redirect URL`) required to identify chains or loops.
- **Page Speed**: The `Response Time` column is ignored, meaning slow-loading pages are not detected.

## 3. Summary of Coverage
- **Implemented**: $\sim 41\%$ of the rulebook.
- **Missing**: $\sim 59\%$ of the rulebook.
- **Critical Missing Rules**: `redirect_chain` (High Severity) and `missing_meta_description` (Medium Severity).
