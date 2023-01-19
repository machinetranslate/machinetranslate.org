---
grand_parent: Building and research
parent: Metrics
nav_order: 100
title: Human evaluation metrics
description: Metrics for human evaluation of machine translation
---

**Human evaluation metrics** for machine translation are standards for assessing and comparing how machine translation systems perform on evaluation sets.

## Challenges

- Human evaluation is subjective by nature.
- Human evaluation is slow and expensive.
- There are several competing standards.
- Results from different languages and evaluation sets cannot be compared.

## Metrics

### MQM

**Multidimensional Quality Metrics** (**MQM**) is a framework that determines specific translation errors, severities, and error weights.

Error dimensions:

- Terminology
- Accuracy
- Linguistic conventions
- Style
- Locale conventions
- Audience appropriateness
- Design and markup

### Average score and average z-score

For the **average score**, human assessment scores for translations are standardised according to each human assessor’s overall mean and standard deviation.
Then a system-level score is computed.

**Average z-score** is a normalised version.
It shows the distance between the average score for a system and the mean average score across all systems.

Average score and average z-score are the main metrics used in the results for the translation shared task since [WMT17](/../events/wmt17.md).

### TrueSkill

**TrueSkill** is a gaming rating system.
Microsoft Research originally developed it for the Xbox Live gaming community.
For [WMT](/../associations/wmt.md), TrueSkill was adapted to machine translation evaluation.

For [WMT14](/../events/wmt14.md), [WMT15](/../events/wmt15.md) and [WMT16](/../events/wmt16.md), TrueSkill was used as the human evaluation ranking for all translation shared tasks.

### Adequacy and fluency judgement

In **adequacy and fluency judgement**, for each input, humans rank the output from each system for both adequacy and fluency.
Adequacy and fluency scores indicate the meaning adequacy and translation fluency of the system outputs on a five-point scale.

Adequacy and fluency judgement was the official ranking for the translation shared task from [WMT06](/../events/wmt06.md) to [WMT07](/../events/wmt07.md).

### Relative ranking

In **relative ranking**, for each input, humans rank the outputs from all systems.
There is no absolute score or label, so there is no measure of absolute quality.

The sequence-level rankings are used to calculate system-level rankings, for example with [TrueSkill](#trueskill).

Relative ranking was the official ranking for the translation shared task from WMT07 to WMT16.

### Constituent ranking

In **constituent ranking**, for each input, humans rank the outputs of an automatically selected syntactic constituent instead of the complete sentences. The constituent score measures how often a system was judged to be better than any other system.

Constituent ranking was the official ranking for the translation shared task from WMT07 to [WMT08](/../events/wmt08.md).

### Yes or no constituent judgement

In **yes or no constituent judgement**, for each input, humans rank the acceptability of the outputs of an automatically selected syntactic constituent.
The acceptability score measures the per cent of a system translation that was judged to be acceptable.

Yes or no constituent judgement was added as an official ranking for WMT08.

### Direct assessment

In **direct assessment**, for each input, humans rate the output from each system with an absolute score or label.
The sequence-level ratings can then be used to calculate system-level ranking.

Direct assessment was first added as an investigatory ranking for WMT16.
Direct assessment is the official ranking for the translation shared task since WMT17.

There are different types of direct assessment.

- Monolingual: Human raters see the system output only.
- Bilingual: Human raters see the system input and output.
- Reference-based: Human raters see the system output and a reference output.
