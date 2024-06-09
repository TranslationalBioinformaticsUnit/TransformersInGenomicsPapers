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

#### Legend
💡: Pretrained Model

## Single-Cell Genomics (SCG) Models
Papers that utilize Transformer models to analyze single-cell genomic data.

### Newly Introduced Methods
| 🧠 Model        | 📄 Paper           | 💻 Code | 🛠️ Architecture        | 🌟 Highlights/Main Focus                         | 🧬 No. of Cells | 📊 No. of Datasets | 🎯 Loss Function(s)       | 📝 Downstream Tasks/Evaluations        |
|-----------------|---------------------|---------|--------------------------|-------------------------------------------------|----------------|-------------------|--------------------------|---------------------------------------|
| scFoundation💡   |  Hao, M., Gong, J., Zeng, X. et al. [Large-scale foundation model on single-cell transcriptomics](https://www.nature.com/articles/s41592-024-02305-7) Nat Methods (2024).         |         | Transformer encoder, Performer decoder | Foundation model for single-cell analysis, built on xTrimoGene architecture with a read-depth-aware (RDA) pretraining across 50 million profiles | 50 million | 7 | Mean square error loss | Cell clustering; Cell type annotation; Perturbation prediction; Drug response prediction |
| scGPT 💡          | Haotian Cui et al., 2024 |         | Transformer | A foundation model designed for single-cell multi-omics aimed to deepen the understanding of biological data and improve performance in tasks like cell type annotation and integration. | 33 million | 441 | Mean square error; Cosine similarity; Cross entropy loss | Cell type annotation; Perturbation response prediction; Multi-batch integration; Multi-omic integration; Gene regulatory network inference |
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
| STGRNS                | Jing Xu et al., 2023                              |                      | Transformer               | Focused on inferring gene regulatory networks from single-cell transcriptomic data, proposing a gene expression motif technique to improve GRN inference accuracy across various scRNA-seq data types | 154K+           | 48                | Cross entropy loss       | Gene regulatory networks inference   |
| TransCluster          | Tao Song et al., 2022                             |                      | Transformer               | Proposes TransCluster, combining linear discriminant analysis and a modified Transformer to enhance cell-type identification accuracy and robustness across various human tissue datasets | 51k              | 2                 | Cross entropy loss       | Cell type annotation                  |
| iSEEEK                | Hongru Shen et al., 2022                          |                      | Transformer               | Introduces iSEEEK, an approach for integrating super large-scale single-cell RNA sequencing data by exploring gene rankings of top-expressing genes.and states suitable for single-cell and bulk analysis | 11.9M           | 60                | Cross entropy loss       | Cell clusters delineation; Marker genes identification; Cell developmental trajectory exploration; Cluster-specific gene–gene interaction modules exploration analysis of bulk tissues |
| Exceiver              | Connell et al., 2022                              |                      | Transformer               | Introduced discrete noise masking for self-supervised learning on unlabeled datasets and developed a framework using scRNA-seq to enhance downstream tasks in gene regulation and phenotype prediction | 500k            | 1                 | Cross entropy loss + Mean square error | Drug response prediction              |
| xTrimoGene            | Jing Gong et al., 2023                            |                      | Asymmetric encoder-decoder transformer | Introduced a transformer variant for scRNA-seq data, significantly reducing computational and memory usage while preserving accuracy, and developed tailored pre-trained models for single-cell data | 5 million       | -                 | Mean square error         | Cell type annotation; Perturbation response prediction; Synergistic drug combination prediction |
| CellPLM               | Hongzhi Wen et al., 2023                          |                      | Transformer               | The framework marks the first of its kind, encoding inter-cell relations, harnessing spatially-resolved transcriptomic data, and adopts a decent prior distribution | 9M scRNA-seq + 2M spatial | 3                 | Masked language modeling with mean squared error loss | Zero-shot clustering; scRNA-seq denoising; Spatial transcriptomic imputation; Cell type annotation; Perturbation prediction |
| scCLIP                | Lei Xiong et al., 2023                            |                      | Transformer               | Introduced a multi-modal Transformer model with contrastive learning, optimized for single-cell ATAC-seq data by tokenizing genomic peaks | 377k            | 2                 | Cross entropy loss       | Modality alignment                   |
| scFoundation          | Minsheng Hao et al., 2023                         |                      | Transformer encoder, Performer decoder | Foundation model for single-cell analysis, excelling in diverse tasks like gene expression enhancement, drug response prediction, and cellular perturbation forecasting with remarkable accuracy | 50M              | 7                 | Mean square error loss    | Gene expression enhancement; Drug response prediction on bulk data; Single-cell drug response classification; Single-cell perturbation prediction |
| Cell2Sentence         | Daniel Levine et al., 2023                        |                      | Transformer (GPT)         | A single and flexible framework for seamlessly integrating Large Language Models (LLMs), specifically GPT-2, into transcriptomics, leveraging widely used LLM libraries | 40k              | 2                 | Cross entropy loss       | Unconditional cell generation; Conditional cell generation; Cell type prediction |
| GenePT                | Yiqun T. Chen et al., 2023                        |                      | Transformer (GPT)         | Used NCBI text descriptions of individual genes with GPT-3.5 to generate gene embeddings then further leveraged on downstream tasks | 21k              | 10                | Cross entropy loss       | Gene property prediction; Batch integration; Cell type annotation |
| CellLM                | Suyuan Zhao et al., 2023                          |                      | Performer Transformer     | Presented a novel divide-and-conquer contrastive learning strategy designed to decouple the batch size from GPU memory constraints in cell representation learning | 2M               | 2                 | Masked language modeling with cross entropy loss, cell type discrimination with binary cross entropy loss, and divide-and-conquer contrastive loss | Cell type annotation; Drug sensitivity prediction |
| scELMo                | Tianyu Liu et al., 2023                           |                      | Transformer (GPT)         | Extended the concept from GenePT and proposeed a novel approach to leverage the advantages from Large Language Models (LLMs) to formalize a foundation model for single-cell data analysis | 69K              | 5                 | Cross entropy loss       | Cell clustering; Batch effect correction; Cell type annotation; Perturbation analysis |
| UCE                   | Yanay Rosen et al., 2023                          |                      | Transformer (GPT)         | Trained in a self-supervised learning fashion on a diverse corpus of cell atlas data encompassing humans and other species, this model offers a cohesive biological latent space capable of representing cells from any tissue or species, all without the need for manual data annotations | 36M              | 300               | Cross entropy loss       | Zero-shot embedding quality and clustering; Cell type organization; Zero-shot cell type alignment to Integrated Mega-scale Atlas (IMA) |
| scMulan               | Bian et al., 2024                                 |                      | Transformer               | A generative multitask model for single-cell analysis, trained on 10 million data points. scMulan enables zero-shot learning for cell type annotation and easy adaptation to new tasks through fine-tuning | 10M              | 5                 | Cross entropy loss       | Cell type annotation; Batch integration; Conditional cell generation |






### Benchmarking Papers
| 📄 Paper                                          | 💻 Code              | 🧠 Benchmarking Models           | 🌟 Main Focus                          | 📝 Results & Insights |
|---------------------------------------------------|----------------------|----------------------------------|----------------------------------------|-----------------------|
| [Single-cell analysis using transformers](#)      | [GitHub Link](#)     | [Benchmarking transformer models](#) | Improved cell type classification    | Standardized metrics |

### Review/Perspective Papers
| 📄 Paper                                          | 💻 Code              | 🌟 Highlights/Main Focus                          | 📝 Remarks & Conclusion                |
|---------------------------------------------------|----------------------|--------------------------------------------------|---------------------------------------|
| [Single-cell analysis using transformers](#)      | [GitHub Link](#)     | Improved cell type classification               | The paper demonstrates the effectiveness of transformer models in analyzing single-cell genomic data. It highlights significant improvements in cell type classification, making it a valuable tool for single-cell studies. The conclusion emphasizes the potential impact of transformer-based approaches in advancing our understanding of cellular heterogeneity and gene expression regulation. |

## DNA Models
Papers focused on the application of Transformer models in DNA sequence analysis.

### Newly Introduced Methods
| 🧠 Model               | 📄 Paper                                          | 💻 Code              | 🛠️ Architecture           | 🌟 Highlights/Main Focus                          | 🧬 No. of Cells | 📊 No. of Datasets | 🎯 Loss Function(s)       | 📝 Downstream Tasks/Evaluations        |
|------------------------|---------------------------------------------------|----------------------|---------------------------|--------------------------------------------------|-----------------|-------------------|--------------------------|---------------------------------------|
| DNA Transformer        | [Single-cell analysis using transformers](#)      | [GitHub Link](#)     | Transformer               | Improved cell type classification               | 10,000          | 5                 | Cross-Entropy            | Cell type classification, DE analysis |

### Benchmarking Papers
| 📄 Paper                                          | 💻 Code              | 🧠 Benchmarking Models           | 🌟 Main Focus                          | 📝 Results & Insights |
|---------------------------------------------------|----------------------|----------------------------------|----------------------------------------|-----------------------|
| [Single-cell analysis using transformers](#)      | [GitHub Link](#)     | [Benchmarking transformer models](#) | Improved cell type classification    | Standardized metrics |

### Review/Perspective Papers
| 📄 Paper                                          | 💻 Code              | 🌟 Highlights/Main Focus                          | 📝 Remarks & Conclusion                |
|---------------------------------------------------|----------------------|--------------------------------------------------|---------------------------------------|
| [Single-cell analysis using transformers](#)      | [GitHub Link](#)     | Improved cell type classification               | The paper demonstrates the effectiveness of transformer models in analyzing single-cell genomic data. It highlights significant improvements in cell type classification, making it a valuable tool for single-cell studies. The conclusion emphasizes the potential impact of transformer-based approaches in advancing our understanding of cellular heterogeneity and gene expression regulation. |

## Spatial Transcriptomics (ST) Models
Papers applying Transformer models to spatial transcriptomics data.

### Newly Introduced Methods
| 🧠 Model               | 📄 Paper                                          | 💻 Code              | 🛠️ Architecture           | 🌟 Highlights/Main Focus                          | 🧬 No. of Cells | 📊 No. of Datasets | 🎯 Loss Function(s)       | 📝 Downstream Tasks/Evaluations        |
|------------------------|---------------------------------------------------|----------------------|---------------------------|--------------------------------------------------|-----------------|-------------------|--------------------------|---------------------------------------|
| ST Transformer        | [Single-cell analysis using transformers](#)      | [GitHub Link](#)     | Transformer               | Improved cell type classification               | 10,000          | 5                 | Cross-Entropy            | Cell type classification, DE analysis |

### Benchmarking Papers
| 📄 Paper                                          | 💻 Code              | 🧠 Benchmarking Models           | 🌟 Main Focus                          | 📝 Results & Insights |
|---------------------------------------------------|----------------------|----------------------------------|----------------------------------------|-----------------------|
| [Single-cell analysis using transformers](#)      | [GitHub Link](#)     | [Benchmarking transformer models](#) | Improved cell type classification    | Standardized metrics |

### Review/Perspective Papers
| 📄 Paper                                          | 💻 Code              | 🌟 Highlights/Main Focus                          | 📝 Remarks & Conclusion                |
|---------------------------------------------------|----------------------|--------------------------------------------------|---------------------------------------|
| [Single-cell analysis using transformers](#)      | [GitHub Link](#)     | Improved cell type classification               | The paper demonstrates the effectiveness of transformer models in analyzing single-cell genomic data. It highlights significant improvements in cell type classification, making it a valuable tool for single-cell studies. The conclusion emphasizes the potential impact of transformer-based approaches in advancing our understanding of cellular heterogeneity and gene expression regulation. |

## Hybrids of SCG, DNA, and ST Models
Papers that combine approaches and modalities from SCG, DNA, and ST using Transformers.

### Newly Introduced Methods
| 🧠 Model               | 📄 Paper                                          | 💻 Code              | 🛠️ Architecture           | 🌟 Highlights/Main Focus                          | 🧬 No. of Cells | 📊 No. of Datasets | 🎯 Loss Function(s)       | 📝 Downstream Tasks/Evaluations        |
|------------------------|---------------------------------------------------|----------------------|---------------------------|--------------------------------------------------|-----------------|-------------------|--------------------------|---------------------------------------|
| Hybrid Transformer        | [Single-cell analysis using transformers](#)      | [GitHub Link](#)     | Transformer               | Improved cell type classification               | 10,000          | 5                 | Cross-Entropy            | Cell type classification, DE analysis |

### Benchmarking Papers
| 📄 Paper                                          | 💻 Code              | 🧠 Benchmarking Models           | 🌟 Main Focus                          | 📝 Results & Insights |
|---------------------------------------------------|----------------------|----------------------------------|----------------------------------------|-----------------------|
| [Single-cell analysis using transformers](#)      | [GitHub Link](#)     | [Benchmarking transformer models](#) | Improved cell type classification    | Standardized metrics |

### Review/Perspective Papers
| 📄 Paper                                          | 💻 Code              | 🌟 Highlights/Main Focus                          | 📝 Remarks & Conclusion                |
|---------------------------------------------------|----------------------|--------------------------------------------------|---------------------------------------|
| [Single-cell analysis using transformers](#)      | [GitHub Link](#)     | Improved cell type classification               | The paper demonstrates the effectiveness of transformer models in analyzing single-cell genomic data. It highlights significant improvements in cell type classification, making it a valuable tool for single-cell studies. The conclusion emphasizes the potential impact of transformer-based approaches in advancing our understanding of cellular heterogeneity and gene expression regulation. |


