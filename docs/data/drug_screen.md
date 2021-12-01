---
layout: default
title: Drugscreens
parent: Data
---

# Drugscreens

Fourteen neuroblastoma derived organoids were screened for drug sensitivity (~200 compounds) using a high throughput drug screening facility. The organoids were treated with for 5 days with a range of drug concentrations after which their viability was measured and normalized against an untreated and an empty control measurement (no cells). All organoids were screened in duplicate. Using these viability measurements, a drug response curve is fitted for every compound and an IC50 (half maximal inhibitory concentration) and AUC (Area Under the Curve) are calculated whenever possible.

The IC50 data contains NA values in cases where the viability remains above 50% even at the highest concentration of a drug. The data also contains ND values (Not Done) since the compound library is continuously updated (new compounds are added and others are removed).  

The fitting of the drug response curves is done with the drc R package [[HvS1](#references)]. The upper limit is set at 1 and the lower limit at 0, under the assumptions that cells don’t grow better under treatment (compared to untreated cells) and that the viabilities below the empty control are also due to experimental noise.

## References
[HvS1]: Ritz C, Baty F, Streibig JC, Gerhard D. Dose-Response Analysis Using R. PLoS One. 2015 Dec 30;10(12):e0146021. doi: 10.1371/journal.pone.0146021. PMID: 26717316; PMCID: PMC4696819.