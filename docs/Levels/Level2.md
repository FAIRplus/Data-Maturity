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
   

## Indicators

{% assign indicators = site.indicators | where:"parent_level", "level2" %}
{% for indicator in indicators %}
{{indicator.content}}
{% endfor %}
