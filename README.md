# When Valid Evidence Goes Unused in Oncology Agents

Supplementary materials for the submitted manuscript.

- **[Extended Methods and Results](extended_methods_and_results.pdf)**: the original bibliography and Appendices A to F, a navigation cover, and addendum sections S1 to S6.
- **[Addendum only](supplement_addendum.pdf)**: study map, paired terminal outcomes, selected explanation observations, prompt sensitivity, and interpretation limits.
- **[Original supplement](archive/extended_methods_and_results_20260927.pdf)**: unchanged 32-page archival edition.
- **[Paired outcome data](data/paired_outcomes.csv)** and **[reaggregation script](source/analyze.py)**: 90 pairs matched by case and repetition from the existing common-prompt experiment.

The addendum summarizes existing outcomes and explains what the studies can support. We ran no new model generations; the submitted manuscript, original scores, and prespecified primary contrast are unchanged. We selected the explanation examples after inspecting outcomes. They do not provide a complete qualitative census or establish an internal causal mechanism.

## Reading the supplement

The original bibliography and appendices occupy PDF pages 2 to 32 and retain their printed page, section, table, and figure numbers. For those pages, **PDF page = original printed page − 8**. The addendum begins on **PDF page 33**, with printed pages S1 onward.

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
| Clarifications and paired-outcome accounting | S1 to S6 | 33 |

References to main-text sections and figures refer to the submitted manuscript. Section S1 summarizes how the studies relate to one another.

## Reproduce the update

Requires Python 3, PyMuPDF, and `pdflatex` with the standard LaTeX packages used in `source/`. From the repository root:

```bash
python3 source/analyze.py
python3 source/build.py
```

The analysis script reproduces the addendum's paired counts from the public CSV. The build compiles the cover and addendum, checks that the original bibliography and appendix pages render identically, and verifies that identifying PDF metadata is empty. `data/verification.json` records checks and artifact hashes. PDF byte hashes may change with TeX build timestamps.

The public CSV contains exported terminal labels. It is sufficient to recompute the counts, but independently regrading the responses would require the underlying records and model outputs. This repository excludes licensed corpus text, case-specific candidate payloads, complete response transcripts, and private reader forms. The addendum source and build work without those materials.
