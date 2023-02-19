---
parent: Building and research
title: Human-in-the-loop
description: Machine translation supported by human post-editing or evaluation
---

**Human-in-the-loop** consists of using human feedback for additional [training](/building-and-research/training.md) of translation engines.
Human feedback can be obtained from different tasks:
* Humans correct post-edited machine translation - see [adaptive machine translation](/customisation/adaptive.md)
* Humans annotate errors in the machine translation output - see [human evaluation metrics](/quality/metrics/human-evaluation-metrics.md)
  
Other human-machine interactions are also considered human-in-the-loop:
* Humans improve source content for better translatability
* Humans label training data to classify various domains or quality levels
* Fallback option to human translation in case an automated solution is inadequate

## Goal

The goal of human-in-the-loop is improving the [quality](/quality/quality.md) of machine translation output in all aspects:
* Accuracy - eliminating factual errors and hallucinating
* Fluency - making the language sound more natural for native speakers
* Terminology and style - using appropriate terms and style in given context

## Tasks

1. Pre-editing: Before feeding text into the machine translation system, human editors may pre-edit the source text to ensure that it is clear, concise, and easy to translate.

2. Machine translation: The pre-edited text is then fed into a machine translation system, which generates an initial translation.

3. Post-editing: A human post-editor reviews the machine-generated translation and makes any necessary corrections to improve the quality of the final output. This task is performed by professional translators.

4. Quality assessment: Human quality assessors may evaluate the quality of the machine-generated translations and provide feedback to the machine translation system to help it improve over time. This task requires a checklist of error categories and weights.
<!-- When an article on quality evaluation is added, it can be linked here -->

## References

[ModernMT blog post](https://blog.modernmt.com/human-in-the-loop/) by Kirti Vashee  
[Pangeanic blog post](https://blog.pangeanic.com/human-in-the-loop-hitl-making-the-most-of-human-and-machine-intelligence) by Ángela Franco  
[Medium article](https://medium.com/vsinghbisen/what-is-human-in-the-loop-machine-learning-why-how-used-in-ai-60c7b44eb2c0) by Vikram Singh Bisen  
