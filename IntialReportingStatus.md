# Initial Reporting Status: SEO Detector Analysis

This document records the initial analysis of the `seo/detector.py` component, detailing the parameters used to audit the `internal_all.csv` export from Screaming Frog.

## 1. Filtering Parameters
To ensure audit accuracy and reduce noise, the detector filters for "Indexable HTML" pages (`idx200` group) using the following columns:
- **Content Type**: Must contain `text/html`.
- **Status Code**: Must be `200`.
- **Indexability**: Must be `indexable`.

## 2. Issue Detection Parameters
The following parameters are monitored to detect specific SEO issues:

| Parameter (Column) | Issue Type | Detection Logic | Severity |
| :--- | :--- | :--- | :--- |
| **Title 1** | `missing_title` | Title is empty or only whitespace. | High |
| **Title 1** | `duplicate_title` | Multiple different URLs sharing the exact same title text. | High |
| **Title 1 Pixel Width** | `title_too_long` | Pixel width exceeds **561px**. | Medium |
| **Title 1 Length** | `title_too_long` | Character length exceeds **60**. | Medium |
| **Status Code** | `broken_link` | HTTP status code is between **400–499**. | High |
| **Status Code** | `server_error` | HTTP status code is between **500–599**. | High |
| **Status Code** | `redirect` | HTTP status code is between **300–399**. | Medium |
| **Inlinks** | `orphan_page` | Page is indexable but has **0 internal links** pointing to it. | Medium |
| **Address** | *All* | Used as the identifier for affected URLs. | N/A |

## 3. Architectural Observations
- **Scope Isolation**: Content-related issues (Titles, Orphan pages) are only analyzed for pages that are HTML, return 200 OK, and are indexable.
- **Global Infrastructure Checks**: Response code errors (4xx, 5xx, 3xx) are analyzed across all rows in the export.
- **Deterministic Logic**: The detection uses plain Python logic and thresholds, ensuring the model is reserved for high-value judgment tasks rather than data filtering.
