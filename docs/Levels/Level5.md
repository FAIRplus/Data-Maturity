---
layout: default
title: Level 5
parent: Maturity levels
nav_order: 6
---

# <span style="color:purple;font-weight:bold">Level 5</span>

## Description

This level of maturity is defined at **enterprise level**. Data at level 5 is optimally managed at the most granular level in an environment offering data governance, master data and reference data management capabilities.

## Level 5 Data Example

![Level5-Overview](../../assets/images/examples/level5_example.png)


## FAIR-DSM Level 5 Indicators

{% assign indicators = site.indicators | where:"parent_level", "level5" %}
{% for indicator in indicators %}
{{indicator.content}}
{% endfor %}
