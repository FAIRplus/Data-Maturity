---
layout: default
title: Challenge Overview & Questions
permalink: /challenge-overview-and-questions
nav_order: 3
has_children: true
has_toc: false
---

## Overview
The aim of the DREAM Challenge is to identify the extent of the translation from cell lines to organoids. Thus, we present two subchallenges. The first one is focused on assessing how good cell line models approach the prediction of drug sensitivity in organoids using publicly available cell line data (CCLE, GDSC). The second subchallenge is focused on integrated new generated proteomic data from selected cell lines to predict drug response.

## Challenge dataset
The generated dataset comprises 13 organoids that have been treated with 209 different drugs. RNAseq data was obtained from the samples before treatment. The proteomic data from <span style="color:orange;font-weight:bold">N</span> selected cell lines comprises <span style="color:orange;font-weight:bold">N</span> proteins.

For more information about the data, see <span style="color:orange;font-weight:bold">here</span>.

## Challenge questions
Within the scope of the Challenge, we invite participants to provide drug sensitivity predictions for the two subchallenges:

1. [Subchallenge I](/docs/challenge_overview/subchallenges_i_iii/#subchallenge-i-predict-missing-markers-at-the-single-cell-level): The Challenge consists of predicting the missing values of drug sensitivity (IC50) for a selected set of organoids and drugs.
2. [Subchallenge II](/docs/challenge_overview/subchallenges_i_iii/#subchallenge-ii-predict-how-single-cells-respond-to-different-kinase-inhibitors): 

The resulting predictions will then be scored relative to the ground truth (measurements within the same batch but not present in the training dataset).

For more information about the data, see <span style="color:orange;font-weight:bold">here</span>.

## Challenge Phases
The Challenge will consist of 3 phases: open/training, leaderboard, and validation.

During the **open/training phase**, participants will develop and train their models on the training data set. We welcome submissions based on new or published methods and the integration of any type of biological knowledge. No scores will be reported during this phase.

During the **leaderboard phase**, submitted predictions will be compared against the test dataset and scores will be reported on a public leaderboard. For each <span style="color:orange;font-weight:bold">question/sub-question</span> an associated and paired ground truth will be used to evaluate the predictions. Participants will have an opportunity to improve their models after each leaderboard round for a maximum of three scorable submissions per round.

During the **validation phase**, submitted predictions will be compared against the test dataset. Scores will NOT be reported on the public leaderboard and will NOT be reported in the emails. Participants can submit a maximum of three scorable submissions, we will consider the LAST submission as the final one. Models will be ranked according to their scores and top performers will be announced for each <span style="color:orange;font-weight:bold">subchallenge</span>.

## Data availability for training and scoring
TBD

## References
- Bandura, D.R., Baranov, V.I., Ornatsky, O.I., Antonov, A., Kinach, R., Lou, X., Pavlov, S., Vorobiev, S., Dick, J.E., and Tanner, S.D. (2009). Mass Cytometry: Technique for Real Time Single Cell Multitarget Immunoassay Based on Inductively Coupled Plasma Time-of-Flight Mass Spectrometry. Anal. Chem. 81, 6813–6822.
- Bendall, S.C., Nolan, G.P., Roederer, M., and Chattopadhyay, P.K. (2012). A deep profiler’s guide to cytometry. Trends Immunol. 33, 323–332.
- Bodenmiller, B., Zunder, E.R., Finck, R., Chen, T.J., Savig, E.S., Bruggner, R. V., Simonds, E.F., Bendall, S.C., Sachs, K., Krutzik, P.O., et al. (2012). Multiplexed mass cytometry profiling of cellular states perturbed by small-molecule regulators. Nat. Biotechnol. 30, 858–867.
- Lun, X.-K., Zanotelli, V.R.T., Wade, J.D., Schapiro, D., Tognetti, M., Dobberstein, N., and Bodenmiller, B. (2017). Influence of node abundance on signaling network state and dynamics analyzed by mass cytometry. Nat. Biotechnol. 35, 164–172.
- Lun, X.-K., Szklarczyk, D., Saez-Rodriguez, J., Von Mering, C., and Correspondence, B.B. (2019). Analysis of the Human Kinome and Phosphatome by Mass Cytometry Reveals Overexpression-Induced Effects on Cancer-Related Signaling In Brief. Mol. Cell 74.
- Zivanovic, N., Jacobs, A., and Bodenmiller, B. (2013). A Practical Guide to Multiplexed Mass Cytometry. In Current Topics in Microbiology and Immunology, pp. 95–109.
- Zunder, E.R., Finck, R., Behbehani, G.K., Amir, E.-A.D., Krishnaswamy, S., Gonzalez, V.D., Lorang, C.G., Bjornson, Z., Spitzer, M.H., Bodenmiller, B., et al. (2015). Palladium-based mass tag cell barcoding with a doublet-filtering scheme and single-cell deconvolution algorithm. Nat. Protoc. 10, 316–333.

