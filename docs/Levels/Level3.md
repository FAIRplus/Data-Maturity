---
layout: default
title: Level 3
parent: Maturity levels
nav_order: 4
---

# <span style="color:purple;font-weight:bold">Level 3</span>

## Description

This level of maturity is defined at **community level**. The data at this level complies with community standard domain models, terminologies and formats, and is hosted in an environment offering searching and retrieval capabilities.

## Indicators

{% assign indicators = site.indicators | where:"parent_level", "level3" %}
{% for indicator in indicators %}
{{indicator.content}}
{% endfor %}
