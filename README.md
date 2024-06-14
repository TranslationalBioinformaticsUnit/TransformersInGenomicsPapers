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
* 💡: Pretrained Model
* 🔍: Peer-reviewed
## Single-Cell Genomics (SCG) Models
Papers that utilize Transformer models to analyze single-cell genomic data.

### Original Papers
| 🧠 Model        | 📄 Paper           | 💻 Code | 🛠️ Architecture        | 🌟 Highlights/Main Focus                         | 🧬 No. of Cells | 📊 No. of Datasets | 🎯 Loss Function(s)       | 📝 Downstream Tasks/Evaluations        |
|-----------------|---------------------|---------|--------------------------|-------------------------------------------------|----------------|-------------------|--------------------------|---------------------------------------|
| scFoundation💡🔍   | [Large-scale foundation model on single-cell transcriptomics](https://www.nature.com/articles/s41592-024-02305-7). Minsheng Hao et al. _Nature Methods_ (2024)         | [GitHub Repository](https://github.com/biomap-research/scFoundation)        | Transformer encoder, Performer decoder | Foundation model for single-cell analysis, built on xTrimoGene architecture with a read-depth-aware (RDA) pretraining across 50 million profiles | 50 million | 7 | Mean square error loss | Cell clustering; Cell type annotation; Perturbation prediction; Drug response prediction |
| scGPT 💡🔍          | [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](https://www.nature.com/articles/s41592-024-02201-0). Haotian Cui et al. _Nature Methods_ (2024) |  [GitHub Repository](https://github.com/bowang-lab/scGPT)       | Transformer | A foundation model designed for single-cell multi-omics aimed to deepen the understanding of biological data and improve performance in tasks like cell type annotation and integration. | 33 million | 441 | Mean square error; Cosine similarity; Cross entropy loss | Cell type annotation; Perturbation response prediction; Multi-batch integration; Multi-omic integration; Gene regulatory network inference |
| MarsGT 🔍         | [MarsGT: Multi-omics analysis for rare population inference using single-cell graph transformer](https://www.nature.com/articles/s41467-023-44570-8). Xiaoying Wang et al. _Nature Communications_ (2024) | [GitHub Repository](https://github.com/OSU-BMBL/marsgt)        | Graph Transformer | Identifying rare cell populations in single-cell multi-omics, with superior performance and insights for early detection and therapeutic intervention strategies | 750k | 550 | KL divergence, cosign similarity, and regression loss | Construct enhancer gene regulatory networks |
| scGREAT 🔍        | [scGREAT: Transformer-based deep-language model for gene regulatory network inference from single-cell transcriptomics](https://www.sciencedirect.com/science/article/pii/S258900422400573X). Yuchen Wang et al. _iScience_ (2024) | [GitHub Repository](https://github.com/ChaozhongLiu/scGREAT?tab=readme-ov-file)        | Transformer | Inferencing Gene Regulatory Networks (GRN) from single-cell transcriptomics data and textual information about genes using a transformer-based model | 4k | 7 | Cross entropy loss | Gene Regulatory Network Inference |
| scMulan 💡🔍         | [scMulan: A Multitask Generative Pre-Trained Language Model for Single-Cell Analysis](https://link.springer.com/chapter/10.1007/978-1-0716-3989-4_57). Haiyang Bian et al. _Research in Computational Molecular Biology (RECOMB)_ (2024) | [GitHub Repository](https://github.com/SuperBianC/scMulan)        | Transformer | Generative multitask model for single-cell analysis, trained on 10 million cells. | 10 million | 5 | Cross entropy loss | Cell type annotation; Batch integration; Conditional cell generation |
| CellPLM 💡🔍        | [CellPLM: Pre-training of Cell Language Model Beyond Single Cells](https://openreview.net/pdf?id=BKXvPDekud). Hongzhi Wen et al. _International Conference on Learning Representations (ICLR)_ (2024) |       [GitHub Repository](https://github.com/OmicsML/CellPLM)   | Transformer | The framework marks the first of its kind, encoding inter-cell relations, harnessing spatially-resolved transcriptomic data, and adopts a decent prior distribution. | 9M scRNA-seq + 2M spatial | 3 | Masked language modeling with mean squared error loss | Zero-shot clustering; scRNA-seq denoising; Spatial transcriptomic imputation; Cell type annotation; Perturbation prediction |
| tGPT 💡🔍           | [Generative pretraining from large-scale transcriptomes for single-cell deciphering](https://www.sciencedirect.com/science/article/pii/S2589004223006132). Hongru Shen et al. _iScience_ (2023) | [GitHub Repository](https://github.com/deeplearningplus/tGPT)        | Transformer | Generative pretraining on 22.3 million single-cell transcriptomes aligns with established cell labels and states suitable for single-cell and bulk analysis. | 22.3 million | 4 | Cross entropy loss | Single-cell clustering; Inference of developmental lineage; Feature representation analysis of bulk tissues |
| TOSICA 🔍         | [Transformer for one stop interpretable cell type annotation](https://www.nature.com/articles/s41467-023-35923-4). Jiawei Chen et al. _Nature Communications_ (2023) | [GitHub Repository](https://github.com/JackieHanLab/TOSICA)        | Transformer | An efficient cell type annotator trained on scRNA-seq data shows high accuracy across diverse datasets and enables new cell type discovery. | 536k | 6 | Cross entropy loss | Cell type annotation; Data integration; Cell differentiation trajectory inference |
| Geneformer 💡🔍     | [Transfer learning enables predictions in network biology](https://www.nature.com/articles/s41586-023-06139-9). Christina V. Theodoris et al. _Nature_ (2023) | [Hugging Face Repository](https://huggingface.co/ctheodoris/Geneformer); [GitHub Repository](https://github.com/jkobject/geneformer)        | Transformer | Pre-trained on 30 million single-cell transcriptomes to enable context-specific predictions and identify therapeutic targets in network biology with limited data. | 30 million | 561 | Cross entropy loss | Chromatin dynamics prediction; Network dynamics prediction; Cell type annotation; Gene network analysis |
| STGRNS 🔍         | [STGRNS: an interpretable transformer-based method for inferring gene regulatory networks from single-cell transcriptomic data](https://academic.oup.com/bioinformatics/article/39/4/btad165/7099621). Jing Xu et al. _Bioinformatics_ (2023) | [GitHub Repository](https://github.com/zhanglab-wbgcas/STGRNS)        | Transformer | Focused on enhancing gene regulatory network inference from single-cell transcriptomic data using a proposed gene expression motif technique, applicable across various scRNA-seq data types. | 154K+ | 48 | Cross entropy loss | Gene regulatory networks inference |
| DeepMAPS 🔍       | [Single-cell biological network inference using a heterogeneous graph transformer](https://www.nature.com/articles/s41467-023-36559-0). Anjun Ma et al. _Nature Communications_ (2023) |  [GitHub Repository](https://github.com/OSU-BMBL/deepmaps)       | Graph Transformer | Infers biological networks from single-cell multi-omics data via a heterogeneous graph and a multi-head graph transformer, enhancing local and global context learning. | 199k | 17 | Mean squared error and KL divergence | Dimensionality reduction and cell clustering; Biological network construction |
| scBERT 💡🔍         | [scBERT as a large-scale pretrained deep language model for cell type annotation of single-cell RNA-seq data](https://www.nature.com/articles/s42256-022-00534-z). Fan Yang et al. _Nature Machine Intelligence_ (2022) | [GitHub Repository](https://github.com/TencentAILabHealthcare/scBERT)        | Transformer (BERT-based model) | A BERT-based model was pre-trained on large amounts of unlabeled scRNA-seq data for cell type annotation, demonstrating superior performance. | 1M | 10 | Cross entropy loss | Cell type annotation; Novel cell type prediction |
| scCLIP 💡🔍         | [scCLIP: Multi-modal Single-cell Contrastive Learning Integration Pre-training](https://openreview.net/pdf?id=KMtM5ZHxct). Lei Xiong et al. _Conference on Neural Information Processing Systems (NeurIPS) AI for Science Workshop_ (2023) | [GitHub Repository](https://github.com/jsxlei/scCLIP)        | Transformer | Introduced a multi-modal Transformer model with contrastive learning, optimized for single-cell ATAC-seq data by tokenizing genomic peaks | 377k | 2 | Cross entropy loss | Modality alignment |
| scMVP 🔍          | [A deep generative model for multi-view profiling of single-cell RNA-seq and ATAC-seq data](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-021-02595-6). Gaoyang Li et al. _Genome Biology_ (2022) | [GitHub Repository](https://github.com/bm2-lab/scMVP)        | Transformer + VAE | Introduces scMVP, a multi-modal deep generative model for processing single-cell RNA-seq and ATAC-seq data, addressing data sparsity and integration challenges. | 100k | 5 | Clustering consistency loss – similar to CycleGAN | Clustering; Imputation; Trajectory Inference |
| Enformer 🔍       | [Effective gene expression prediction from sequence by integrating long-range interactions](https://www.nature.com/articles/s41592-021-01252-x). Žiga Avsec et al. _Nature Methods_ (2021) | [Hugging Face Repository](https://huggingface.co/EleutherAI/enformer-preview); [GitHub Repository](https://github.com/lucidrains/enformer-pytorch)     | Transformer with attention layers | To improve gene expression prediction from DNA sequences by integrating long-range interactions, leveraging transformer architecture for better accuracy. | 254k | 2 | Poisson negative log-likelihood loss | Gene expression prediction; Variant effect prediction; Epigenetic state prediction |
| CIForm 🔍               | [CIForm as a Transformer-based model for cell-type annotation of large-scale single-cell RNA-seq data](https://academic.oup.com/bib/article/24/4/bbad195/7169137). Jing Xu et al. _Briefings in Bioinformatics_ (2023)    | [GitHub Repository](https://github.com/zhanglab-wbgcas/CIForm)       | Transformer               | Developed for cell-type annotation of large-scale single-cell RNA-seq data, aiming to overcome batch effects and efficiently process large datasets | 12 million      | 16                | Cross entropy loss       | Cell type annotation                  |
| TransCluster 🔍         | [TransCluster: A Cell-Type Identification Method for single-cell RNA-Seq data using deep learning based on transformer](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.1038919/full). Tao Song et al. _Frontiers Genetics_ (2022)          |  [GitHub Repository](https://github.com/Danica123/TransCluster)                    | Transformer               | Proposes TransCluster, combining linear discriminant analysis and a modified Transformer to enhance cell-type identification accuracy and robustness across various human tissue datasets | 51k              | 2                 | Cross entropy loss       | Cell type annotation                  |
| iSEEEK 💡🔍               | [A universal approach for integrating super large-scale single-cell transcriptomes by exploring gene rankings](https://pubmed.ncbi.nlm.nih.gov/35048121/). Hongru Shen et al. _Briefings in Bioinformatics_ (2022)      |  [GitHub Repository](https://github.com/lixiangchun/iSEEEK)     | Transformer               | Introduces iSEEEK, an approach for integrating super large-scale single-cell RNA sequencing data by exploring gene rankings of top-expressing genes and states suitable for single-cell and bulk analysis | 11.9M           | 60                | Cross entropy loss       | Cell clusters delineation; Marker genes identification; Cell developmental trajectory exploration; Cluster-specific gene-gene interaction modules exploration analysis of bulk tissues |
| Exceiver 💡             | [A single-cell gene expression language model](https://arxiv.org/abs/2210.14330). Connell et al. _arXiv_ (2022)                              |  [GitHub Repository](https://github.com/keiserlab/exceiver)                    | Transformer               | Introduced discrete noise masking for self-supervised learning on unlabeled datasets and developed a framework using scRNA-seq to enhance downstream tasks in gene regulation and phenotype prediction | 500k            | 1                 | Cross entropy loss + Mean square error | Drug response prediction              |
| xTrimoGene 💡🔍           | [xTrimoGene: An Efficient and Scalable Representation Learner for Single-Cell RNA-Seq Data](https://papers.nips.cc/paper_files/paper/2023/file/db68f1c25678f72561ab7c97ce15d912-Paper-Conference.pdf). Jing Gong et al. _Conference on Neural Information Processing Systems (NeurIPS)_ (2023) |  _Unpublished_    | Asymmetric encoder-decoder transformer | Introduced a transformer variant for scRNA-seq data, significantly reducing computational and memory usage while preserving accuracy, and developed tailored pre-trained models for single-cell data | 5 million       | -                 | Mean square error         | Cell type annotation; Perturbation response prediction; Synergistic drug combination prediction |
| Cell2Sentence 💡🔍        | [Cell2Sentence: Teaching Large Language Models the Language of Biology](https://www.biorxiv.org/content/10.1101/2023.09.11.557287v3). Daniel Levine et al. _International Conference on Machine Learning (ICLR)_ (2024)                        |  [GitHub Repository](https://github.com/vandijklab/cell2sentence-ft)                    | Transformer (GPT)         | A single and flexible framework for seamlessly integrating Large Language Models (LLMs), specifically GPT-2, into transcriptomics, leveraging widely-used LLM libraries | 40k              | 2                 | Cross entropy loss       | Unconditional cell generation; Conditional cell generation; Cell type prediction |
| GenePT 💡               | [GenePT: A Simple But Effective Foundation Model for Genes and Cells Built From ChatGPT](https://www.biorxiv.org/content/10.1101/2023.10.16.562533v2). Yiqun T. Chen & James Zou _bioRxiv_ (2023)       |  [GitHub Repository](https://github.com/yiqunchen/GenePT)                        | Transformer (GPT)         | Used NCBI text descriptions of individual genes with GPT-3.5 to generate gene embeddings then further leveraged on downstream tasks | 21k              | 10                | Cross entropy loss       | Gene property prediction; Batch integration; Cell type annotation |
| CellLM 💡               | [Large-Scale Cell Representation Learning via Divide-and-Conquer Contrastive Learning](https://arxiv.org/abs/2306.04371). Suyuan Zhao et al. _arXiv_ (2023)    |  [GitHub Repository](https://github.com/PharMolix/OpenBioMed)                | Performer Transformer     | Presented a novel divide-and-conquer contrastive learning strategy designed to decouple the batch size from GPU memory constraints in cell representation learning | 2M               | 2                 | Masked language modeling with cross-entropy loss, cell type discrimination with binary cross-entropy loss, and divide-and-conquer contrastive loss | Cell type annotation; Drug sensitivity prediction |
| scELMo 💡               | [scELMo: Embeddings from Language Models are Good Learners for Single-cell Data Analysis](https://www.biorxiv.org/content/10.1101/2023.12.07.569910v2). Tianyu Liu et al. _bioRxiv_ (2023)    | [GitHub Repository](https://github.com/HelloWorldLTY/scELMo)                     | Transformer (GPT)         | Extended the concept from GenePT and proposed a novel approach to leverage the advantages from Large Language Models (LLMs) to formalize a foundation model for single-cell data analysis | 69K              | 5                 | Cross entropy loss       | Cell clustering; Batch effect correction; Cell type annotation; Perturbation analysis |
| UCE 💡                  | [Universal Cell Embeddings: A Foundation Model for Cell Biology](https://www.biorxiv.org/content/10.1101/2023.11.28.568918v1). Yanay Rosen et al. _bioRxiv_ (2023)     | [GitHub Repository](https://github.com/snap-stanford/UCE)                     | Transformer          | Trained in a self-supervised learning fashion on a diverse corpus of cell atlas data encompassing humans and other species, this model offers a cohesive biological latent space capable of representing cells from any tissue or species, all without the need for manual data annotations | 36M              | 300               | Cross entropy loss       | Zero-shot embedding quality and clustering; Cell type organization; Zero-shot cell type alignment to Integrated Mega-scale Atlas (IMA) |
| CellFM 💡                  | [a large-scale foundation model pre-trained on transcriptomics of 100 million human cells](https://www.biorxiv.org/content/10.1101/2024.06.04.597369v1). Yuansong Zeng et al. _bioRxiv_ (2024)     | [GitHub Repository](https://github.com/biomedAI/CellFM)                     | Transformer          | CellFM, a  800-million-parameter single-cell model trained on ~100 million human cells, outperforming existing models in applications like cell annotation and gene function prediction | 100M              | 20               | Mean square error loss loss       |Cell type annotation; Pertubation prediction; Gene function predction |
| Nicheformer 💡           | [Nicheformer: A Foundation Model for Single-Cell and Spatial Omics](https://www.biorxiv.org/content/10.1101/2024.04.15.589472v1). Anna C. Schaar et al. _bioRxiv_ (2024)    | [GitHub Repository](https://github.com/theislab/nicheformer)                     | Transformer               | Transformer-based model that integrates over 110 million human and mouse cells, learning unified representations from dissociated and spatial transcriptomics for advanced analysis of cellular interactions and environments. | 110 million     | 180+      | Masked language modeling loss, Cross entropy loss | Spatial cell type, niche region label prediction; Neighborhood cell density prediction |
| CELLama 💡                | [CELLama: Foundation Model for Single Cell and Spatial Transcriptomics by Cell Embedding Leveraging Language Model Abilities](https://www.biorxiv.org/content/10.1101/2024.05.08.593094v1). Hongyoon Choi et al. _bioRxiv_ (2024)         | [GitHub Repository](https://github.com/portrai-io/CELLama)                     | Transformer               | CELLama leverages language models to transform scRNA-seq and spatial transcriptomics data into gene expression 'sentences,' facilitating advanced cellular analysis across diverse datasets | 536k+           | 4                 | Cosine similarity         | Cell typing; Integration              |
| LangCell 💡              | [LangCell: Language-Cell Pre-training for Cell Identity Understanding](https://arxiv.org/abs/2405.06708). Suyuan Zhao et al. _arXiv_ (2024)                          | [GitHub Repository](https://github.com/PharMolix/LangCell)                     |   Transformer                        | LangCell integrates single-cell data with natural language during pre-training enabling effective zero-shot, few-shot, and fine-tuning performance in cell identity understanding tasks | 27.5 million    | 4                 | Masked gene modeling, Cell-cell contrastive, Cell-text contrastive, and Cell-text matching losses | Novel cell type identification; Cell type annotation; Batch integration |
| GeneCompass 💡           | [GeneCompass: Deciphering Universal Gene Regulatory Mechanisms with Knowledge-Informed Cross-Species Foundation Model](https://www.biorxiv.org/content/10.1101/2023.09.26.559542v1). Xiaodong Yang et al. _bioRxiv_ (2023)                        |  [GitHub Repository](https://github.com/xCompass-AI/GeneCompass)                    |     Transformer                      | Cross-species foundation model pre-trained on over 120 million single-cell transcriptomes from humans and mice, integrating biological prior knowledge | 120 million     | 13                | Mean square error, Cross entropy loss | Cell type annotation; Gene regulatory network prediction; Drug dose response prediction |
| scTranslator 💡          | [A pre-trained large generative model for translating single-cell transcriptome to proteome](https://www.biorxiv.org/content/10.1101/2023.07.04.547619v2). Linjing Liu et al. _bioRxiv_ (2023)                          |  [GitHub Repository](https://github.com/TencentAILabHealthcare/scTranslator)                    | Transformer               | scTranslator, a pre-trained generative model inspired by NLP and genetic translation, enhances single-cell proteomics by generating multi-omics data from the transcriptome | 239k            | 76                | Mean square error         | Interaction inference; Cell clustering |
| scMoFormer 🔍            | [Single-Cell Multimodal Prediction via Transformers](https://dl.acm.org/doi/10.1145/3583780.3615061). Wenzhuo Tang et al. _ACM International Conference on Information and Knowledge Management (CIKM)_ (2023)                         |  [GitHub Repository](https://github.com/OmicsML/scMoFormer)                    | Transformer               | Transformer-based framework designed to leverage and model the interactions of multimodal single-cell data, incorporating external domain knowledge for enhanced performance | 146k             | 3                 | Mean square error loss    | Multimodal prediction                |
| scTransSort 💡🔍           | [scTransSort: Transformers for Intelligent Annotation of Cell Types by Gene Embeddings](https://www.mdpi.com/2218-273X/13/4/611). Linfang Jiao et al. _Biomolecules_ (2023)                         |  [GitHub Repository](https://github.com/jiaojiao-123/scTransSort)                    | Transformer               | Cell-type annotation using transformers, pre-trained on single-cell transcriptomics data | 185k            | 47                | Sparse Categorical Cross entropy | Cell type annotation                  |
| BioFormers              | [BioFormers: A Scalable Framework for Exploring Biostates using Transformers](https://www.biorxiv.org/content/10.1101/2023.11.29.569320v1). Siham Amara-Belgadi et al. _bioRxiv_ (2023)                          |  [GitHub Repository](https://github.com/BiostateAI/Bioformers-BERT)                     | Transformer               | Transformer-based unsupervised learning to model biological systems, defining a 'biostate' as a comprehensive vector of genomic, proteomic, and other biological markers | 8k               | 3                 | Cross entropy loss         | Genetic perturbation prediction; Gene network inference |
| MuSe-GNN 🔍              | [MuSe-GNN: Learning Unified Gene Representation From Multimodal Biological Graph Data](https://openreview.net/pdf?id=4UCktT9XZx). Tian Yu et al. _Conference on Neural Information Processing Systems (NeurIPS)_ (2023)         | [GitHub Repository](https://github.com/HelloWorldLTY/MuSe-GNN)                     | Graph-Transformer         | Multimodal Similarity Learning Graph Neural Network, for integrating multimodal biological data to uncover gene function similarities across diverse datasets | -                | 82                | Binary cross entropy, Cosine similarity, Noise contrastive estimation loss | Cell clusters delineation; Marker genes identification; Cell developmental trajectory exploration; Cluster-specific gene–gene interaction modules exploration analysis of bulk tissues |
| scFormer               | [scFormer: A Universal Representation Learning Approach for Single-Cell Data Using Transformers](https://www.biorxiv.org/content/10.1101/2022.11.20.517285v1). Haotian Cui et al. _bioRxiv_ (2022)                          | [GitHub Repository](https://github.com/bowang-lab/scFormer)                     | Transformer               | Transformer-based deep learning framework employing self-attention to jointly optimize unsupervised cell and gene embeddings | 27k              | 3                 | Cross entropy loss         | Integration; Perturbation prediction |
| scTT 🔍                  | [Representation Learning and Translation between the Mouse and Human Brain using a Deep Transformer Architecture](https://icml-compbio.github.io/icml-website-2020/2020/papers/WCBICML2020_paper_29.pdf). Minxing Pang & Jesper Tegnér. _International Conference on Machine Learning (ICML) Workshop on Computational Biology_ (2020)                              | _Unpublished_                     | Transformer               | Transformer-based architecture translates single-cell genomic data between mouse and human, with enhanced clustering accuracy | 170k             | 2                 | Mean square error          | Clustering; Alignment                 |




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


