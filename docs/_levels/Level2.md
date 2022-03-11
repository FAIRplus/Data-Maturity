---
layout: default
title: Level 2
parent: Maturity levels
nav_order: 3
---

# <span style="color:purple;font-weight:bold">Level 2</span>

## Description

Level 2 aims to enhance the usability of a project, or a study's structured data, which often are represented by multiple related datasets. Different projects usually have their own data model and collect different subsets of clinical, molecular, imaging or other data. The FAIRplus-DSM model distinguishes between structured data, unstructured data, and data objects in a project. Structured data include subject-based clinical data, sample-based assay data and other data associated with the data schema. Therefore, indicators at this level, refer to the FAIR Data Object as the **Dataset** indicating more requirements related to the structural metadata of the Dataset, namely the **Dataset Fields** and the corresponding **Dataset Field Values**. 

This level of maturity aims to increase the FAIRness level of structured data by focusing on Dataset-level structural metadata and Project-level contextual metadata. 

This level of maturity is aimed at data hosted within project-based data repositories, general purpose data repositories or data catalogues.
   

### Indicators

| Category | Identifier | Indicator description |
| -------- | ---------- | --------------------- |
| Content | [F+MM-2.1C] | Project's structured Data are organized into identifiable Dataset(s) each assigned a unique Dataset identifier |
| Content | [F+MM-2.2C] | Contextual and Domain-related Metadata is reported (Common Domain Entities reported in and across the Dataset(s) and relationships between them). |
| Content | [F+MM-2.3C] | Each recorded Data Variable is individually reported in a single Dataset Field. |
| Content | [F+MM-2.4C] | Metadata Record includes Dataset-Field level metadata (e.g. field name, field description and type). |
| Content | [F+MM-2.5C] | Dataset Field Values are standardized against a locally defined Data Dictionary within and across related datasets. |
| Content | [F+MM-2.6C] | Metadata Record includes reference to Value-level metadata defined in the Data Dictionary.  |
| Representation and format |  [F+MM-2.1R] | Contextual Metadata and Domain related metadata is represented in a human interpretable form |
| Representation and format |  [F+MM-2.2R] | Project related Datasets conform to a locally defined Dataset Model for data exchange purposes. |
| Representation and format |  [F+MM-2.3R] | Dataset’s internal Structural Metadata is represented in accordance to a standard Metadata Schema. |
| Representation and format |  [F+MM-2.4R] | Dataset(s) available in Machine Readable Format. |
| Hosting Environment | [F+MM-2.1H] | Data hosting environment stores data in accordance to a locally defined Data Model / Schema  for persistence purposes. |
| Hosting Environment | [F+MM-2.2H] | Metadata hosting environment provides programmatic access and retrieval (API) for the Dataset's Metadata Record. |
| Hosting Environment | [F+MM-2.3H] | Hosting environment offers the capability to browse related Datasets |
