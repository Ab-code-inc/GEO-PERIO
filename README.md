# GEO-PERIO

Scientific source data and figure reproduction for **Integrative analysis of periodontitis transcriptomes reveals shared tissue responses and limits of gene-level replication**.

The study combines published gene-expression claims with participant-aware reanalysis of public periodontitis transcriptomes, held-out prediction, cellular context and comparisons with other inflammatory diseases. The data preserve the distinction between strict replication, nominal support, exploratory candidate prioritisation and disease-specific evidence.

## Files

Download the versioned files from [release v1.0.0](https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.0). The release asset manifest records their exact names, byte sizes and SHA-256 checksums.

- `03_Source_Data.xlsx` contains source values for the main and supplementary figures and tables, with data dictionaries and source locations.
- `04_Supplementary_Data_01.xlsx` through `10_Supplementary_Data_07.xlsx` contain the seven supplementary workbooks.
- `11_Supplementary_Data_08.zip` through `13_Supplementary_Data_10.zip` contain the larger supplementary result tables and their documentation.
- `Figure_Reproduction_Public.zip` contains runnable code for seven main and twenty supplementary figures, their exact embedded inputs, separate readable source tables, column dictionaries and final figure files.

See [DATA_SCHEMA.md](DATA_SCHEMA.md) for the structure and interpretation of these files. Large scientific files are supplied as release assets so the Git checkout remains small.

To verify a download, place `SHA256SUMS` beside the downloaded release files and run `shasum -a 256 -c SHA256SUMS` on macOS or `sha256sum -c SHA256SUMS` on Linux. The command reports missing files if only part of the release was downloaded.

## Reproduce the figures

Extract `Figure_Reproduction_Public.zip`, enter its `Figure_Reproduction_Public` directory and use Python 3.12:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python reproduce_all.py --list
python reproduce_all.py --figure Figure_07
```

To rebuild all figures, run `python reproduce_all.py`. A single figure folder is also self-contained:

```bash
python figures/Figure_01/run.py --output reproduced/Figure_01
```

Each figure includes its input data in `embedded_data.py`. The runner verifies input hashes before plotting and writes generated files and an execution receipt within its output directory. The generators use Matplotlib. They require no network access or original project workspace after dependencies are installed. Arial is used when available, with DejaVu Sans as a fallback; font substitution can change typography.

These commands regenerate figures from saved scientific results. They do not rerun raw GEO preprocessing, cohort model fitting or the complete analytical pipeline. Source-data tables remain the appropriate reference for numerical values, correction families and interpretation. Successful figure reproduction does not independently validate every source publication or scientific claim.

## Citation and source attribution

Repository: [Ab-code-inc/GEO-PERIO](https://github.com/Ab-code-inc/GEO-PERIO). The release citation is: *GEO-PERIO: Scientific source data and figure reproduction*, version 1.0.0, https://github.com/Ab-code-inc/GEO-PERIO/releases/tag/v1.0.0 . Cite the associated article when citing scientific findings, and preserve the GEO accessions and publication identifiers when citing original studies.

See [RIGHTS_AND_ATTRIBUTION.md](RIGHTS_AND_ATTRIBUTION.md) for source attribution and reuse terms.
