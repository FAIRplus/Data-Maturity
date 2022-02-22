---
layout: default
title: Level 2
parent: Maturity levels
nav_order: 3
---

# <span style="color:purple;font-weight:bold">Level 2</span>

## Description

Level 2 aims to enhance the usability of a project's structured data. Different projects usually have their own data model and collect different subsets of clinical, molecular, imaging or other data. The FAIRplus-DSM model distinguishes between structured data, unstructured data, and data objects in a project. Structured data include subject-based clinical data, sample-based assay data and other data associated with the data schema. Therefore, indicators at this level, refer to the FAIR Data Object as the 'Dataset' indicating more requirements related to the Dataset Fields and Dataset Field Values. 

This level of maturity aims to increase the FAIRness level of structured data by focusing on Dataset-level structural metadata and Project-level contextual metadata. 

This level of maturity is aimed at data hosted within project-based data repositories, general purpose data repositories or data catalogues.
   

### Indicators

| Category | Identifier | Indicator description |
| -------- | ---------- | --------------------- |
| Content | [F+MM-2.1C] | Structured data are organised into a Dataset structure with identifiable Dataset Fields. |
| Content | [F+MM-2.2C] | Each individual data variable is reported in a single Dataset Field. |
| Content | [F+MM-2.3C] | Metadata record includes Dataset Field level metadata. |
| Content | [F+MM-2.4C] | Dataset field values are standardized against a locally defined dictionary of terms within and across datasets. |
| Representation and format |  [F+MM-2.1R] | Project-level metadata is defined and conforms to a locally defined domain model. |
| Representation and format |  [F+MM-2.2R] | Metadata describing project datasets conforms to a defined standard model. |
| Representation and format |  [F+MM-2.3R] | Dataset(s) available in machine readable format. |
| Hosting environment capabilities | [F+MM-2.1H] | Data and Metadata exchange format is retrieved using API technologies. |
| Hosting environment capabilities | [F+MM-2.2H] | Metadata is registered or indexed in a searchable resource. |
| Hosting environment capabilities | [F+MM-2.3H] | The hosting environment offers metadata archiving capability. |
