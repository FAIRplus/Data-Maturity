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

![Levels](assets/images/overview/levels_definition.JPG)

## Maturity Model

| Categories | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |
| ---------- | ------- | ------- | ------- | ------- | ------- | ------- |
| **Content** | • The Data object or dataset as an entity is undefined or undescribed.<br /> • No metadata available. | • Data object is defined and it is assigned a locally unique and persistent identifier.<br /> • Metadata for the data object includes generic descriptive elements of the data object as a whole. | • Each study variable is reported in a single dataset field / variable.<br /> • Metadata includes dataset field/variable level metadata.<br /> • Data values are standardized against a locally defined dictionary of terms within and across datasets.<br /> • Metadata contains access information for the data. | • Data values are standardized against community standard controlled vocabularies and/or ontologies.<br /> • Metadata includes license information under which data can be reused.<br /> • The Dataset object is assigned a globally unique and persistent identifier. | • Dataset(s) are semantically typed.<br /> • Dataset(s) fields are semantically typed.<br /> • Master Data Entities across all datasets are defined.<br /> • Relevant attributes are provided to allow reuse of the data between communities. | • Domain model entities are defined and harmonized against enterprise managed master data entities.<br /> • Field/Variable Level data is linked and harmonized against enterprise managed Reference Data.<br /> • Metadata includes provenance information according to a cross-community language. |
| **Representation and format** | • No formal definition or representation of metadata.<br /> • Metadata not available in machine readable format. | • Representation of metadata conforms to a locally defined model/schema.<br /> • Metadata available in a machine-readable format. | • Metadata describing project datasets conforms to a Defined Standard Model.<br /> • Overall project/study data representation uniformly conforms to a locally defined (project-defined) data model or schema providing contextual information about the relationships between data content across datasets.<br /> • Dataset(s) available in machine readable format.<br /> | • Overall project/study data representation conforms to a community defined standard domain model.<br /> • Dataset(s) available in a structural representation conforming to a community data exchange standard model.<br /> • Dataset(s) available in machine readable community standard format relevant to the adopted domain and data model.<br /> | • Metadata is represented in a semantic machine interpretable form. <br /> • Master entity models are formally represented.<br /> | • Data-linked Data Elements are represented and formatted in a community standard model/format.<br /> • Data-linked controlled terminologies and ontologies are formatted and represented by community standards.<br /> |
| **Hosting Environment Capabilities** | • Data or metadata is hosted in non-accessible storage and only retrievable by a single or limited users.<br /> • Data or metadata hosted in an accessible resource but with no retrieval capability.<br /> | • Data object and its metadata record are indexed and retrievable via its globally unique and persistent identifier by a standardized communication protocol.<br /> • The standardized communication protocol for data / metadata retrieval is open, free and universally implementable.<br /> • If legally required, the hosting environment offers authentication and authorisation capabilities.<br /> | • Data and Metadata exchange format is retrieved using API technologies.<br /> • Metadata is registered or indexed in a searchable resource. Data can be retrieved via its metadata descriptive elements.<br /> | • Data content is searchable. (e.g. data is retrieable via queries for standarised field names, ontology or controlled terms reported in the datasets)<br /> • The hosting environment is a public / controlled-access repository.<br /> • The hosting environment offers data archiving capability.<br /> • The hosting environment offers version control capability.<br /> | • Cross-study data is queryable via harmonized master data entities and their attributes.<br /> | • Hosting Environment implements Master Data Management Capability.<br /> • Hosting Environment implements Reference Data Management Capability.<br /> • Hosting Environment implements Data Governance Capability.<br /> |
