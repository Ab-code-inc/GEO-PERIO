# Scientific data structure

## Workbooks

`03_Source_Data.xlsx` has a README, a data dictionary, code-value definitions, main figure and table sheets, and supplementary figure/table sheets. Each figure sheet identifies its panels, header row and data ranges. The dictionaries define variables, units, statistical correction families and blank-cell meanings. Main Table 2 contains candidate-gene evidence; Supplementary Table 31 contains the analytical chronology.

The seven supplementary workbooks retain their supplied sheet names and column definitions. Their README and definition sheets describe the scientific unit represented by each row. Claims, hypotheses, genes, cohorts, participants, samples and panels are distinct units and must not be counted interchangeably. Multiple panels may share the same evaluation participants.

The three supplementary ZIP files contain larger result tables and their own README and column definitions. Interpret single-cohort estimates and moderated tests separately from pooled random-effects estimates and Hartung–Knapp tests, as identified in the table definitions.

## Figure tables

Within the figure reproduction asset, `data/Figure_01` through `data/Figure_07` and `data/Supplementary_Fig_01` through `data/Supplementary_Fig_20` contain standalone CSV source tables. `FIGURE_SOURCE_TABLES.csv` indexes panels and workbook ranges; `PLOTTED_SOURCE_TABLES.csv` indexes the exact tables emitted by the current plotting scripts.

Each figure has a `data_dictionary.csv` and a manifest linking its data, code and checksums. Figures 1 and 7 also have annotation tables containing text, x/y positions in millimetres, font sizes in points and annotation roles. Annotation positions and illustrative shapes are layout parameters, not measured biological quantities.

CSV files use UTF-8 and a header row. Empty cells remain empty. Boolean values exported from workbooks use `TRUE` and `FALSE`. Numeric CSV exports preserve stored values without additional rounding; plotting inputs can retain more floating-point precision than Excel storage. Units, denominators, directional conventions, missing-value meanings and correction families are specified by the associated dictionary or source block.

## Interpretation

- A count of claim records is distinct from a count of unique hypotheses or genes.
- Nominal statistical support does not establish strict replication or a validated biomarker.
- An inconclusive cross-disease result is not evidence of absence or equivalence.
- The complete-result-list variable is an extraction proxy and does not measure reporting-checklist completeness.
- Disease-process set-by-cell-type q values use Benjamini–Hochberg correction across all set-by-cell-type tests within each dataset. Other q-value families are defined for their own panels.
- Historical timing categories describe when analyses occurred; they do not establish that every rule was prospectively registered.

The final source tables retain the uncertainty and eligibility distinctions used in the associated scientific report.
