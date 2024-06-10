# Transformers In Genomics Papers
A curated repository of academic papers showcasing the use of Transformer models in genomics. This repository aims to guide researchers, data scientists, and enthusiasts in finding relevant literature and understanding the applications of Transformers in various genomic contexts.

## Table of Contents

1. [Single-Cell Genomics (SCG) Models](#single-cell-genomics-scg-models)
   - [Original Papers](#original-papers)
   - [Benchmarking Papers](#benchmarking-papers)
   - [Review/Perspective Papers](#reviewperspective-papers)

2. [DNA Models](#dna-models)
   - [Original Papers](#original-papers-1)
   - [Benchmarking Papers](#benchmarking-papers-1)
   - [Review/Perspective Papers](#reviewperspective-papers-1)

3. [Spatial Transcriptomics (ST) Models](#spatial-transcriptomics-st-models)
   - [Original Papers](#original-papers-2)
   - [Benchmarking Papers](#benchmarking-papers-2)
   - [Review/Perspective Papers](#reviewperspective-papers-2)

4. [Hybrids of SCG, DNA, and ST Models](#hybrids-of-scg-dna-and-st-models)
   - [Original Papers](#original-papers-3)
   - [Benchmarking Papers](#benchmarking-papers-3)
   - [Review/Perspective Papers](#reviewperspective-papers-3)

#### Legend
💡: Pretrained Model

## Single-Cell Genomics (SCG) Models
Papers that utilize Transformer models to analyze single-cell genomic data.

### Original Papers
| 🧠 Model        | 📄 Paper           | 💻 Code | 🛠️ Architecture        | 🌟 Highlights/Main Focus                         | 🧬 No. of Cells | 📊 No. of Datasets | 🎯 Loss Function(s)       | 📝 Downstream Tasks/Evaluations        |
|-----------------|---------------------|---------|--------------------------|-------------------------------------------------|----------------|-------------------|--------------------------|---------------------------------------|
| scFoundation💡   | [Large-scale foundation model on single-cell transcriptomics](https://www.nature.com/articles/s41592-024-02305-7). Minsheng Hao et al. Nature Methods (2024).         | [GitHub Page](https://github.com/biomap-research/scFoundation)        | Transformer encoder, Performer decoder | Foundation model for single-cell analysis, built on xTrimoGene architecture with a read-depth-aware (RDA) pretraining across 50 million profiles | 50 million | 7 | Mean square error loss | Cell clustering; Cell type annotation; Perturbation prediction; Drug response prediction |
| scGPT 💡          | [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](https://www.nature.com/articles/s41592-024-02201-0). Haotian Cui et al. Nature Methods (2024) |  [GitHub Page](https://github.com/bowang-lab/scGPT)       | Transformer | A foundation model designed for single-cell multi-omics aimed to deepen the understanding of biological data and improve performance in tasks like cell type annotation and integration. | 33 million | 441 | Mean square error; Cosine similarity; Cross entropy loss | Cell type annotation; Perturbation response prediction; Multi-batch integration; Multi-omic integration; Gene regulatory network inference |
| MarsGT          | Xiaoying Wang et al., 2024 |         | Graph Transformer | Identifying rare cell populations in single-cell multi-omics, with superior performance and insights for early detection and therapeutic intervention strategies | 750k | 550 | KL divergence, cosign similarity, and regression loss | Construct enhancer gene regulatory networks |
| scGREAT         | Yuchen Wang et al., 2024 |         | Transformer | Inferencing Gene Regulatory Networks (GRN) from single-cell transcriptomics data and textual information about genes using a transformer-based model | 4k | 7 | Cross entropy loss | Gene Regulatory Network Inference |
| scMulan 💡         | Bian et al., 2024 |         | Transformer | Generative multitask model for single-cell analysis, trained on 10 million cells. | 10 million | 5 | Cross entropy loss | Cell type annotation; Batch integration; Conditional cell generation |
| CellPLM 💡        | Hongzhi Wen et al., 2023 |         | Transformer | The framework marks the first of its kind, encoding inter-cell relations, harnessing spatially-resolved transcriptomic data, and and adopts a decent prior distribution. | 9M scRNA-seq + 2M spatial | 3 | Masked language modeling with mean squared error loss | Zero-shot clustering; scRNA-seq denoising; Spatial transcriptomic imputation; Cell type annotation; Perturbation prediction |
| tGPT 💡           | Hongru Shen et al., 2023 |         | Transformer | Generative pretraining on 22.3 million single-cell transcriptomes aligns with established cell labels and states suitable for single-cell and bulk analysis. | 22.3 million | 4 | Cross entropy loss | Single-cell clustering; Inference of developmental lineage; Feature representation analysis of bulk tissues |
| TOSICA          | Jiawei Chen et al., 2023 |         | Transformer | An efficient cell type annotator trained on scRNA-seq data shows high accuracy across diverse datasets and enables new cell type discovery. | 536k | 6 | Cross entropy loss | Cell type annotation; Data integration; Cell differentiation trajectory inference |
| Geneformer 💡     | Theodoris et al., 2023 |         | Transformer | Pre-trained on 30 million single-cell transcriptomes to enable context-specific predictions and identify therapeutic targets in network biology with limited data. | 30 million | 561 | Cross entropy loss | Chromatin dynamics prediction; Network dynamics prediction; Cell type annotation; Gene network analysis |
| STGRNS          | Jing Xu et al., 2023 |         | Transformer | Focused on enhancing gene regulatory network inference from single-cell transcriptomic data using a proposed gene expression motif technique, applicable across various scRNA-seq data types. | 154K+ | 48 | Cross entropy loss | Gene regulatory networks inference |
| DeepMAPS        | Anjun Ma et al., 2023 |         | Graph Transformer | Infers biological networks from single-cell multi-omics data via a heterogeneous graph and a multi-head graph transformer, enhancing local and global context learning. | 199k | 17 | Mean squared error and KL divergence | Dimensionality reduction and cell clustering; Biological network construction |
| scBERT 💡         | Fan Yang et al., 2022 |         | Transformer (BERT- based model) | A BERT-based model was pre-trained on large amounts of unlabeled scRNA-seq data for cell type annotation, demonstrating superior performance. | 1M | 10 | Cross entropy loss | Cell type annotation; Novel cell type prediction |
| scCLIP 💡         | Lei Xiong et al., 2023 |         | Transformer | Introduced a multi-modal Transformer model with contrastive learning, optimized for single-cell ATAC-seq data by tokenizing genomic peaks | 377k | 2 | Cross entropy loss | Modality alignment |
| scMVP           | Gaoyang Li et al., 2022 |         | Transformer + VAE | Introduces scMVP, a multi-modal deep generative model for processing single-cell RNA-seq and ATAC-seq data, addressing data sparsity and integration challenges. | 100k | 5 | Clustering consistency loss – similar to CycleGAN | Clustering; Imputation; Trajectory Inference |
| Enformer        | Žiga Avsec et al., 2021 |         | Transformer with attention layers | To improve gene expression prediction from DNA sequences by integrating long-range interactions, leveraging transformer architecture for better accuracy. | 254k | 2 | Poisson negative log-likelihood loss | Gene expression prediction; Variant effect prediction; Epigenetic state prediction |
| CIForm                | Jing Xu et al., 2023                              |                      | Transformer               | Developed for cell-type annotation of large-scale single-cell RNA-seq data, aiming to overcome batch effects and efficiently process large datasets | 12 million      | 16                | Cross entropy loss       | Cell type annotation                  |
| TransCluster          | Tao Song et al., 2022                             |                      | Transformer               | Proposes TransCluster, combining linear discriminant analysis and a modified Transformer to enhance cell-type identification accuracy and robustness across various human tissue datasets | 51k              | 2                 | Cross entropy loss       | Cell type annotation                  |
| iSEEEK 💡               | Hongru Shen et al., 2022                          |                      | Transformer               | Introduces iSEEEK, an approach for integrating super large-scale single-cell RNA sequencing data by exploring gene rankings of top-expressing genes.and states suitable for single-cell and bulk analysis | 11.9M           | 60                | Cross entropy loss       | Cell clusters delineation; Marker genes identification; Cell developmental trajectory exploration; Cluster-specific gene–gene interaction modules exploration analysis of bulk tissues |
| Exceiver 💡             | Connell et al., 2022                              |                      | Transformer               | Introduced discrete noise masking for self-supervised learning on unlabeled datasets and developed a framework using scRNA-seq to enhance downstream tasks in gene regulation and phenotype prediction | 500k            | 1                 | Cross entropy loss + Mean square error | Drug response prediction              |
| xTrimoGene 💡           | Jing Gong et al., 2023                            |                      | Asymmetric encoder-decoder transformer | Introduced a transformer variant for scRNA-seq data, significantly reducing computational and memory usage while preserving accuracy, and developed tailored pre-trained models for single-cell data | 5 million       | -                 | Mean square error         | Cell type annotation; Perturbation response prediction; Synergistic drug combination prediction |
| Cell2Sentence 💡        | Daniel Levine et al., 2023                        |                      | Transformer (GPT)         | A single and flexible framework for seamlessly integrating Large Language Models (LLMs), specifically GPT-2, into transcriptomics, leveraging widely used LLM libraries | 40k              | 2                 | Cross entropy loss       | Unconditional cell generation; Conditional cell generation; Cell type prediction |
| GenePT 💡               | Yiqun T. Chen et al., 2023                        |                      | Transformer (GPT)         | Used NCBI text descriptions of individual genes with GPT-3.5 to generate gene embeddings then further leveraged on downstream tasks | 21k              | 10                | Cross entropy loss       | Gene property prediction; Batch integration; Cell type annotation |
| CellLM 💡               | Suyuan Zhao et al., 2023                          |                      | Performer Transformer     | Presented a novel divide-and-conquer contrastive learning strategy designed to decouple the batch size from GPU memory constraints in cell representation learning | 2M               | 2                 | Masked language modeling with cross entropy loss, cell type discrimination with binary cross entropy loss, and divide-and-conquer contrastive loss | Cell type annotation; Drug sensitivity prediction |
| scELMo 💡               | Tianyu Liu et al., 2023                           |                      | Transformer (GPT)         | Extended the concept from GenePT and proposeed a novel approach to leverage the advantages from Large Language Models (LLMs) to formalize a foundation model for single-cell data analysis | 69K              | 5                 | Cross entropy loss       | Cell clustering; Batch effect correction; Cell type annotation; Perturbation analysis |
| UCE 💡                  | Yanay Rosen et al., 2023                          |                      | Transformer (GPT)         | Trained in a self-supervised learning fashion on a diverse corpus of cell atlas data encompassing humans and other species, this model offers a cohesive biological latent space capable of representing cells from any tissue or species, all without the need for manual data annotations | 36M              | 300               | Cross entropy loss       | Zero-shot embedding quality and clustering; Cell type organization; Zero-shot cell type alignment to Integrated Mega-scale Atlas (IMA) |
| Nicheformer            | Anna C. et al., 2024                              |                      | Transformer               | Transformer-based model that integrates over 110 million human and mouse cells, learning unified representations from dissociated and spatial transcriptomics for advanced analysis of cellular interactions and environments. | 110 million     | 180+              | Masked language modeling loss, Cross entropy loss | Spatial cell type, niche region label prediction; Neighborhood cell density prediction |
| CELLama                | Hongyoon Choi et al., 2024                        |                      | Transformer               | CELLama leverages language models to transform scRNA-seq and spatial transcriptomics data into gene expression 'sentences,' facilitating advanced cellular analysis across diverse datasets | 536k+           | 4                 | Cosine similarity         | Cell typing; Integration              |
| scELMo                 | Tianyu Liu et al., 2024                           |                      | Transformer (GPT)         | Extended the concept from GenePT and proposed a novel approach to leverage the advantages from Large Language Models (LLMs) to formalize a foundation model for single-cell data analysis | 69k              | 5                 | Cross entropy loss       | Cell clustering; Batch effect correction; Cell type annotation; Perturbation analysis |
| LangCell               | Suyuan Zhao et al., 2024                          |                      |                           | LangCell integrates single-cell data with natural language during pre-training enabling effective zero-shot, few-shot, and fine-tuning performance in cell identity understanding tasks | 27.5 million    | 4                 | Masked gene modeling, Cell-cell contrastive, Cell-text contrastive, and Cell-text matching losses | Novel cell type identification; Cell type annotation; Batch integration |
| GeneCompass            | Xiaodong Yang et al., 2023                        |                      |                           | Cross-species foundation model pre-trained on over 120 million single-cell transcriptomes from humans and mice, integrating biological prior knowledge | 120 million     | 13                | Mean square error, Cross entropy loss | Cell type annotation; Gene regulatory network prediction; Drug dose response prediction |
| scTranslator           | Linjing Liu et al., 2023                          |                      | Transformer               | scTranslator, a pre-trained generative model inspired by NLP and genetic translation, enhances single-cell proteomics by generating multi-omics data from the transcriptome | 239k            | 76                | Mean square error         | Interaction inference; Cell clustering |
| scMoFormer             | Wenzhuo Tang et al., 2023                         |                      | Transformer               | Transformer-based framework designed to leverage and model the interactions of multimodal single-cell data, incorporating external domain knowledge for enhanced performance | 146k             | 3                 | Mean square error loss    | Multimodal prediction                |
| scTransSort            | Linfang Jiao et al., 2023                         |                      | Transformer               | Cell-type annotation using transformers, pre-trained on single-cell transcriptomics data | 185k            | 47                | Sparse Categorical Cross entropy | Cell type annotation                  |
| BioFormer              | Siham Amara et al., 2023                          |                      | Transformer               | Transformer-based unsupervised learning to model biological systems, defining a 'biostate' as a comprehensive vector of genomic, proteomic, and other biological markers | 8k               | 3                 | Cross entropy loss         | Genetic perturbation prediction; Gene network inference |
| MuSe-GNN               | Tian Yu et al., 2023                              |                      | Graph-Transformer         | Multimodal Similarity Learning Graph Neural Network, for integrating multimodal biological data to uncover gene function similarities across diverse datasets | -                | 82                | Binary cross entropy, Cosine similarity, Noise contrastive estimation loss | Cell clusters delineation; Marker genes identification; Cell developmental trajectory exploration; Cluster-specific gene–gene interaction modules exploration analysis of bulk tissues |
| scFormer               | Haotian Cui et al., 2022                          |                      | Transformer               | Transformer-based deep learning framework employing self-attention to jointly optimize unsupervised cell and gene embeddings | 27k              | 3                 | Cross entropy loss         | Integration; Perturbation prediction |
| scTT                   | Minxing et al., 2020                              |                      | Transformer               | Transformer-based architecture translates single-cell genomic data between mouse and human, with enhanced clustering accuracy | 170k             | 2                 | Mean square error          | Clustering; Alignment                 |




### Benchmarking Papers
| 📄 Paper                                          | 💻 Code              | 🧠 Benchmarking Models           | 🌟 Main Focus                          | 📝 Results & Insights |
|---------------------------------------------------|----------------------|----------------------------------|----------------------------------------|-----------------------|
| [x](#)      | [x](#)     | [x](#) | x    | x |

### Review/Perspective Papers
| 📄 Paper                                          | 💻 Code              | 🌟 Highlights/Main Focus                          | 📝 Remarks & Conclusion                |
|---------------------------------------------------|----------------------|--------------------------------------------------|---------------------------------------|
| [x](#)      | [x](#)     | x               | x |

## DNA Models
Papers focused on the application of Transformer models in DNA sequence analysis.

### Original Papers
| 🧠 Model               | 📄 Paper                                          | 💻 Code              | 🛠️ Architecture           | 🌟 Highlights/Main Focus                          | 🧬 No. of Cells | 📊 No. of Datasets | 🎯 Loss Function(s)       | 📝 Downstream Tasks/Evaluations        |
|------------------------|---------------------------------------------------|----------------------|---------------------------|--------------------------------------------------|-----------------|-------------------|--------------------------|---------------------------------------|
| x        | [x](#)      | [x](#)     | x               |x               | x          | x              | x          | x |

### Benchmarking Papers
| 📄 Paper                                          | 💻 Code              | 🧠 Benchmarking Models           | 🌟 Main Focus                          | 📝 Results & Insights |
|---------------------------------------------------|----------------------|----------------------------------|----------------------------------------|-----------------------|
| [x](#)      | [x](#)     | [x](#) | x    | x |

### Review/Perspective Papers
| 📄 Paper                                          | 💻 Code              | 🌟 Highlights/Main Focus                          | 📝 Remarks & Conclusion                |
|---------------------------------------------------|----------------------|--------------------------------------------------|---------------------------------------|
| [x](#)      | [x](#)     | x               | x |

## Spatial Transcriptomics (ST) Models
Papers applying Transformer models to spatial transcriptomics data.

### Original Papers
| 🧠 Model               | 📄 Paper                                          | 💻 Code              | 🛠️ Architecture           | 🌟 Highlights/Main Focus                          | 🧬 No. of Cells | 📊 No. of Datasets | 🎯 Loss Function(s)       | 📝 Downstream Tasks/Evaluations        |
|------------------------|---------------------------------------------------|----------------------|---------------------------|--------------------------------------------------|-----------------|-------------------|--------------------------|---------------------------------------|
| x        | [x](#)      | [x](#)     | x               |x               | x          | x              | x          | x |

### Benchmarking Papers
| 📄 Paper                                          | 💻 Code              | 🧠 Benchmarking Models           | 🌟 Main Focus                          | 📝 Results & Insights |
|---------------------------------------------------|----------------------|----------------------------------|----------------------------------------|-----------------------|
| [x](#)      | [x](#)     | [x](#) | x    | x |

### Review/Perspective Papers
| 📄 Paper                                          | 💻 Code              | 🌟 Highlights/Main Focus                          | 📝 Remarks & Conclusion                |
|---------------------------------------------------|----------------------|--------------------------------------------------|---------------------------------------|
| [x](#)      | [x](#)     | x               | x |

## Hybrids of SCG, DNA, and ST Models
Papers that combine approaches and modalities from SCG, DNA, and ST using Transformers.

### Original Papers
| 🧠 Model               | 📄 Paper                                          | 💻 Code              | 🛠️ Architecture           | 🌟 Highlights/Main Focus                          | 🧬 No. of Cells | 📊 No. of Datasets | 🎯 Loss Function(s)       | 📝 Downstream Tasks/Evaluations        |
|------------------------|---------------------------------------------------|----------------------|---------------------------|--------------------------------------------------|-----------------|-------------------|--------------------------|---------------------------------------|
| x        | [x](#)      | [x](#)     | x               |x               | x          | x              | x          | x |

### Benchmarking Papers
| 📄 Paper                                          | 💻 Code              | 🧠 Benchmarking Models           | 🌟 Main Focus                          | 📝 Results & Insights |
|---------------------------------------------------|----------------------|----------------------------------|----------------------------------------|-----------------------|
| [x](#)      | [x](#)     | [x](#) | x    | x |

### Review/Perspective Papers
| 📄 Paper                                          | 💻 Code              | 🌟 Highlights/Main Focus                          | 📝 Remarks & Conclusion                |
|---------------------------------------------------|----------------------|--------------------------------------------------|---------------------------------------|
| [x](#)      | [x](#)     | x               | x |


