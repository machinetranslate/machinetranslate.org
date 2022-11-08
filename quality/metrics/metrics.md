---
parent: Building and research
has_children: true
nav_order: 150
title: Metrics
description: Metrics for evaluating machine translation
---

Metrics are formulas that represent the quality of the machine translation output.

Machine translation quality metrics are divided into string-based metrics and pre-trained metrics.

## String-based metrics

String-based metrics measure the lexical matching between the system output and the reference translation.

### Challenges

String-based metrics are challenging because there are many possible translations for a single source text.

### Examples

- BLEU
- METEOR
- NIST
- chrF
- TER

*Note: The list is incomplete.*

### Pre-trained metrics

Pre-trained metrics use a language model. These metrics embed the source sentence into a multidimesional space to calculate the differences.

- COMET
- YiSi
- BERTscore

*Note: The list is incomplete.*

| String-based metrics | Pre-trained metrics |
| --- | --- |
| Support any language | Support only pre-trained language |
| Need reference | Do not reference |
| Low correlation with human evaluation | High correlation with human evaluation |

### Metrics timeline
>
> ##### Slide from [Unbabel](/industry/companies.md#unbabel) for [AMTA 2022](/events/amta2022.md)
> <img title='Evaluation timeline' src='/quality/metrics/timeline.jpg' width='700' style='padding: 1em;' />


## See also

- [Quality evaluation](building-and-research/quality-evaluation.md)
- [Quality estimation](building-and-research/quality-estimation.md)
