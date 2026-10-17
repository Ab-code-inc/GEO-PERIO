# Reference data attribution and use terms

GEO records and deposited data are attributed through their accession links in `INPUT_FILES.csv`. NCBI places no restrictions of its own on use or distribution of GEO data; original submitters may retain rights that NCBI cannot transfer. Attribute the original studies and accessions and retain applicable source terms: [NCBI GEO disclaimer](https://www.ncbi.nlm.nih.gov/geo/info/disclaimer.html).

The frozen HGNC data are released under CC0. Attribute HGNC (RRID:SCR_002827), *Genenames.org: the HGNC resources in 2023*, and the [HGNC licence statement](https://www.genenames.org/about/license/).

MSigDB data are copyright 2004–2026 Broad Institute, Inc., Massachusetts Institute of Technology, and Regents of the University of California. The supplied Hallmark/Reactome membership table is a three-column export (`collection`, `set`, `symbol`) under CC BY 4.0. Retain this attribution and the [MSigDB terms](https://www.gsea-msigdb.org/gsea/msigdb_license_terms.jsp).

The broad reference is acquired separately through the upstream distribution. Follow [GENESET_ACQUISITION.md](GENESET_ACQUISITION.md) for the pinned version, retrieval commands and expected checksum. Ordinary MSigDB collections follow CC BY 4.0. KEGG MEDICUS follows CC BY-SA 4.0 and retains copyright 2009–2023 Kanehisa Laboratories. KEGG LEGACY retains copyright 1995–2017 Kanehisa Laboratories and the additional [KEGG policies](https://www.kegg.jp/kegg/docs/plea.html). BioCarta retains copyright 2000–2017 BioCarta and its [disclaimer](https://data.broadinstitute.org/gsea-msigdb/msigdb/biocarta/biocarta_disclaimer_of_liability_and_of_warranties.txt). Acquisition, use and redistribution follow each collection's linked terms and applicable permissions.

The broad analysis uses H, KEGG LEGACY, KEGG MEDICUS, Reactome, WikiPathways, BioCarta, PID, GO biological process/cellular component/molecular function, C8 and TFT:GTRD. The workflow verifies the complete export against its pinned checksum before analysis.

Upstream terms apply to their respective reference datasets. Licensing of the authored code and curated records is handled separately. Literature inputs consist of curated study records and bibliographic references in `extraction/STUDY_CITATIONS.tsv`.
