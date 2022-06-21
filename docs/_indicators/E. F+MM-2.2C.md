---
layout: default
title: F+MM-2.2C
parent_level: level2
nav_exclude: True
---

## F+MM-2.2C

| Identifier | [F+MM-2.2C](https://github.com/FAIRplus/Data-Maturity/edit/v0.3/docs/_indicators/E.%20F+MM-2.2C.md) |
| ---------- | ----------|
| Name | Where applicable, the [Dataset Model](https://fairplus.github.io/Data-Maturity/docs/Glossary/#dataset-model) organises data values within a dataset according to the [Tidy Data Principles](https://fairplus.github.io/Data-Maturity/docs/Glossary/#tidy-data-principles)  |
| Maturity Level | 2 |
| Category | Content and Context |
| Granularity Level | Dataset Fields |
| Related FAIR Principle | R1. Meta(data) are richly described with a plurality of accurate and relevant attributes |
| Description | This is a **data-related requirement** that is a pre-requisite for the 'accuracy' of metadata that FAIR principle (R1) refers to. This requirement is borrowed from one of the key Tidy Data Principles, which states that each column/field should be a **single** variable. This prevents the often seen scenario in structured data whereby a single column header might carry values for more than one variable. For example, 'temperature_screening', 'temperature_followup', each column implicitly carries the value for a **visit** variable and a value for an observation **temperature** in this case. This indicator therefore requires the data manager to split these variables into two fields: One per variable that is a field for **temperature** and a field for **visit**. This is a pre-requisite to F+MM-2.5 and F+MM-2.6 since each Dataset Field is expected to control its terms and create a local dictionary. Unless individual concepts are reported per Dataset Field it will not be possible to find suitable terms that can later be standardised for level 3. |
| Cross-reference FAIR indicators | |