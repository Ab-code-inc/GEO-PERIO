# Analysis input data

The scientific pipeline starts from GEO-deposited expression values, gene-count matrices, cohort definitions and curated literature claims. For microarray and processed RNA-seq cohorts, the starting matrices incorporate preprocessing performed by the source submitters. Single-cell inputs contain gene-by-cell counts, feature annotations and barcodes.

All input archives extract into one `GEO_PERIO_Reproducibility` directory. Keep this directory layout. `INPUT_FILES.csv` records each supplied input's package path, source identity, byte count, SHA-256 checksum, measurement level and packaging transformation. `environment/GENESET_REFERENCE_HASHES.json` identifies the exact gene-set references; [GENESET_ACQUISITION.md](GENESET_ACQUISITION.md) gives retrieval instructions for the broader reference acquired separately. The workflow checks these references against their recorded SHA-256 hashes.

| Location | Data unit and interpretation |
|---|---|
| `data/geo/GSE*/` | Deposited or format-assembled bulk expression matrices, original conversion archives and single-cell count inputs. Values include raw counts, array intensities, TPM, RPKM and normalized counts. The cohort specification and scientific notes identify the measurement scale and preparation route for each input. |
| `data/sc_added/` | Additional deposited gene-by-cell count matrices, feature tables and cell barcodes used for contextual single-cell analyses. |
| `data/cohorts/specs/*.json` | Cohort/contrast model definitions: accession, assay class, matrix filename, case/reference labels, covariates, participant exclusions, recruitment family and analysis role. `*_QC` specifications are sensitivity models that reuse the corresponding base matrix/sample map. |
| `data/cohorts/maps/*.samples.tsv` | Specimen-to-participant/condition maps, inclusion flags and available covariates. GSM and study participant codes are public source identifiers. A participant can contribute multiple specimens; the specification controls aggregation and paired modelling. Blank covariates indicate unavailable metadata. |
| `data/cohorts/SYNTHESIS_PLAN.json` | Cohort/contrast/recruitment-family membership for each synthesis and sensitivity analysis. |
| `data/cohorts/RECRUITMENT_FAMILY_MAP.tsv` and `RECRUITMENT_FAMILY_EDGES.tsv` | Accession-to-recruitment-family map and supporting relations used to identify dependent cohorts. The map also includes accessions appearing in source-study claims. |
| `data/curation/candidate_rules.json` and `data/curation/candidate_source_evidence.json` | Source properties and classification gates for the final candidate analysis: endpoint modality, comparison, gene identity, direction and source validation. Source-study identifiers resolve through `extraction/STUDY_CITATIONS.tsv`. |
| `data/cohorts/PROBE_MAP_SOURCES.tsv` | Pinned microarray probe annotation file and checksum for each applicable cohort. |
| `data/geo/platforms/` | GEO platform annotation inputs, the original GPL21827 table and the frozen custom GPL21827 probe map. Optional regeneration of the custom map uses the documented GENCODE reference. |
| `env/reference/hgnc_complete_set.json` | Frozen HGNC gene-identifier reference. |
| `00_admin/sealed/GENE_TOKEN_KEY.tsv` | Gene-token-to-gene identity mapping consumed by the claim pipeline. |
| `singlecell/*/SAMPLES.tsv` | One row per deposited library: library/GSM, count-directory path, filename prefix, donor and condition. Paths are relative to the project root. |
| `singlecell/MARKERS_v1.tsv` | Fixed marker definitions used for cell-type annotation. |
| `singlecell/DATASET_ROLES.tsv` | Primary, evaluation and contextual role of each single-cell dataset. |
| `analysis/external/SELECTED_COHORTS_FINAL.tsv` | External disease-cohort selection, case/reference definitions, assay scale and independence evidence consumed downstream. |
| `analysis/external/EXTERNAL_FIT_STATUS.tsv` | Fixed external-cohort availability and measurement metadata consumed downstream. Historical fit fields describe the recorded source run. |
| `analysis/external/meta/GSE193677.gsm.txt` | GEO sample records used to map deposited count-column titles to GSM accessions during format conversion. |
| `extraction/final/*.json` | One corrected source-study family record containing curated signals, panels, reported statistics, dataset roles, clinical endpoints, eligibility flags and source uncertainties. |
| `extraction/STUDY_IDS.tsv` | The 449 source-study family identifiers used by the input completeness check. |
| `extraction/STUDY_CITATIONS.tsv` | Family/study identifier to bibliographic title, authors, year, journal and DOI mapping. Reading-record alternatives are retained where supplied by the source inventory. Blank PMID fields indicate missing metadata. |
| `extraction/RETRACTION_STATUS.tsv` | Source-study retraction status used by the sensitivity analysis. |
| `analysis/added/GENESETS_HALLMARK_REACTOME.tsv` | Frozen Hallmark/Reactome gene-set memberships (`collection`, `set`, `symbol`). |
| `analysis/added/GENESETS_MSIGDB_ALL.tsv` | Broader gene-set reference acquired separately using the documented version and expected SHA-256. |

## Claim-record fields

`family_id` and `study_ids` identify source records; `final_state` records the retained eligibility state. `study_design`, `datasets` and `own_cohorts` describe design, assay/tissue, participant counts and discovery/validation roles. `signals` contains gene or feature claims, direction, endpoint, reported statistics and source-level eligibility/uncertainty. `panels` contains panel members, coefficients when available, training/validation roles and reconstructability.

`native_result_tables`, `corrections_or_retractions` and `limitations` describe the source findings and their qualifications. `verification_tier` identifies the recorded source-check procedure. `source_uncertainties` retains the original scientific uncertainty content. Source-document locators use document basenames. Literature inputs comprise these curated records and the bibliographic references in `STUDY_CITATIONS.tsv`.

## Manifest columns

`package_path` is relative to the project root. `accession` identifies an upstream molecular series/platform when applicable. `upstream_record_url` links to the public source record; `recorded_download_url` retains a recorded acquisition URL where available. `bytes` and `sha256` describe the supplied file. `measurement_level` states what the observations or definitions represent. `transformation` distinguishes byte-preserved copies from portability/metadata projections. `upstream_source_ids` links curated study inputs to `STUDY_CITATIONS.tsv`.

The analytical workflow derives prepared matrices, fitted models and result tables from these starting inputs. The `figures/figure_reproduction/` subproject supplies the exact plotted values, separate source tables and code for rendering the figures.
