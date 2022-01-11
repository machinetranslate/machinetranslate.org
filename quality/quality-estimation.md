---
parent: Quality
title: Quality estimation
description: Machine translation quality estimation
---

**Quality estimation** (**QE**) is a method for automatically assessing the quality of the machine translation output without human intervention. QE scores are independent from the expected translation output.

| Original                     | Translation                    | Quality estimate     |
| -----------------------------| -------------------------------| ---------------------|
| `English` `July 30th, 2021`  | `French` `30 juillet 2021`     | `Good`               |
| `English` `This is my home.` | `Spanish` `Este es mi inicio.` | `Bad`                |

Evaluation metrics like BLEU or post-editing distance require human reference translations, but there are no human reference translations for new content.

QE models predicts the quality based on either specific features or deep learning.


### Use cases

Quality estimation has offline and production use cases:

* Comparing machine translation systems or translation models
* [Hybrid translation](/workflows/hybrid-translation.md)
* Estimating [post-editing](/workflows/post-editing.md) effort
* Validating final human translations
* Filtering training data for machine translation

### Granularity

* Word-level
* Phrase-level
* Sentence-level
* Document-level

Sentence-level scores can be aggregated into paragraph-level scores or document-level scores. Word-, phrase- and sentence-level scores can indicate if a machine translation output needs to be post-edited. Document-level scores indicate if a machine translation output can be used without human post-editing.

### Approaches

Quality estimation is typically implemented as classification or regression.

### Supervised
Supervised quality estimation trains on parallel data that includes human labels or human post-edits. 

### Unsupervised
Unsupervised quality estimation trains on monolingual data or parallel data only. Supervised quality estimation relies on labeled or post-edited data.

### Glassbox
Glassbox approaches are tied to the machine translation system itself.  A glassbox system makes a prediction based on the internal variables of the machine translation model.  It is like a confidence score.

### Blackbox
Blackbox approaches are independent of the machine translation system.  They are not necessarily trained on the same data, and can be used with any machine translation system.

#### Feature engineering
Early quality estimation approaches use machine learning with feature engineering.

Examples of specific features are the number of noun or prepositional phrases in the source and target, the number of named entities, etc. Based on these features, a QE model is built using machine learning techniques.

#### Deep learning
With the rise of deep learning, quality estimation technology resorts to deep learning architectures based on artificial neural networks.

#### Single-language-pair
Early quality estimation approaches created one model or system per language pair, similar to most machine translation systems at the time.

#### Multilingual
Multilingual quality estimation uses one model or system for many language pairs, similar to multilingual machine translation sytems.


### Frameworks, models and systems

A growing set of frameworks, models and systems are generally available.

| Name       | Tool                                     | Owner                       | Approach
| ---------- | ---------------------------------------- | --------------------------- | --------------------------- |
| QuEst++    | Framework                                | University of Sheffield     | Feature engineering, blackbox |
| DeepQuest  | Framework                                | University of Sheffield     | Deep learning, blackbox     |
| OpenKiwi   | Framework                                | Unbabel                     | Deep learning, blackbox     |
| TransQuest | Pretrained models                        | University of Wolverhampton | Deep learning, blackbox     |
| KantanQES  | Feature of machine translation API       | KantanAI                    | Glassbox                    |
| Memsource quality estimation  | Feature of translation management system | Memsource | Deep learning, blackbox    |
| ModelFront | System with API and console              | ModelFront                  | Deep learning, multilingual, blackbox |

More companies have researched quality estimation internally, but did not launch or do not provide quality estimation to others.
- Amazon
- Microsoft
- Transperfect
- Unbabel
- VMware
- eBay
- Facebook AI Research
- MusixMatch

*Note: This list is incomplete.*

### Research

In 2012, [Lucia Specia](/people/lucia-specia.md) and Radu Soricut organized the first Shared Task on Quality Estimation. In 2018, Lucia Specia, Carolina Scarton and Gustavo Henrique Paetzold published the book Quality Estimation for Machine Translation. There is also research on word-level quality estimation and paragraph-level quality estimation. In 2020, ModelFront launched a multilingual quality estimation API, Tharindu Rasinghe openly published pretrained quality estimation models and Facebook Research launched unsupervised quality estimation internally.

### Challenges

QE models are likely to guess translation quality rather than estimate it if trained with publicly available datasets.
