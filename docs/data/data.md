---
layout: default
title: Data
permalink: /data
has_children: true
has_toc: false
---

# Data

## Description

In the subsections we describe the data that we provide for building models:

* Single cell phosphoproteomics data
  * Antibody mapping table
  * Cell line name conversion table
  * Cell line description table (FileID_table)
* Median intensities of the phosphoproteomics data
* Protein abundance data
  * Raw protein abundance
  * Relative protein abundance
* RNA sequencing data (RNA-seq), Copy Number Variation (CNV) data and Single Nucleotide Polymorphism (SNP) data

![Figure 1. Datasets provided for the challenge.](assets/images/overview/figure1.xml)
_Figure 1. Datasets provided for the challenge._

In the entire Challenge, we encourage participants to exploit the population average measurements (proteomic, transcriptomic, and genomic) to help in the predictions.

While we do not explicitly provide all of the literature data on the cell lines (genomics and transcriptomics are provided, and the proteomic and the single-cell signaling datasets are newly acquired), we welcome participants to use external resources (including drug sensitivity information) and prior knowledge (i.e. protein-protein interaction databases) in training and developing their methods. Previous DREAM Challenges have shown that leveraging the literature, domain knowledge, and external databases can improve model performance.

## Data contribution

The single-cell phosphoproteomics data and the proteomics data was provided by the [Bodenmiller group, University of Zurich](https://www.dqbm.uzh.ch/en/research/groups/bodenmiller.html) and [Picotti group, ETH Zurich](https://imsb.ethz.ch/research/picotti.html), respectively.
The RNA-seq, CNV, and SNP data are published data (Marcotte et al., 2016).

## Data usage

Data used for the leaderboard and validation phase were generated with mass cytometry.

## Conditions for use

These data are provided exclusively for use within the Single Cell Signaling in Breast Cancer Challenge.

Challenge participants must abide by the guiding principles for responsible research use and data handling within the Synapse Commons Platform as described in the Synapse Governance documents and by the [DREAM Challenges Official Rules](https://www.synapse.org/#!Synapse:syn10144147/wiki/448310).

**Publication embargo**: The use of Challenge data or Challenge results in a publication, presentation or preprint by Challenge participants is not permitted until the Parties have jointly published an overview paper on the results from the Single Cell Signaling in Breast Cancer Challenge and the best performing strategies used in the Challenge (the “Overview Paper”), unless the Overview Paper is not published within 2 years of the Challenge Launch. You will be contacted through your Synapse-affiliated email address when this condition has been met. This information will also be posted within the Single Cell Signaling in Breast Cancer Challenge project.

**Acknowledgement**: Challenge participants are permitted to use, publish and present the Challenge data and Challenge results, after publication of the Overview Paper or the 2-year embargo period, provided they acknowledge Attila Gabor, Marco Tognetti, Bernd Bodenmiller, Julio Saez-Rodriguez, Paola Picotti, and Sage Bionetworks as follows: “The Datasets used for the analyses described in this manuscript (or publication) were contributed by Attila Gabor and Marco Tognetti. They were obtained as part of the Single Cell Signaling in Breast Cancer Challenge through Synapse ID [synXXXX]”.

**Citations**: In recognition of the effort that the Contributing Study Investigators and their institutions have made in obtaining the data that were the basis for the Single Cell Signaling in Breast Cancer Challenge, publications and presentations using the Challenge data must cite the Overview Paper.

## Access

You must be registered to the challenge to access the data. **[Learn How to Participate](https://www.synapse.org/#!Synapse:syn20366914/wiki/594732)**

## References

* Marcotte, R., Sayad, A., Brown, K.R., Sanchez-Garcia, F., Reimand, J., Haider, M., Virtanen, C., Bradner, J.E., Bader, G.D., Mills, G.B., et al. (2016). Functional Genomic Landscape of Human Breast Cancer Drivers, Vulnerabilities, and Resistance. Cell 164, 293–309.
