---
layout: default
title: Level 3
parent: Maturity levels
nav_order: 4
---

# <span style="color:purple;font-weight:bold">Level 3</span>

## Description

This level of maturity is defined at **community level**. The data at this level complies with community standard domain models, terminologies and formats, and is hosted in an environment offering searching and retrieval capabilities.

### Indicators

{% for indicator in site.indicators_L3 %}
{{ indicator.content }}
{% endfor %}
