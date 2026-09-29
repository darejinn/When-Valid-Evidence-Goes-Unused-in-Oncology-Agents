# When Valid Evidence Goes Unused in Oncology Agents

Supplementary materials for the submitted manuscript.

- **[Extended Methods and Results](extended_methods_and_results.pdf)**: archival bibliography and Appendices A–F, with a revised navigation cover and an addendum S1–S6.
- **[Addendum only](supplement_addendum.pdf)**: study map, paired terminal outcomes, selected explanation observations, prompt sensitivity, and interpretation limits.
- **[Original supplement](archive/extended_methods_and_results_20260927.pdf)**: unchanged 32-page archival edition.
- **[Paired outcome data](data/paired_outcomes.csv)** and **[reaggregation script](source/analyze.py)**: 90 case–repetition pairs from the existing common-prompt experiment.

The update adds descriptive accounting of existing outcomes and clarifies the scope of the evidence. It introduces no new model generations and does not change the submitted manuscript, original scores, or prespecified primary contrast. Selected explanation examples are not a completed qualitative census or evidence of an internal causal mechanism. See [CHANGES.md](CHANGES.md).

## Reading the supplement

The archival body remains on PDF pages 2–32. Its original printed page, section, table, and figure numbers are preserved. For those pages, **PDF page = original printed page − 8**. The new addendum begins on **PDF page 33**, with printed pages S1 onward.

| Material | Section | PDF page |
|---|---|---:|
| Bibliography | References | 2 |
| Historical agent audits | A | 3 |
| Corpus, retrieval, and execution | B | 7 |
| Additional related work | B.6 | 12 |
| Earlier repair protocols | C | 12 |
| Common-prompt fresh/repair/reset study | D | 20 |
| Inventory and saved-path serialization | E | 25 |
| Earlier inventory explanation audits | E.5 | 29 |
| Source review and validation status | F | 29 |
| Clarifications and paired-outcome accounting | S1–S6 | 33 |

References to main-text sections and figures refer to the submitted manuscript. Historical implementation/version names in the archival body identify earlier studies; the addendum supplies descriptive study names. Archival references to a larger source delivery or companion report are not claims that those files are included in this repository.

## Reproduce the update

Requires Python 3, PyMuPDF, and `pdflatex` with the standard LaTeX packages used in `source/`. From the repository root:

```bash
python3 source/analyze.py
python3 source/build.py
```

The analysis script reproduces the addendum's paired counts from the public CSV. The build compiles the cover and addendum, preserves the archival body, and verifies page-render equality and anonymous PDF metadata. `data/verification.json` records checks and artifact hashes. PDF byte hashes may change with TeX build timestamps.

The public CSV contains exported terminal labels, not candidate records or full model responses. It supports reaggregation, not independent regrading of the underlying responses. Licensed corpus text, case-specific candidate payloads, complete response transcripts, and private reader forms are not distributed here. The addendum source and build do not require those materials.
