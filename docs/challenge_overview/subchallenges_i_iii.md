---
layout: default
title: "Subchallenge I-III: Predict missing single-cell measurements"
parent: Challenge Overview & Questions
---

## Subchallenge I-III: Predict missing single-cell measurements.

## Overview
Subchallenge I focuses on single cell predictions. Participants are asked to predict missing markers in single cells (subchallenge I) and to predict single cell response to kinase inhibitors (subchallenge II and III). For each subchallenge, we selected a small set of cell lines to score the submissions and therefore the respective data is removed from the training set. We provide complete data for more than 40 cell lines, which can be used to train and validate the models. Further, we encourage participants to use the proteomics and genomics data provided for the cell lines and to use external resources (including drug sensitivity information) and prior knowledge (i.e. protein-protein interaction databases) in training and developing their methods.

## Subchallenge I: Predict missing markers at the single cell level.
Predicting missing markers is experimentally a very relevant question as missing markers might result from experimental errors (for example in this dataset p-PLCg2 and p-HER2 are not available for all cell lines) or due to limitations in the panel size (such as in fluorescence measurements). In a nutshell, we ask participants in subchallenge I. to predict the missing values based on other reporters of the measured cells.

For six cell lines we do not provide the measurements for the following markers: p-ERK, p-PLCg2, p-HER2, p-S6, p-AKT_S473 in any treatment conditions - as shown in Figure 1.a and 1.b - and we ask the participants to predict their levels on single cell level, in specific time points after perturbation. Note, that the data on the other cell lines are also available and might be used to improve the prediction.

![Figure 1](../../../assets/images/challenge_overview/subchallenges_i_iii/figure1_aim1.1.jpg)
_Figure 1. Overview subchallenge I. a) List of cell lines and conditions used for scoring the submission for subchallenge I. b) Highlights the available markers across conditions (green boxes) and the missing markers that need to be predicted (dark blue) across each time point in subchallenge I._

## Subchallenge II: Predict how single cells respond to different kinase inhibitors.
In subchallenge II we ask the participants to predict the single cell response to kinase inhibitors. For each of the measured inhibitors we selected three celllines to be predicted as shown in Figure 2.

We ask the participants to derive models that can predict the value of all the single-cell markers in the missing conditions. Please note that for each cell line, in each condition and for each time point we ask for the prediction for all the marker values in 10’000 representative cells. We will compare the statistical properties of the predicted cells to the measured cells to score the predictions. For the exact time points and reporters please consult the “Templates for submitting the predictions” section.

![Figure 2](../../../assets/images/challenge_overview/subchallenges_i_iii/figure2_aim1.2.1.jpg)
_Figure 2. Overview subchallenge II. List of cell lines and conditions used for scoring subchallenge II._

## Subchallenge III: Predict how single cells respond to a novel kinase inhibitor.
The goal of model building is often to make predictions for conditions that the model was not trained on. To test this capability of the methods, we do not provide imTOR perturbation data for any of the cell lines, but we ask the participants to predict the effects of inhibition of mTOR for all cell lines that have otherwise complete single cell data, see Table in Figure 3.

||||||
| --- | --- | --- | --- | --- |
| BT20 | HBL100 | HCC2185 | MDAMB175VII | UACC812|
| BT474 | HCC1187 | HCC3153 | MDAMB361 | UACC893 |
| BT549 | HCC1395 |	HCC38 | MDAMB415 | ZR7530 |
| CAL148 | HCC1419 | HCC70 | MDAMB453 | |
| CAL51 | HCC1500 | HDQP1 | MFM223| |
| CAL851 | HCC1569 | JIMT1 | MPE600 | |
| DU4475 | HCC1599 | MCF7 | MX1 | |
| EFM192A |	HCC1937 | MDAMB134VI | OCUBM | |
| EVSAT | HCC1954 | MDAMB157 | T47D | |

_Figure 3 Cell lines used in scoring subchallenge III._

Participants have to computationally simulate the effect of inhibition for the given time points for each reporter. We ask the participants to derive a model that can predict the value of all the single cell markers in the missing imTOR condition. Please note that in each condition and time point we ask for 10’000 representative cells. For the exact time points and reporters please consult the “Templates for submitting the predictions” section.