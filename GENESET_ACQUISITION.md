# Exact gene-set references

The analysis used msigdbr 26.1.1 with MSigDB 2026.1. Its installed download helper pins [msigdb.2026.1.zip](https://zenodo.org/records/18968178/files/msigdb.2026.1.zip?download=1) with MD5 `512ba99c6827141a9d471972b812d4ac`. The package reads the collection RDS files from its R user cache.

The supplied Hallmark/Reactome table is byte-pinned. The full table includes additional collections with distinct upstream terms, including KEGG Legacy and BioCarta; it is acquired through the upstream distribution rather than redistributed in this project. Obtain access consistent with the [MSigDB terms](https://www.gsea-msigdb.org/gsea/msigdb_license_terms.jsp). With the recorded R environment installed, run from the project root:

```bash
source config/paths.sh
env/R/bin/Rscript code/R/pf26a_export_genesets_all.R
python3 tools/check_genesets.py
```

The exporter downloads the version pinned by msigdbr on its first use. Configured caches and temporary files stay inside this project. Expected broad table: `analysis/added/GENESETS_MSIGDB_ALL.tsv`, 69,679,926 bytes, SHA-256 `9356a6bd75b406e5027dd4d18e9169f72979ac39eca879c7404f0985895668cb`. Expected Hallmark/Reactome table: `analysis/added/GENESETS_HALLMARK_REACTOME.tsv`, 5,189,966 bytes, SHA-256 `e3e5726569d63ad0c500a6c045077cbf00a1b8da0aed162e7e7740df950adc1c`.

Preflight verifies both complete reference tables against their expected hashes. The exporters reuse existing reference tables. `GEO_PERIO_REFRESH_GENESETS=1` explicitly requests a new export; changes must still pass the recorded hash check to reproduce this analysis.
