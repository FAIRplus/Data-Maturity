---
layout: default
title: Indicators
nav_order: 3
---

# FAIRplus-DSM indicators definitions

The indicators of the FAIRplus-DSM Model are designed to enable researchers in the life sciences to measure dataset maturity using a finite set of dimensions in conjunction with maturity levels. The levels themselves are a collection of well defined indicators across each maturity dimension, thus enabling user to better understand in what aspects the dataset can be improved in terms of FAIR. This assessment will help the users to benchmark and visibly improve re-usability of their data assets and to increase discoverability, interoperability and overall machine actionability incrementally.

The FAIRplus dataset maturity indicators were created based on previous work around the FAIR indicators, done by the Research Data Alliance (RDA) and the FAIRsFAIR projects:
- FAIR Data Maturity Model Working Group. (2020). FAIR Data Maturity Model. Specification and Guidelines (1.0). https://doi.org/10.15497/rda00050
- Devaraju, Anusuriya, Huber, Robert, Mokrane, Mustapha, Herterich, Patricia, Cepinskas, Linas, de Vries, Jerry, L'Hours, Herve, Davidson, Joy, & Angus White. (2020). FAIRsFAIR Data Object Assessment Metrics (0.4). Zenodo. https://doi.org/10.5281/zenodo.4081213

In the definitions of the FAIRplus-DSM indicators, you will find a link to the corresponding RDA or FAIRsFAIR indicator when they are related.

{% for indicator in site.indicators_L1 %}
{{ indicator.content }}
{% endfor %}
