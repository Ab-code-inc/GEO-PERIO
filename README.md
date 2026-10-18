# GEO-PERIO

Data and analysis code for **Cellular remodelling and shared inflammation in the periodontitis transcriptome**.

GEO-PERIO combines evaluation of published gene claims with cohort-level replication, predictive modelling, single-cell localisation, cross-disease comparisons and periodontal tissue biology.

## Data and code

The [v1.0.1 release](https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.1) supplies the starting inputs and workflows:

| Archive | Contents |
|---|---|
| `01_Bulk_GEO_Inputs.zip` | Expression/count matrices from 31 bulk GEO series and original files used for format conversion |
| `02_Primary_SingleCell_Inputs.zip` | Counts, barcodes and feature annotations for GSE164241 and GSE171213 |
| `03_Additional_SingleCell_Inputs.zip` | Counts, barcodes and feature annotations for GSE266897, GSE272774 and GSE283882 |
| `04_Reference_and_Study_Definitions.zip` | Sample and participant maps, cohort models, comparison definitions and reference annotations |
| `05_Corrected_Claim_Inputs.zip` | Corrected literature-derived records and source-study identifiers used to construct the claim inventory |
| `06_Analysis_Code.zip` | Python/R analysis scripts, software requirements, setup tools and workflow documentation |
| `07_Figure_Code_and_Inputs.zip` | The preceding figure-code set, preserved with the analytical release |

The molecular starting points are GEO-deposited expression/count matrices and single-cell count triplets. Cohort specifications identify the measurement scale and preparation route. File manifests record source accessions, download locations and SHA-256 hashes. Reference-data instructions identify the exact gene-set snapshot used for enrichment.

## Download

Use Python 3.11 or newer and choose a destination path without spaces:

```bash
git clone https://github.com/Ab-code-inc/GEO-PERIO.git
cd GEO-PERIO
python3 download_reproduction.py --destination /path/to/work
```

The downloader checks each archive and unpacks all components into `/path/to/work/GEO_PERIO_Reproducibility/`. `release-assets.json` and `SHA256SUMS` identify the files in this version. The downloader retrieves the v1.0.1 analysis snapshot. The revised figure set is supplied separately below.

## Run the analysis

From `GEO_PERIO_Reproducibility/`, follow `environment/README.md` to install or configure Python and R, and `ANALYSIS_WORKFLOW.md` for reference preparation and the ordered analysis commands:

```bash
bash tools/install_environment.sh
source config/paths.sh
env/R/bin/Rscript code/R/pf26a_export_genesets_all.R
env/py/bin/python tools/check_genesets.py
env/py/bin/python tools/preflight.py
bash run_analysis.sh
bash run_derived_analyses.sh
```

The main workflow builds prepared matrices, cohort fits, meta-analyses, prediction results, cellular analyses and cross-disease comparisons. The derived workflow produces the final candidate classifications and partial-conjunction analyses.

## Reproduce the figures

Download `Figure_Code_and_Inputs.zip` from the [v1.0.2 figure release](https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.2), extract it, and enter `Figure_Reproduction/`:

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python reproduce_all.py
```

`FIGURE_INDEX.csv` maps the seven main and twenty supplementary figures to their code. `SOURCE_TABLE_INDEX.csv` maps the separate source tables, and `PANEL_INPUT_MAP.csv` identifies the inputs and transformations for the 40 statistical main-figure panels. Each figure folder contains its exact embedded input data and can also run independently. Figures are generated with Matplotlib.

## Citation

Cite the study title, the [v1.0.1 analytical data/code release](https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.1), and the [v1.0.2 figure-code release](https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.2). GEO accessions and source-study identifiers are retained in the input manifests.

