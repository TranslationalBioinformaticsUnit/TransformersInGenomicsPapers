# Transformers In Genomics Papers
A curated repository of academic papers showcasing the use of Transformer models in genomics. This repository aims to guide researchers, data scientists, and enthusiasts in finding relevant literature and understanding the applications of Transformers in various genomic contexts.

## Table of Contents

1. [Single-Cell Genomics (SCG) Models](#single-cell-genomics-scg-models)
   - [Newly Introduced Methods](#newly-introduced-methods)
   - [Benchmarking Papers](#benchmarking-papers)
   - [Review/Perspective Papers](#reviewperspective-papers)

2. [DNA Models](#dna-models)
   - [Newly Introduced Methods](#newly-introduced-methods-1)
   - [Benchmarking Papers](#benchmarking-papers-1)
   - [Review/Perspective Papers](#reviewperspective-papers-1)

3. [Spatial Transcriptomics (ST) Models](#spatial-transcriptomics-st-models)
   - [Newly Introduced Methods](#newly-introduced-methods-2)
   - [Benchmarking Papers](#benchmarking-papers-2)
   - [Review/Perspective Papers](#reviewperspective-papers-2)

4. [Hybrids of SCG, DNA, and ST Models](#hybrids-of-scg-dna-and-st-models)
   - [Newly Introduced Methods](#newly-introduced-methods-3)
   - [Benchmarking Papers](#benchmarking-papers-3)
   - [Review/Perspective Papers](#reviewperspective-papers-3)

## Single-Cell Genomics (SCG) Models
Papers that utilize Transformer models to analyze single-cell genomic data.

### Newly Introduced Methods

| Model                    | Paper                                                                                                                                                     | Code                                                                   | Omic Modalities                                          | Pre-training Dataset                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Input Embedding                                                                                                                                                                                        | Architecture                                         | SSL Tasks                                                                                                                   | Supervised Tasks                                                                                                                                               | Zero-shot Tasks                                                                                    |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| scMulan                  | 📝[Bian et al. 2024](https://www.biorxiv.org/content/10.1101/2024.01.25.577152v1)                                                                         | [🔍Github](https://github.com/SuperBianC/scMulan/tree/main)            | scRNA-Seq                                                | 10M / cross-tissue, human ([hECA](https://www.sciencedirect.com/science/article/pii/S2589004222005892))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Not specified                                                                                                                                                                                          | Decoder                                              | Conditional cell generation                                                                                                 | cell type annotation, cell metadata annotation (both also used in training)                                                                                    | Batch integration                                                                                  |
| BioFormers               | 📝[Belgadi and Li et al. 2023](https://www.biorxiv.org/content/10.1101/2023.11.29.569320v1.full.pdf)                                                      | None                                                                   | scRNA-Seq                                                | 8K / single tissue, human ([PBMC](https://docs.scvi-tools.org/en/stable/api/reference/scvi.data.pbmc_dataset.html), [Adamson et al. 2016](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90546))                                                                                                                                                                                                                                                                                                                                                                                                      | Value categorization: value binning                                                                                                                                                                    | Encoder                                              | MLM with CE loss                                                                                                            | None                                                                                                                                                           | Cell clustering, gene expression imputation, genetic perturbation effect prediction, GRN inference |
### Benchmarking Papers

### Review/Perspective Papers


## DNA Models
Papers focused on the application of Transformer models in DNA sequence analysis.

### Newly Introduced Methods

### Benchmarking Papers

### Review/Perspective Papers

## Spatial Transcriptomics (ST) Models
Papers applying Transformer models to spatial transcriptomics data.

### Newly Introduced Methods

### Benchmarking Papers

### Review/Perspective Papers

## Hybrids of SCG, DNA, and ST Models
Papers that combine approaches and modalities from SCG, DNA, and ST using Transformers.

### Newly Introduced Methods

### Benchmarking Papers

### Review/Perspective Papers


