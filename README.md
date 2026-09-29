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

## Find material cited in the paper

Use this guide with the 20-page submitted paper, **When Valid Evidence Goes Unused in Oncology Agents**. The paper condenses the appendices, so its subsection and table numbers differ from those in the supplement. The links below open [Extended Methods and Results](extended_methods_and_results.pdf); page numbers refer to the PDF viewer. Match references by topic using the table below.

| Reference in the paper | Corresponding material in the supplement | PDF pages |
|---|---|---|
| Table 1: protocol roles and budgets | Study overview in S1; repair protocols in Table 14 and inventory methods in E.1 | [33](extended_methods_and_results.pdf#page=33), [13](extended_methods_and_results.pdf#page=13), [25](extended_methods_and_results.pdf#page=25) |
| Appendix B, Table 3: shared samples and execution limits | B.1 and B.5; study-specific settings in C, D and E | [7](extended_methods_and_results.pdf#page=7), [10 to 12](extended_methods_and_results.pdf#page=10) |
| Introduction; Appendix A, Table 2: typed-output scope errors | A.4, Table 4: 68/352 invalid claims and 28/144 affected trajectories | [4 to 5](extended_methods_and_results.pdf#page=4) |
| Section 2; Appendix B: corpus, eligibility, retrieval, execution | B.1 to B.5; execution and historical artifact descriptions are in B.5 | [7 to 12](extended_methods_and_results.pdf#page=7) |
| Section 3; Appendix C.1, Table 4: fixed exposure | C.1, Table 15; terminal outcomes in Table 17 | [13 to 15](extended_methods_and_results.pdf#page=13) |
| Section 4.3; Appendix C.2, Table 4: live retry | C.2, Tables 16 and 17 | [14 to 15](extended_methods_and_results.pdf#page=14) |
| Appendix C.3: initial instructions and message structure | C.4: initial system instruction, checklist text, feedback tail, and message assembly | [19 to 20](extended_methods_and_results.pdf#page=19) |
| Section 4; Appendix D.1, Table 5: common prompt and five conditions | D.1, Table 22; exact common system instruction and final command | [20 to 21](extended_methods_and_results.pdf#page=20) |
| Appendix D.2: design, scoring, statistical analysis | D.2 | [21 to 22](extended_methods_and_results.pdf#page=21) |
| Appendix D.3, Tables 6 and 7: outcomes and paired contrasts | D.3, Tables 23 and 24; pooled contrasts in Table 25 | [22 to 23](extended_methods_and_results.pdf#page=22) |
| Appendix D: detailed resource accounting | D.4, Table 26 | [24](extended_methods_and_results.pdf#page=24) |
| Section 5.1; Appendix E.1: inventory task and saved logs | E.1 to E.2, Tables 27 to 29 | [25 to 26](extended_methods_and_results.pdf#page=25) |
| Appendix E.2, Table 8: serialization on the same retrieved records | E.4, Tables 31 and 32; replay verification continues on page 29 | [28 to 29](extended_methods_and_results.pdf#page=28) |
| Appendix E.3: controls and output omissions | Controls in E.3; omissions in E.4; prognostic/N/A example in E.5 | [27 to 29](extended_methods_and_results.pdf#page=27) |
| Section 5.2; Appendix F, Table 9: twelve-family judgments | F.3, Table 35; joint judgments are marked J | [31](extended_methods_and_results.pdf#page=31) |
| Appendix F, Table 10: W04 genotype and model distinction | F.3, W04 discussion following Table 35 | [31](extended_methods_and_results.pdf#page=31) |
| Appendix F: review procedure and completion status | F.1 to F.4, Tables 33 to 36 | [29 to 32](extended_methods_and_results.pdf#page=29) |

The addendum's tables belong to sections S1 and S2 and have their own numbering. They are not replacements for the paper's tables. Section S6 (PDF page 37 onward) also contains a guide to the paper's references and file availability.

## Files cited in the paper

The `versions/`, `analysis_inputs/`, `runs/`, and `design/` paths in the paper and the original appendices refer to the research workspace used for the experiments. **Those directories are not included in this repository.** In particular, the directory map in original Appendix B.5, Table 13 describes that workspace, not this repository's file tree. Readers can use the passages below to understand the methods. Running the original experiments would require the original code and inputs.

| Path or document cited in the paper | Where to read the corresponding description | Availability here |
|---|---|---|
| `versions/v14-full-paper-revision/README.md`, `src/common.py`, `src/agents.py` | B.1 to B.5, PDF pages 7 to 12 | Original README and code not included |
| `analysis_inputs/prompt_material_exact.json` | C.4, PDF pages 19 to 20: initial system instruction, checklist core and feedback tail | Disclosed text in PDF; original JSON not included |
| V40 `src/study.py`; V38 E1 `src/runner.py` and `src/feedback.py` | C.1 to C.2 and C.4, PDF pages 13 to 15 and 19 to 20 | Protocol descriptions in PDF; original code not included |
| `analysis_inputs/v41_public_prompt_contract.json` | D.1, PDF pages 20 to 21: exact common system instruction and final command | Disclosed instructions in PDF; full JSON, schema and request hashes not included as files |
| `versions/v41-repair-history-control/` | D.1 to D.4, PDF pages 20 to 24 | Study description and aggregate results in PDF; original experiment directory not included |
| Other study directories, execution plans, timing files and score files listed in B.5 | B.5, PDF pages 10 to 12; relevant study appendices | Original files and complete per-run results not included |
| Saved-pool replay code and inputs listed in B.5 | E.4, PDF pages 28 to 29 | Procedure and reported checks in PDF; executable replay and original inputs not included |
| Companion technical report | Historical studies in A and C, and review scope in F | Separate companion report not included; its additional results are not supplied by this PDF |
| Signed reader submissions and source-bearing review materials | F.1 to F.4, PDF pages 29 to 32 | Methods and reported judgments in PDF; underlying restricted materials not included |

## What can be reproduced from this repository

[data/paired_outcomes.csv](data/paired_outcomes.csv) contains 90 pairs of fresh and diagnostic-repair terminal labels (180 outputs): 64 co-alteration pairs and 26 sibling-disease pairs. [source/analyze.py](source/analyze.py) recomputes the paired counts in S2 and writes [data/paired_summary.json](data/paired_summary.json). This is a subset of the 450 outputs across all five common-prompt conditions.

The CSV does not include variant-cluster assignments, the other three conditions, candidate records, or full responses. It therefore supports the published count reaggregation, but not independent response scoring, reconstruction of all five conditions, or reproduction of the reported variant-cluster bootstrap intervals. The repository also does not include the original experiment runners or saved-pool replay inputs.

To recompute the paired counts, run Python 3 from the repository root:

```bash
python3 source/analyze.py
```

To rebuild the PDFs, also install PyMuPDF and `pdflatex` with the LaTeX packages used in `source/`, then run:

```bash
python3 source/build.py
```

The build compiles [source/cover.tex](source/cover.tex) and [source/addendum.tex](source/addendum.tex), combines them with the original bibliography and appendices, and checks that those original pages have identical text and rendering. It also checks that identifying PDF metadata is empty. [data/verification.json](data/verification.json) records the checks and artifact hashes. PDF byte hashes may change with TeX build timestamps.

Licensed corpus text, case-specific candidate payloads, complete response transcripts, and private reader forms are not distributed here. They are not needed to recompute the public paired counts or rebuild these PDFs.
