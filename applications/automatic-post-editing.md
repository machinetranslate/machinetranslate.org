---
nav_order: 5
parent: Building and research
title: Automatic post-editing
description: Automatic post-editing of machine translation
---

**Automatic post-editing (APE)** is the task of automatically correcting the output of a machine translation system. Like in manual human post-editing, the objective is to improve the quality of a machine translation output. For example, automatic post-editing can be used to correct errors or apply a certain style.
Automatic post-editing systems should meet multiple requirements:
- detect and fix machine translation errors
- avoid making overcorrections, especially those that add new errors


### Evolution
The evolution of automatic post-editing systems is similar to that of machine translation. The first systems took [rule-based approaches](/rule-based-machine-translation), later systems took [statistical approaches](/statistical-machine-translation) and then [neural approaches](/neural-machine-translation).


### Use cases
Automatic post-editing can be applied in several use cases:
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


### Datasets
The datasets from the [quality estimation](/quality-estimation) shared task at [WMT](/wmt) can be used for training and evaluating automatic post-editing systems.

When human post-edited translations are not available, synthetic post-editing data can be created from ordinary translation data. For example, [eSCAPE (Synthetic Corpus for Automatic Post-Editing)]( https://aclanthology.org/L18-1004.pdf) creates synthetic data by inserting a machine translation.


### Evaluation
Automatic post-editing systems can be evaluated like machine translation systems:
-	Automatic, reference-based evaluation metrics, like [TER](/ter) or [BLEU](/bleu)
-	Human evaluation, like direct assessment

Evaluation reveals how many sentences were improved. Precision can be calculated by dividing the number of improved sentences by the total number of modified sentences. Another common metric is the average number of edits per segment.

