---
layout: default
title: Indicators definition
nav_order: 2
---

# Indicators definition

## <span style="color:purple;font-weight:bold">Level 0</span>

| Category | Identifier | Identifier description |
| -------- | ---------- | ---------------------- |
| Content | [F+MM-0.1C] | The Data object or dataset as an entity is undefined or undescribed. |
| Content | [F+MM-0.2C] | No metadata available. |
| Representation and format |  [F+MM-0.1R] | No formal definition or representation of metadata. |
| Representation and format |  [F+MM-0.2R] | Metadata not available in machine readable format (e.g. no metadata or in pdf). |
| Hosting environmnet capabilities | [F+MM-0.1H] | Data or metadata is hosted in non-accessible storage (e.g., personal desktop, local file system or archive)  and only retrievable by a single or limited users. |
| Hosting environmnet capabilities | [F+MM-0.2H] | Data or metadata hosted in an accessible resource but with no retrieval capability. |

## <span style="color:purple;font-weight:bold">Level 1</span>

| Category | Identifier | Identifier description |
| -------- | ---------- | ---------------------- |
| Content | [F+MM-1.1C] | Data object is defined and it is assigned a locally unique and persistent identifier. |
| Content | [F+MM-1.2C] | Metadata for the data object includes generic descriptive elements of the data object as a whole (e.g., name, description, keywords). |
| Content | [F+MM-1.3C] | Metadata includes study/project level summary information (i.e., project-level metadata). |
| Representation and format |  [F+MM-1.1R] | Representation of metadata conforms to a locally defined model/schema  (e.g., dictionary of key/value pairs). |
| Representation and format |  [F+MM-1.2R] | Metadata available in a machine-readable format (e.g. CSV, JSON, XML, or similar). |
| Hosting environmnet capabilities | [F+MM-1.1H] | *Data retrieval capability*:<br/> Data object and its metadata record are indexed and retrievable via its globally unique and persistent identifier by a standardized communication protocol. |
| Hosting environmnet capabilities | [F+MM-1.2H] | The standardized communication protocol for data / metadata retrieval is open, free and universally implementable such as HTTP, FTP (e.g. simple links for download). |
| Hosting environmnet capabilities | [F+MM-1.3H] | If legally required, the hosting environment offers authentication and authorisation capabilities. |

## <span style="color:purple;font-weight:bold">Level 2</span>

| Category | Identifier | Identifier description |
| -------- | ---------- | ---------------------- |
| Content | [F+MM-2.1C] | Each study variable is reported in a single dataset field / variable. |
| Content | [F+MM-2.2C] | Metadata includes dataset field/variable level metadata (e.g. field name, field description and type). |
| Content | [F+MM-2.3C] | Data values (i.e. field/variable values) are standardized against a locally defined dictionary of terms within and across datasets. |
| Content | [F+MM-2.4C] | Metadata contains access information for the data. |
| Representation and format |  [F+MM-2.1R] | Metadata describing project datasets conforms to a Defined Standard Model (e.g. DCAT, DublinCore, BioSchemas). |
| Representation and format |  [F+MM-2.2R] | Overall project/study data representation uniformly conforms to a locally defined (project-defined) data model or schema providing contextual information about the relationships between data content across datasets. |
| Representation and format |  [F+MM-2.3R] | Dataset(s) available in machine readable format (e.g. CSV, JSON, XML, or similar). |
| Hosting environmnet capabilities | [F+MM-2.1H] | *Retrieval capability*:<br/> Data and Metadata exchange format is retrieved using API technologies (REST, RPC, GRAPHQL). |
| Hosting environmnet capabilities | [F+MM-2.2H] | *Search capability*:<br/> Metadata is registered or indexed in a searchable resource. Data can be retrieved via its metadata descriptive elements. |

## <span style="color:purple;font-weight:bold">Level 3</span>

| Category | Identifier | Identifier description |
| -------- | ---------- | ---------------------- |
| Content | [F+MM-3.1C] | Data values (i.e. field/variable values) are standardized against community standard controlled vocabularies and/or ontologies. |
| Content | [F+MM-3.2C] | Metadata includes license information under which data can be reused. |
| Content | [F+MM-3.3C] | The Dataset object is assigned a globally unique and persistent identifier. |
| Representation and format |  [F+MM-3.1R] | Overall project/study data representation conforms to a community defined standard domain model (e.g., domain specific repos, OMOP, DATS, ISA). |
| Representation and format |  [F+MM-3.2R] | Dataset(s) available in a structural representation conforming to a community data exchange standard model (e.g. domain specific repos, SDTM, FHIR, or similar). |
| Representation and format |  [F+MM-3.3R] | Dataset(s) available in machine readable community standard format relevant to the adopted domain and data model. |
| Hosting environmnet capabilities | [F+MM-3.1H] | *Search capability*:<br/> Data content is searchable. (e.g. data is retrieable via queries for standarised field names, ontology or controlled terms reported in the datasets). |
| Hosting environmnet capabilities | [F+MM-3.2H] | The hosting environment is a public / controlled-access repository. |
| Hosting environmnet capabilities | [F+MM-3.3H] | The hosting environment offers data archiving capability. |
| Hosting environmnet capabilities | [F+MM-3.4H] | The hosting environment offers version control capability. |

## <span style="color:purple;font-weight:bold">Level 4</span>

| Category | Identifier | Identifier description |
| -------- | ---------- | ---------------------- |
| Content | [F+MM-4.1C] | Dataset(s) are semantically typed. |
| Content | [F+MM-4.2C] | Dataset(s) fields are semantically typed. |
| Content | [F+MM-4.3C] | Master Data Entities across all datasets are defined. |
| Content | [F+MM-4.4C] | Relevant attributes are provided to allow reuse of the data between communities. |
| Representation and format |  [F+MM-4.1R] | Metadata is represented in a semantic machine interpretable form. |
| Representation and format |  [F+MM-4.2R] | Master entity models are formally represented. |
| Hosting environmnet capabilities | [F+MM-4.1H] | *Search capability*:<br/> Cross-study data is queryable via harmonized master data entities and their attributes. |

## <span style="color:purple;font-weight:bold">Level 5</span>

| Category | Identifier | Identifier description |
| -------- | ---------- | ---------------------- |
| Content | [F+MM-5.1C] | Domain model entities are defined and harmonized against enterprise managed master data entities (e.g. Observation Features Types, Subject Types, Domain Types). |
| Content | [F+MM-5.2C] | Field/Variable Level data is linked and harmonized against enterprise managed Reference Data (e.g. MDR registered Data Elements). |
| Content | [F+MM-5.3C] | Metadata includes provenance information according to a cross-community language. |
| Representation and format |  [F+MM-5.1R] | Data-linked Data Elements are represented and formatted in a community standard model/format (e.g. ISO 11179 MDR standard). |
| Representation and format |  [F+MM-5.2R] | Data-linked controlled terminologies and ontologies are formatted and represented by community standards. |
| Hosting environmnet capabilities | [F+MM-5.1H] | Hosting Environment implements Master Data Management Capability. |
| Hosting environmnet capabilities | [F+MM-5.2H] | Hosting Environment implements Reference Data Management Capability. |
| Hosting environmnet capabilities | [F+MM-5.3H] | Hosting Environment implements Data Governance Capability. |
