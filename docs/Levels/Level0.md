---
layout: default
title: Level 0
parent: Maturity levels
identifier: level1
nav_order: 1
---

# <span style="color:purple;font-weight:bold">Level 0</span>

## Description

Level 0 is a reference level representing a state of data that is missing one or more fundamental FAIR requirements. Data at this level has no potential for reuse beyond the lifetime of the research project.

## Indicators

{% assign indicators = site.indicators | where:"parent_level", "level0" %}
{% for indicator in indicators %}
{{indicator.content}}
{% endfor %}

