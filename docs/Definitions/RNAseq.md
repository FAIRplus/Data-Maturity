---
layout: default
title: RNAseq
parent: Definitions
---


# RNAseq

The RNASeq data was generated in two different facilities with considerably different procedures.

Eleven organoids (batch 1) were expression profiled using a polyA strategy and mapped to the older GRCh37.p13 version of the human genome with the Gencode version 19 genebuild. Two organoids (batch 2) were profiled at another facility with total RNA library preparation and mapped to the most recent genome version (GRCh38.p13) and Gencode version 31.

For one organoid (AMC717) no expression profile is available.

**Batch 1**

01-182, AMC691B, AMC691T, AMC711T, AMC753, AMC772T2, NB039, NB059, NB067, NB129 and NB139

**Batch 2**

066 and 072

The sequence reads were aggregated per gene and normalized as TPM (Transcripts Per Kilobase Million) values. The batches were processed as two separate datasets, so mapping across genebuilds and batch correction still needs to be applied.
