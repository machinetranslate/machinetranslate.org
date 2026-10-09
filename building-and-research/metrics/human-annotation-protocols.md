---
grand_parent: Building and research
parent: Metrics
nav_order: 100
title: Human annotation protocols
description: Metrics for human evaluation of machine translation
---

**Human annotation protocols** for evaluation of machine translation are standards for assessing and comparing how machine translation systems perform on evaluation sets.

## Challenges

- Human evaluation is subjective by nature.
- Human evaluation is slow and expensive.
- There are several competing standards.
- Results from different languages and evaluation sets cannot be compared.

## Annotation protocols

### Direct assessment

In [**direct assessment**](https://aclanthology.org/N15-1124/), for each input, humans rate the output from each system with an absolute score or label.
The sequence-level ratings can then be used to calculate system-level ranking.

Direct assessment was first added as an investigatory ranking for WMT16.
Direct assessment is the official ranking for the translation shared task since WMT17.

There are different types of direct assessment.

- Monolingual: Human raters see the system output only.
- Bilingual: Human raters see the system input and output.
- Reference-based: Human raters see the system output and a reference output.

For [WMT22](/wmt22), a combination of direct assessment and SQM was used for the evaluation of out-of-English and non-English translation pairs.
The [**Scalar Quality Metric**] (**SQM**) evaluation gathers scalar ratings at the segment level with document context.
A table row displays every source segment and its corresponding translated segment from the document. 
For each segment, humans choose a rating on a seven-point scale.

### MQM

[**Multidimensional Quality Metrics**](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00437/108866/Experts-Errors-and-Context-A-Large-Scale-Study-of) (**MQM**) is a framework that determines specific translation errors, severities, and error weights.

Error dimensions:

- Terminology
- Accuracy
- Linguistic conventions
- Style
- Locale conventions
- Audience appropriateness
- Design and markup


### ESA

[**Error Span Annotation**](https://aclanthology.org/2024.wmt-1.131/) (**ESA**) is a combination of a lightweight version of MQM and direct assessment.
With ESA, annotators first mark the error spans with severity (minor or major) but still assign a final score for each segment.
An AI-assisted version of this annotation protocol, dubbed [**ESA<sup>AI</sup>**](https://aclanthology.org/2025.naacl-long.255/) has the error spans pre-filled by a quality-estimation model, which the annotator post-edits and then assigns a final score to the whole translation.
This protocol is the default for WMT sice [WMT23](/wmt23).

### Average score and average z-score

For the **average score**, human assessment scores for translations are standardised according to each human assessor’s overall mean and standard deviation.
Then a system-level score is computed.

**Average z-score** is a normalised version.
It shows the distance between the average score for a system and the mean average score across all systems.

Average score and average z-score are the main metrics used in the results for the translation shared from [WMT17](/wmt17) to [WMT22](/wmt22).

### TrueSkill

[**TrueSkill**](https://proceedings.neurips.cc/paper/2006/file/f44ee263952e65b3610b8ba51229d1f9-Paper.pdf) is a gaming rating system that is able to estimate model performance given a partial list of relative ranking comparisons.
Microsoft Research originally developed it for the Xbox Live gaming community.
For [WMT](/wmt), TrueSkill was adapted to machine translation evaluation.

For [WMT14](/wmt14), [WMT15](/wmt15) and [WMT16](/wmt16), TrueSkill was used as the human evaluation ranking for all translation shared tasks.

### Adequacy and fluency judgement

In **adequacy and fluency judgement**, for each input, humans rank the output from each system for both adequacy and fluency.
Adequacy and fluency scores indicate the meaning adequacy and translation fluency of the system outputs on a five-point scale.

Adequacy and fluency judgement was the official ranking for the translation shared task from [WMT06](/wmt06) to [WMT07](/wmt07).

### Relative ranking

In **relative ranking**, for each input, humans rank the outputs from all systems.
There is no absolute score or label, so there is no measure of absolute quality.

The sequence-level rankings are used to calculate system-level rankings, for example with [TrueSkill](#trueskill).

Relative ranking was the official ranking for the translation shared task from WMT07 to WMT16.

### Constituent ranking

In **constituent ranking**, for each input, humans rank the outputs of an automatically selected syntactic constituent instead of the complete sentences. The constituent score measures how often a system was judged to be better than any other system.

Constituent ranking was the official ranking for the translation shared task from WMT07 to [WMT08](/wmt08).

### Yes or no constituent judgement

In **yes or no constituent judgement**, for each input, humans rank the acceptability of the outputs of an automatically selected syntactic constituent.
The acceptability score measures the per cent of a system translation that was judged to be acceptable.

Yes or no constituent judgement was added as an official ranking for WMT08.


## Tools

The annotation protocols are formal description of how human assessments of translation quality are solicited and are independent of the actual implementation.
The specific annotation tool determines the implementation details and how are annotations distributed and tested.

### Appraise

The [**Appraise** tool](https://aclanthology.org/C18-2019/) has been used by the translation shared task from [WMT16](/wmt16) through [WMT25](/wmt25) and implements many of the above protocols.
>
> ##### SQM protocol example in the Appraise tool
> <img title='SQM protocol example for Chinese to English translation in the Appraise tool' src='/building-and-research/metrics/appraise.png' width='700' style='padding: 1em;' />


### Pearmut

To help with the ease of use, improve reproducibility, and ultimately increase the quality of human evaluation, [**Pearmut**](https://arxiv.org/abs/2601.02933) was proposed in 2026 as a lightweight alternative that implements most of the above protocols.
>
> ##### ESA protocol example in the Pearmut tool
> <img title='ESA protocol example for English to Czech translation in the Pearmut tool' src='/building-and-research/metrics/pearmut.png' width='700' style='padding: 1em;' />