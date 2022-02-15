---
layout: default
title: Indicators
nav_order: 3
---

# FAIRplus-DSM indicators definitions

The indicators of the FAIRplus-DSM Model are designed to enable researchers in the life sccinces to measure dataset maturity using a finite set of dimensions in conjunction with maturity levels. The levels themselves are a collection of well defined indicators across each maturity dimension, thus enabling user to better understand in what aspects the dataset can be improved in terms of FAIR. This assessment will help the users to benchmark and visibly improve re-usability of their data assets and to increase discoverability, interoperability and overall machine actionability incrementally.

The FAIRplus dataset maturity indicators were created based on previous work around the FAIR indicators, done by the Research Data Alliance (RDA) and the FAIRsFAIR projects:
- FAIR Data Maturity Model Working Group. (2020). FAIR Data Maturity Model. Specification and Guidelines (1.0). https://doi.org/10.15497/rda00050
- Devaraju, Anusuriya, Huber, Robert, Mokrane, Mustapha, Herterich, Patricia, Cepinskas, Linas, de Vries, Jerry, L'Hours, Herve, Davidson, Joy, & Angus White. (2020). FAIRsFAIR Data Object Assessment Metrics (0.4). Zenodo. https://doi.org/10.5281/zenodo.4081213

In the definitions of the FAIRplus-DSM indicators, you will find a link to the corresponding RDA or FAIRsFAIR indicator when they are related.

### F+MM-1.1C

.. include:: indicator_details/F+MM-1.1C.md

### F+MM-1.2C

| Identifer | F+MM-1.2C |
| ----------| ----------|
| Name | Metadata for the data object includes generic descriptive elements of the data object as a whole. |
| Description | Metadata includes descriptive information about the data object, which includes the minimum descriptive information requrired to enable data finding (e.g., name, description, keywords). |
| Related FAIR indicators | F2F-F2-01M |

### F+MM-1.3C

| Identifer | F+MM-1.3C |
| ----------| ----------|
| Name | Metadata includes study/project level summary information (i.e., project-level metadata). |
| Description | Metadata includes information about the project/study in which the data object is included. |
| Related FAIR indicators | None |

### F+MM-1.1R

| Identifer | F+MM-1.1R |
| ----------| ----------|
| Name | Representation of metadata conforms to a locally defined model/schema. |
| Description | The metadata related to the data is represented in a locally defined model such as dictionary of key/value pairs. In level 1, it is not necessary to use a starndarized metadata schema, but a local schema. |
| Related FAIR indicators | None |

### F+MM-1.2R

| Identifer | F+MM-1.2R |
| ----------| ----------|
| Name | Metadata available in a machine-readable format (e.g. CSV, JSON, XML, or similar). |
| Description | Metadata should be readable and interpretable by machines without any requirements such as specific translators or mappings. |
| Related FAIR indicators | RDA-I1-02M, FsF-I1-01M | 

### F+MM-1.1H

| Identifer | F+MM-1.1H |
| ----------| ----------|
| Name | Data object and metadata are retrievable by a standardized communication protocol. |
| Description | Data object and its metadata records are indexed and retrievable via its locally unique identifier by a standardized communication protocol. Given a local identifier of the data object, it should be retrievable using a standard communication protocol such as HTTP or FTP. |
| Related FAIR indicators | RDA-A1-04D, RDA-A1-03M, FsF-A1-03D, FsF-A1-02M |

### F+MM-1.2H

| Identifer | F+MM-1.2H |
| ----------| ----------|
| Name | The standardized communication protocol for data / metadata retrieval is open, free and universally implementable. |
| Description | Protocol free of charge which facilitates access of the data such as HTTP, FTP (e.g. simple links for download). |
| Related FAIR indicators | RDA-A1.1-01D |

### F+MM-2.1C

| Identifer | F+MM-2.1C |
| ----------| ----------|
| Name | Each individual data variable should be reported in a single field, conforming a structured dataset. |
| Description | In level 2, the data object is structured in fields and conforms a dataset. |
| Related FAIR indicators | None |

### F+MM-2.2C

| Identifer | F+MM-2.2C |
| ----------| ----------|
| Name | Metadata includes dataset field level metadata. |
| Description | The fields conforming the dataset are included in the metadata, together with the field name, description and data type. |
| Related FAIR indicators | None |

### F+MM-2.3C

| Identifer | F+MM-2.3C |
| ----------| ----------|
| Name | Data values are standardized against a locally defined dictionary of terms within and across datasets. |
| Description | The values of the data are standardized using a local dictionary. In level 2, there is no need to use ontologies or a community standard vocabullary, but to standarize them locally. |
| Related FAIR indicators | None |

### F+MM-2.1R

| Identifer | F+MM-2.1R |
| ----------| ----------|
| Name | Metadata describing project datasets conforms to a Defined Standard Model. |
| Description | Metadata is structured using a standard model or schema, which can be DCAT, DublinCore or BioSchemas. |
| Related FAIR indicators | None |

### F+MM-2.2R

| Identifer | F+MM-2.2R |
| ----------| ----------|
| Name | Overall project/study data representation uniformly conforms to a locally defined (project-defined) data model or schema. |
| Description | Data is structured in a data model or schema which provides contextual information about the relationships between data content across datasets. |
| Related FAIR indicators | None |

### F+MM-2.3R

| Identifer | F+MM-2.3R |
| ----------| ----------|
| Name | Dataset(s) available in machine readable format. |
| Description |  Dataset(s) should be readable and interoperable by machines without any requirements such as specific translators or mapping. This representation includes CVS, JSON, XML or similar. |
| Related FAIR indicators | RDA-I1-02D |

### F+MM-2.1H

| Identifer | F+MM-2.1H |
| ----------| ----------|
| Name | Data and metadata exchange format is retrieved using API technologies. |
| Description | The communication protocol to retrieve the data at this lavel are API technologies like REST, RPC or GRAPHQL. |
| Related FAIR indicators | None |

### F+MM-2.2H

| Identifer | F+MM-2.2H |
| ----------| ----------|
| Name | Metadata is registered in a searchable resource. |
| Description | Metadata is registred or indexed in a searchable resources and therefore data can be retrieved via its metadata descriptive elements. |
| Related FAIR indicators | RDA-F4-01M |

### F+MM-3.1C

| Identifier | F+MM-3.1C |
| --------- | ----------|
| Name | The dataset is assigned a globally unique and persistent identifier. |
| Maturity Level | 3 |
| Category | Content-related requirements |
| Granularity Level | Dataset |
| Related FAIR Principle | F1. (Meta)data are assigned a globally unique and persistent identifier |
| Description | This indicator only relates to the identification of the dataset as a whole. It adds 'global uniqueness' requirement to F+MM-1.1C. Global uniquness of the identifier is only relevant at this level, since data at this level is expected to be hosted by public repositories or community-level resources.     |
| Related FAIR indicators |  |

### F+MM-3.2C

| Identifier | F+MM-3.2C |
| --------- | ----------|
| Name | Data values are standardized against community standard controlled vocabularies and/or ontologies |
| Maturity Level | 3 |
| Category | Content-related requirements |
| Granularity Level | Dataset Field Values |
| Related FAIR Principle | I2. (Meta)data use vocabularies that follow FAIR principles |
| Description | This indicator focuses on the set of data values for a given dataset field. To promote interoperability and enable the hosting environment to carry out cross-study queries, dataset textual field values should be standardised against community-standard controlled terminology or ontologies.       |
| Related FAIR indicators |  |

### F+MM-3.3C

| Identifier | F+MM-3.3C |
| --------- | ----------|
| Name |  |
| Maturity Level | 3 |
| Category | Content-related requirements |
| Granularity Level |  |
| Related FAIR Principle |  |
| Description |       |
| Related FAIR indicators |  |

### F+MM-3.1R

| Identifier | F+MM-3.1R |
| --------- | ----------|
| Name | Project-level metadata is represented in compliance with a community defined standard Domain Model |
| Maturity Level | 3 |
| Category | Metadata Representation requirements |
| Granularity Level | Project-level |
| Related FAIR Principle | R1.3. (Meta)data meet domain-relevant community standards |
| Description |  This indicator requires multiple-related datasets within a project to conform to a community defined domain model. This indicator does NOT require the Domain Model itself to be formally represented. In most cases, this requirement is satisfied, when datasets are deposited in public repositories, which will implement the standard domain model as their schema.   |
| Related FAIR indicators | RDA-R1.3-01M |

### F+MM-3.2R

| Identifier | F+MM-3.2R |
| --------- | ----------|
| Name | Dataset structural representation conforms to a standard dataset model |
| Maturity Level | 3 |
| Category | Data Representation requirements |
| Granularity Level | Dataset-level |
| Related FAIR Principle | R1.3. (Meta)data meet domain-relevant community standards |
| Description | This indicator requires the collection of data at this level to be structured and represented according to a community-defined standard or a domain-specific repository dataset model. This will guarantee a level of syntactic interoperability that will enable cross-study data indexing and discoverability.   |
| Related FAIR Indicators | RDA-R1.3-01D |

