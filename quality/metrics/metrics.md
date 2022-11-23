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

- [BLEU](bleu.md)
- [METEOR](meteor.md)
- [NIST](nist.md)
- [chrF](chrf.md)
- [TER](ter.md)

*Note: The list is incomplete.*

## Machine learning metrics

Machine learning metrics use a language model. These metrics embed the source sentence into a multidimesional space to calculate the differences.

- [COMET](comet.md)
- [YiSi](yisi.md)
- [BERTscore](bertscore.md)

*Note: The list is incomplete.*

## Language support

String-based metrics can support any language. But the density of words and characters vary by language. So the accuracy varies by language pair, and the results cannot be compared across language pairs.

Machine learning-based metrics require a model that was trained on data with the source and target languages.


## Accuracy

Machine learning-based metrics have a higher correlation with human evaluation.

But metrics based on machine learning are not explainable or fair, so they cannot be used in a research competition.


### History
>
> ##### Slide from [Unbabel](/industry/companies.md#unbabel) for [AMTA 2022](/events/amta2022.md)
> <img title='Evaluation timeline' src='/quality/metrics/timeline.jpg' width='700' style='padding: 1em;' />


## See also

- [Quality evaluation](building-and-research/quality-evaluation.md)
- [Quality estimation](building-and-research/quality-estimation.md)
