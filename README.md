# GEO-PERIO

Data and analysis code for the GEO-PERIO integrative study of periodontitis transcriptomes. The study combines evaluation of published gene claims with independent-cohort replication, prediction, single-cell localisation, cross-disease comparisons and periodontal tissue biology.

## Data and code

The [v1.0.1 data release](https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.1) supplies the starting inputs:

| Archive | Contents |
|---|---|
| 01_Bulk_GEO_Inputs.zip | Expression/count matrices from 31 bulk GEO series and original conversion inputs |
| 02_Primary_SingleCell_Inputs.zip | Counts, barcodes and feature annotations for GSE164241 and GSE171213 |
| 03_Additional_SingleCell_Inputs.zip | Counts, barcodes and feature annotations for GSE266897, GSE272774 and GSE283882 |
| 04_Reference_and_Study_Definitions.zip | Sample and participant maps, cohort models, comparison definitions and reference annotations |
| 05_Corrected_Claim_Inputs.zip | Literature-derived records and source-study identifiers used to construct the claim inventory |

The [v1.0.5 analysis release](https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.5) supplies the corrected `Analysis_Code.zip`. The [v1.0.6 figure release](https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.6) supplies `Figure_Code_and_Inputs.zip`, including the updated study chronology wording used by both manuscript versions.

The molecular starting points are GEO-deposited expression/count matrices and single-cell count triplets. Manifests retain source accessions, acquisition locations and SHA-256 hashes. Reference instructions identify the gene-set snapshot used for enrichment.

## Download and run

Use Python 3.11 or newer and choose a working path without spaces:

```bash
git clone https://github.com/Ab-code-inc/GEO-PERIO.git
cd GEO-PERIO
python3 download_reproduction.py --destination /path/to/work
```

The downloader retrieves and verifies the v1.0.1 snapshot. Extract `Analysis_Code.zip` from v1.0.5 into `/path/to/work/`, replacing its analytical code with the corrected version. Both archives use the `GEO_PERIO_Reproducibility/` root. Keep the v1.0.1 input data in place.

From `GEO_PERIO_Reproducibility/`, follow `environment/README.md` and `ANALYSIS_WORKFLOW.md`:

```bash
bash tools/install_environment.sh
source config/paths.sh
env/R/bin/Rscript code/R/pf26a_export_genesets_all.R
env/py/bin/python tools/check_genesets.py
env/py/bin/python tools/preflight.py
bash run_analysis.sh
bash run_derived_analyses.sh
```

The workflows build prepared matrices, cohort fits, meta-analyses, prediction results, cellular analyses, cross-disease comparisons and candidate classifications. The v1.0.5 release note documents the clinical-summary repair: single-cohort summaries retain the finite-degree-of-freedom probabilities from the fitted limma models. The primary replication criterion and cohort effects are unchanged.

## Reproduce the figures

Extract `Figure_Code_and_Inputs.zip` from v1.0.6 and enter `Figure_Reproduction/`:

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python reproduce_all.py
```

`FIGURE_INDEX.csv` maps seven main and twenty supplementary figures to their standalone generators. Each figure has exact embedded data, scientific Python plotting code and separate readable source tables. `SOURCE_TABLE_INDEX.csv` provides file hashes, and `PANEL_INPUT_MAP.csv` maps figures to their inputs. The anatomical illustrations are reproducible vector drawings made with Matplotlib.

Main Figures 1–6 cover the six results domains; Figure 7 integrates the findings in a detailed periodontal cutaway. Supplementary Figures 13, 14 and 16 provide the lesion, molecular-function and clinical-context detail. The `primary_source_audit/` directory links biological annotations to full primary papers and records the evidence-supported corrections. Independent checks cover gene assignments, donor proportions, clinical probabilities and 192 module effects.

The same curated set supports *Periodontitis gene signatures retain predictive information and reveal shared inflammatory responses* and *Cellular remodelling and shared inflammation in the periodontitis transcriptome*. Earlier releases preserve the preceding versions.

## Citation

Cite the study, the [v1.0.1 starting-data release](https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.1), the [v1.0.5 corrected analysis release](https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.5) and the [v1.0.6 figure release](https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.6). GEO accessions and source-study identifiers are retained in the manifests.
