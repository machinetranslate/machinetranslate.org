---
parent: Building and research
has_children: true
nav_order: 150
title: Metrics
description: List of metrics for evaluating machine translation
seo:
    name: List of metrics for evaluating machine translation
---

**Metrics** measure the quality of the output of a machine translation system.

Metrics are used to compare different machine translation systems.

The best known metric for machine translation is [BLEU](/bleu), a string-based automatic metric.

{% include collapsible_toc.html %}

## Automatic evaluation metrics

Automatic quality metrics can be computed relatively quickly.

Automatic quality metrics are divided into **string-based metrics** and **machine learning-based metrics**.

### String-based metrics

String-based metrics generally measure the word or character distance between the target sentence and the reference translation.

Examples:
- [BLEU](/bleu)
- [METEOR](/meteor)
- [NIST](/nist)
- [chrF](/chrF)
- [TER](/ter)

String-based are used in research papers and competitions because they are explainable and fair, and they can support any language pair.

But string-based metrics can punish translations that convey the correct meaning, and the scores cannot be compared across language pairs.

The scores generally do not correlate well with human evaluation scores when translation quality is high.


### Machine learning-based metrics

Machine learning-based metrics use [sentence embeddings](/sentence-embeddings) to calculate the difference between the generated target sentence and the reference translation, or even between the target sentence and the source sentence.

Examples:/
- [COMET](/comet)
- [YiSi](/yisi)
- [BERTscore](/bertscore)

Machine learning-based metrics require a model that was trained on data with the source and target languages.

The score can correlate well with human evaluation scores.

But the scores are not explainable or fair, so they cannot be used in a research competition.


## Human evaluation metrics

Human evaluation is the gold standard.

- [MQM](/human-evaluation-metrics#mqm)
- [SQM](/human-evaluation-metrics#sqm)
- [Average score and average z-score](/human-evaluation-metrics#average-score-and-average-z-score)
- [TrueSkill](/human-evaluation-metrics#trueskill)
- [Adecuacy and fluency judgement](/human-evaluation-metrics#adequacy-and-fluency-judgement)
- [Relative ranking](/human-evaluation-metrics#relative-ranking)
- [Constituent ranking](/human-evaluation-metrics#constituent-ranking)
- [Yes or no constituent judgement](/human-evaluation-metrics#yes-or-no-constituent-judgement)
- [Direct assessment](/human-evaluation-metrics#direct-assessment)

But human evaluation is slow, expensive and subjective.


### Evolution
>
> ##### Slide from [Unbabel](/companies#unbabel) for [AMTA 2022](/amta-2022)
> <img title='Evaluation timeline' src='/building-and-research/metrics/timeline.jpg' width='700' style='padding: 1em;' />


## See also

- [Quality evaluation](/quality-evaluation)
- [Quality estimation](/quality-estimation)
