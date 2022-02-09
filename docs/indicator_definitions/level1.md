---
layout: default
title: Level 1
parent: Indicators extensive definitions
nav_order: 1
---

# Level 1

## Content

### F+MM-1.1C

| Identifer | F+MM-1.1C |
| ----------| ----------|
| Name | Data object is defined and it is assigned a locally unique identifier. |
| Description | The data object is assigned to a locally unique identifier such that it can be referenced unambiguously and therefore there are no two identical identifiers that identify the same data object at a project level. Locally unique means an identifier should be associated with only one reosurce in the local project. In level 1, it does not need to be globally unique. |
| Related FAIR indicators | None |

### F+MM-1.2C

| Identifer | F+MM-1.2C |
| ----------| ----------|
| Name | Metadata for the data object includes generic descriptive elements of the data object as a whole. |
| Description | Metadata includes descriptive information about the data object, which includes the minimum descrptive information requrired to enable data finding (e.g., name, description, keywords). |
| Related FAIR indicators | F2F-F2-01M |

### F+MM-1.3C

| Identifer | F+MM-1.3C |
| ----------| ----------|
| Name | Metadata includes study/project level summary information (i.e., project-level metadata). |
| Description | Metadata includes information about the project/study in which the data object is included. |
| Related FAIR indicators | None |

## Representation and format

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

## Hosting environment capabilities

### F+MM-1.1H

| Identifer | F+MM-1.1H |
| ----------| ----------|
| Name | Data retrieval capability. |
| Description | Data object and its metadata record are indexed and retrievable via its locally unique and persistent identifier by a standardized communication protocol. Given a local identifier of a data object, it should be retrievable using a standard communication protocol such as HTTP or FTP. |
| Related FAIR indicators | RDA-A1-04D, FsF-A1-03D |

### F+MM-1.2H

| Identifer | F+MM-1.2H |
| ----------| ----------|
| Name | The standardized communication protocol for data / metadata retrieval is open, free and universally implementable. |
| Description | Protocol free or charge which facilitates access of the data such as HTTP, FTP (e.g. simple links for download). |
| Related FAIR indicators | RDA-A1.1-01D |
