---
nav_order: 5
parent: Application areas
title: Automatic post-editing
description: A method to correct errors in the machine translation output
---

**Automatic post-editing** (APE) is the task of correcting automatically the output of a machine translation system.


### Training
Training automatic post-editing models requires access to datasets containing triplets with
- a source text
- the machine-translated version of this source text
- the post-edited version of the machine-translated text
After being trained on these triplets, automatic post-editing models can automatically detect errors and implement corrections.


### Evolution
The evolution of automatic post-editing models is similar to that of machine translation. The first systems were based on rules, then statistical methods were employed before moving to neural networks.
The field gained considerable popularity after the introduction of an APE shared task at [WMT](/more/associations/wmt.md). The shared task provided triplets for training, which facilitated research.


### Challenges
Given that machine translation and automatic post-editing models use similar technology, the margin for improvement is often tight, which raises two main challenges.
Namely, automatic post-editing models 
- Must detect the right errors.
- Must avoid overcorrections (unnecessary changes).


### Data
Data scarcity is another challenge for the field of automatic post-editing, since finding triplets can be a tedious task. A good source of data is the APE shared task at WMT. It includes several domains and language pairs. Since 2019, the machine translation outputs provided in the datasets are based on neural machine translation only, so it is a more accurate representation of current technology.


Due to data availability issues, it is common to build synthetic datasets to train automatic post-editing models. Synthetic data can be created for this task by 
1. Taking a parallel corpus.
2. Applying machine translation to the source.
3. Considering the pre-existing translation as the post-edited version of the machine translation output obtained in 2.
A good example is [eSCAPE (Synthetic Corpus for Automatic Post-Editing)]([https://www.example.com](https://aclanthology.org/L18-1004.pdf) 


### Evaluation methods
Automatic post-editing models can be evaluated using a combination of automatic metrics and human assessment.


Relevant automatic metrics include [TER](/building-and-research/metrics/ter.md) and [BLEU](/building-and-research/metrics/bleu.md) scores. Macro indicators provide the percentage of segments which the model modifies, improves and deteriorates. Based on this information, the precision can be computed as the proportion of improved sentences out of the total number of modified sentences. Micro indicators comprise the distribution of edit operations (average number of edits per segment).


A common methodology for human evaluation is source-based direct assessment, in which evaluators assign a quality score to both translation options (machine translation and automatic post-editing).


### Use cases and tools
Automatic post-editing can be used for specific purposes, such as domain adaptation. It is particularly relevant to improve machine translation without having access to the parameters of a machine translation model.
Corrected versions of machine translation output coming from automatic post-editing models can be used to provide alternative suggestions in translation tools. A good example is the [OpenTIPE](https://aclanthology.org/2023.acl-demo.19.pdf) tool.

