# jutils

Bioinformatics and phenotype analysis toolkit

## Installation

```bash
pip install jutils
```

Or install from source:

```bash
git clone https://github.com/imjiaoyuan/jutils.git
cd jutils
pip install -e .
```

## Commands

**Sequence Operations**

```bash
jutils seq extract -fa genome.fa -ids ids.txt -o output.fa
jutils seq rename -fa input.fa -map mapping.csv -o output.fa
jutils seq rename-by-gff -fa transcripts.fa -gff genes.gff -parent Parent -o output.fa
jutils seq translate -fa genome.fa -gff genes.gff -id ID -o proteins.fa
```

**Visualization**

```bash
jutils plot gene-structure -gff genes.gff -ids genes.txt -o gene_structure.png
jutils plot exon-structure -gff genes.gff -ids genes.txt -o exon_structure.png
jutils plot chromosome-map -gff genes.gff -o chromosome_map.png
jutils plot protein-domain -tsv domains.tsv -o protein_domains.png
jutils plot cis-element -bed elements.bed -o cis_elements.png
```

**Analysis Tools**

```bash
jutils analyze phylo-tree -fa sequences.fa -o tree.nwk -a nj
jutils analyze phylo-tree -fa sequences.fa -o tree.nwk -a ml
jutils analyze motif -fa promoters.fa -o motif_output -nmotifs 5
```

**Phenotype Image Analysis**

```bash
jutils pheno split-fruit -i fruit_image.jpg -o output_dir
jutils pheno split-fruit-raw -i fruit_image.jpg -o output_dir
jutils pheno split-leaf -i leaf_image.jpg -o output_dir
jutils pheno split-leaf-edge -i leaf_image.jpg -o output_dir
```