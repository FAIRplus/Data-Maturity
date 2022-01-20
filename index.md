---
layout: default
title: Overview
nav_order: 1
description: "Overview FAIRplus data maturity"
permalink: /
---

![Banner](assets/images/overview/banner_draft.JPG)

## FAIRplus Dataset Maturity Model (DSM)

A life-sciences domain-specific, indicator-based dataset maturity model to serve as both an assessment and a maturation guide towards FAIR maturity of a dataset. The levels within this Maturity Model contain the metadata required to achieve a certain level of Dataset FAIRness (as outlined in the FAIR Metadata Requirements Model) along with the FAIR benefits achieved at each level.

## The three dimensions of FAIR Data Maturation

- **Content-related**: What is reported in the dataset & the metadata.
- **Representation and format**: How the data object & metadata object are represented and formatted.
- **Hosting environment capabilities**: What capabilities of the hosting environment that enables and supports the use of FAIR data.

![Dimensions](assets/images/overview/dimensions.JPG)

## Maturity levels

![Levels](assets/images/overview/levels_definition.png)

## Maturity Model

![Grid](assets/images/overview/grid_view.png)

| Categories | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |
| ---------- | ------- | ------- | ------- | ------- | ------- | ------- |
| Content | • The Data object or dataset as an entity is undefined or undescribed.<br /> • No metadata available | • Data object is defined and it is assigned a locally unique and persistent identifier.<br /> • Metadata for the data object includes generic descriptive elements of the data object as a whole. | • Each study variable is reported in a single dataset field / variable.<br /> • Metadata includes dataset field/variable level metadata.<br /> • Data values are standardized against a locally defined dictionary of terms within and across datasets.<br /> • Metadata contains access information for the data. | • Data values are standardized against community standard controlled vocabularies and/or ontologies.<br /> • Metadata includes license information under which data can be reused.<br /> • The Dataset object is assigned a globally unique and persistent identifier. | • Dataset(s) are semantically typed.<br /> • Dataset(s) fields are semantically typed.<br /> • Master Data Entities across all datasets are defined.<br /> - Relevant attributes are provided to allow reuse of the data between communities. | • Domain model entities are defined and harmonized against enterprise managed master data entities.<br /> • Field/Variable Level data is linked and harmonized against enterprise managed Reference Data.<br /> • Metadata includes provenance information according to a cross-community language |
