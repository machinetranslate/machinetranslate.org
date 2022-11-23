---
grand_parent: Building and research
parent: Metrics
nav_order: 5
title: chrF
description: CHaRacter-level F-score
---

**chrF** (**CHaRacter-level F-score**) is a metric for machine translation evaluation that calculates the similarity between a machine translation output and a reference translation using character [n-grams](/../concepts/n-gram.md), not word n-grams.
Metrics based on word n-grams are especially problematic for high-morphology languages.

chrF was introduced in 2015 by Maja Popović.

The chrF metric compares the machine translation output with reference translations, looking at character sequences. Character sequences matching help in recognizing different forms of a single word.

> It is language-independent, tokenisation-independent and it shows good correlations with human judgments both on the system- as well as with on the segment-level, especially the CHRF3 variant.


### Variants

- chrF3
- chrF++

*Note: The list is incomplete.*

### See more:

- [Metrics](/../resources/publications#metrics)
- [github.com/m-popovic/chrF](https://github.com/m-popovic/chrF)
