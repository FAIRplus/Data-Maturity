---
layout: default
title: Level 1
parent: Maturity levels
nav_order: 2
---

# <span style="color:purple;font-weight:bold">Level 1</span>

## Description

In level 1, data is identifiable as individual generic data objects that are described by generic metadata elements. Hosting environment offers limited retrieval capabilities.

This level prescribes the entry level requirements that all the higher levels will build up upon. It establishes basic requirements to enable 'Findability', 'Accessibility' with basic descriptive metadata that enables data users to interpret and understand the data object.

The first step to be at Maturity Level 1 is to define and identify the data object that is expected to be shared and re-used (i.e., the FAIR data object). Notice this level is referring to a Data Object rather than a Dataset. This is to imply that data at this level includes both structured and unstructured data. 

### Indicators

{% for indicator in site.1indicators %}
{{ indicator.content }}
{% endfor %}
