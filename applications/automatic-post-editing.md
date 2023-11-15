---
nav_order: 5
parent: Application areas
title: Automatic post-editing
description: Automatic correction of machine translation errors
---

**Automatic post-editing** (APE) is the task of correcting automatically the output of a machine translation system.
Automatic post-editing systems should
- detect machine translation errors
- avoid making overcorrections, especially those that add new errors


### Evolution
The evolution of automatic post-editing systems is similar to that of machine translation. The first systems took [rule-based approaches](/building-and-research/approaches/rule-based-machine-translation.md), later systems took [statistical approaches](/building-and-research/approaches/statistical-machine-translation.md) and then [neural approaches](/building-and-research/approaches/neural-machine-translation.md).


### Use cases and tools
Automatic post-editing can be used for 
- fixing errors in machine translation outputs
- adapting the output of a machine translation system to a custom domain
- providing alternative translation suggestions in translation tools, for example [OpenTIPE](https://aclanthology.org/2023.acl-demo.19.pdf)


### Training
Automatic post-editing systems are usually trained with parallel triplets containing
- a source text
- the machine-translated version of this source text
- the post-edited version of the machine-translated text

| Source | Machine translation | Human post-edited translation|
| How are you?	| ¿Cómo estás?	| ¿Cómo está?|
| Computer| Computadora| Ordenadora|
| … | … | …|


### Data
The introduction of an automatic post-editing shared task at [WMT](/more/associations/wmt.md) facilitated research by providing triplets for training.

When human post-edited translations are not available, synthetic data can be created from parallel data. For example, [eSCAPE (Synthetic Corpus for Automatic Post-Editing)]( https://aclanthology.org/L18-1004.pdf) creates synthetic data by inserting a machine translation.


### Evaluation
Automatic post-editing systems can be evaluated like machine translation systems:
-	automatic, reference-based evaluation metrics, like [TER](/building-and-research/metrics/ter.md) or [BLEU](/building-and-research/metrics/bleu.md)
-	human evaluation, like direct assessment

Evaluation reveals how many sentences were improved. Precision can be calculated by dividing the number of improved sentences by the total number of modified sentences. Another common metric is the average number of edits per segment.
