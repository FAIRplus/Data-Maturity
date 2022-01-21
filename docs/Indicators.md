---
layout: default
title: Indicators definition
nav_order: 2
---

## Indicators definition

| Level | Category | Identifier | Identifier description |
| ----- | -------- | ---------- | ---------------------- |
| **Level 0** | Content | [F+MM-0.1C] | The Data object or dataset as an entity is undefined or undescribed. |
| **Level 0** | Content | [F+MM-0.2C] | No metadata available. |
| **Level 0** | Representation and format |  [F+MM-0.1R] | No formal definition or representation of metadata. |
| **Level 0** | Representation and format |  [F+MM-0.2R] | Metadata not available in machine readable format (e.g. no metadata or in pdf). |
| **Level 0** | Hosting environmnet capabilities | [F+MM-0.1H] | Data or metadata is hosted in non-accessible storage (e.g., personal desktop, local file system or archive)  and only retrievable by a single or limited users. |
| **Level 0** | Hosting environmnet capabilities | [F+MM-0.2H] | Data or metadata hosted in an accessible resource but with no retrieval capability. |
| **Level 1** | Content | [F+MM-1.1C] | Data object is defined and it is assigned a locally unique and persistent identifier. |
| **Level 1** | Content | [F+MM-1.2C] | Metadata for the data object includes generic descriptive elements of the data object as a whole (e.g., name, description, keywords). |
| **Level 1** | Content | [F+MM-1.3C] | Metadata includes study/project level summary information (i.e., project-level metadata). |
| **Level 1** | Representation and format |  [F+MM-1.1R] | Representation of metadata conforms to a locally defined model/schema  (e.g., dictionary of key/value pairs). |
| **Level 1** | Representation and format |  [F+MM-1.2R] | Metadata available in a machine-readable format (e.g. CSV, JSON, XML, or similar). |
| **Level 1** | Hosting environmnet capabilities | [F+MM-1.1H] | *Data retrieval capability*:<br/> Data object and its metadata record are indexed and retrievable via its globally unique and persistent identifier by a standardized communication protocol. |
| **Level 1** | Hosting environmnet capabilities | [F+MM-1.2H] | The standardized communication protocol for data / metadata retrieval is open, free and universally implementable such as HTTP, FTP (e.g. simple links for download). |
| **Level 1** | Hosting environmnet capabilities | [F+MM-1.3H] | If legally required, the hosting environment offers authentication and authorisation capabilities. |
| **Level 2** | Content | [F+MM-2.1C] | Each study variable is reported in a single dataset field / variable. |
| **Level 2** | Content | [F+MM-2.2C] | Metadata includes dataset field/variable level metadata (e.g. field name, field description and type). |
| **Level 2** | Content | [F+MM-2.3C] | Data values (i.e. field/variable values) are standardized against a locally defined dictionary of terms within and across datasets. |
| **Level 2** | Content | [F+MM-2.4C] | Metadata contains access information for the data. |
| **Level 2** | Representation and format |  [F+MM-2.1R] | Metadata describing project datasets conforms to a Defined Standard Model (e.g. DCAT, DublinCore, BioSchemas). |
| **Level 2** | Representation and format |  [F+MM-2.2R] | Overall project/study data representation uniformly conforms to a locally defined (project-defined) data model or schema providing contextual information about the relationships between data content across datasets. |
| **Level 2** | Representation and format |  [F+MM-2.3R] | Dataset(s) available in machine readable format (e.g. CSV, JSON, XML, or similar). |
| **Level 2** | Hosting environmnet capabilities | [F+MM-2.1H] | *Retrieval capability*:<br/> Data and Metadata exchange format is retrieved using API technologies (REST, RPC, GRAPHQL). |
| **Level 2** | Hosting environmnet capabilities | [F+MM-2.2H] | *Search capability*:<br/> Metadata is registered or indexed in a searchable resource. Data can be retrieved via its metadata descriptive elements. |
| **Level 3** | Content | [F+MM-3.1C] | Data values (i.e. field/variable values) are standardized against community standard controlled vocabularies and/or ontologies. |
| **Level 3** | Content | [F+MM-3.2C] | Metadata includes license information under which data can be reused. |
| **Level 3** | Content | [F+MM-3.3C] | The Dataset object is assigned a globally unique and persistent identifier. |
| **Level 3** | Representation and format |  [F+MM-3.1R] | Overall project/study data representation conforms to a community defined standard domain model (e.g., domain specific repos, OMOP, DATS, ISA). |
| **Level 3** | Representation and format |  [F+MM-3.2R] | Dataset(s) available in a structural representation conforming to a community data exchange standard model (e.g. domain specific repos, SDTM, FHIR, or similar). |
| **Level 3** | Representation and format |  [F+MM-3.3R] | Dataset(s) available in machine readable community standard format relevant to the adopted domain and data model. |
| **Level 3** | Hosting environmnet capabilities | [F+MM-3.1H] | *Search capability*:<br/> Data content is searchable. (e.g. data is retrieable via queries for standarised field names, ontology or controlled terms reported in the datasets). |
| **Level 3** | Hosting environmnet capabilities | [F+MM-3.2H] | The hosting environment is a public / controlled-access repository. |
| **Level 3** | Hosting environmnet capabilities | [F+MM-3.3H] | The hosting environment offers data archiving capability. |
| **Level 3** | Hosting environmnet capabilities | [F+MM-3.4H] | The hosting environment offers version control capability. |
| **Level 4** | Content | [F+MM-4.1C] | Dataset(s) are semantically typed. |
| **Level 4** | Content | [F+MM-4.2C] | Dataset(s) fields are semantically typed. |
| **Level 4** | Content | [F+MM-4.3C] | Master Data Entities across all datasets are defined. |
| **Level 4** | Content | [F+MM-4.4C] | Relevant attributes are provided to allow reuse of the data between communities. |
| **Level 4** | Representation and format |  [F+MM-4.1R] | Metadata is represented in a semantic machine interpretable form. |
| **Level 4** | Representation and format |  [F+MM-4.2R] | Master entity models are formally represented. |
| **Level 4** | Hosting environmnet capabilities | [F+MM-4.1H] | *Search capability*:<br/> Cross-study data is queryable via harmonized master data entities and their attributes. |
| **Level 5** | Content | [F+MM-5.1C] | Domain model entities are defined and harmonized against enterprise managed master data entities (e.g. Observation Features Types, Subject Types, Domain Types). |
| **Level 5** | Content | [F+MM-5.2C] | Field/Variable Level data is linked and harmonized against enterprise managed Reference Data (e.g. MDR registered Data Elements). |
| **Level 5** | Content | [F+MM-5.3C] | Metadata includes provenance information according to a cross-community language. |
| **Level 5** | Representation and format |  [F+MM-5.1R] | Data-linked Data Elements are represented and formatted in a community standard model/format (e.g. ISO 11179 MDR standard). |
| **Level 5** | Representation and format |  [F+MM-5.2R] | Data-linked controlled terminologies and ontologies are formatted and represented by community standards. |
| **Level 5** | Hosting environmnet capabilities | [F+MM-5.1H] | Hosting Environment implements Master Data Management Capability. |
| **Level 5** | Hosting environmnet capabilities | [F+MM-5.2H] | Hosting Environment implements Reference Data Management Capability. |
| **Level 5** | Hosting environmnet capabilities | [F+MM-5.3H] | Hosting Environment implements Data Governance Capability. |
