---
parent: Building and research
nav_order: 165
title: Quality estimation
description: Machine translation quality estimation
featured: true
redirect_from:
  - /quality-prediction
---

Machine translation **quality estimation** (**QE** or **MTQE**) or machine translation **quality prediction** (**QP** or **MTQP**) is the task of automatically predicting the quality of machine translation output.

| Original                     | Translation                    | Quality prediction   |
| -----------------------------| -------------------------------| ---------------------|
| `English` `July 30th, 2021`  | `French` `30 juillet 2021`     | `Good`               |
| `English` `This is my home.` | `Spanish` `Este es mi inicio.` | `Bad`                |

Quality estimation does not require human reference translations, so it is useful for new content.  It uses machine learning to provide predictions that are relatively accurate at the segment level.

[Quality evaluation](/quality/quality-evaluation.md) [metrics](/quality/metrics.md) like [BLEU](/quality/metrics/bleu.md) require human reference translations against which to compare the machine translation output.  But for new content, there are no human reference translations available.


### Use cases

Quality estimation has offline and production use cases:

* [Hybrid translation](/workflows/hybrid-translation.md)
* Estimating [post-editing](/workflows/post-editing.md) effort
* Validating final human translations
* Comparing machine translation systems or translation models
* Filtering training data for machine translation

The main use case is hybrid translation.


### Granularity

Quality estimation is most commonly at the segment-level, for example a sentence.

* Word-level
* Phrase-level
* Sentence-level
* Document-level

Sentence-level scores can be aggregated into paragraph-level scores or document-level scores.
Word-, phrase- and sentence-level scores can indicate if a machine translation output needs to be post-edited.
Document-level scores indicate if a machine translation output can be used without human post-editing.

---

In 2012, [Lucia Specia](/people/lucia-specia.md) and Google researcher Radu Soricut organized the first *Shared Task on Quality Estimation*.

In 2018, Lucia Specia, Carolina Scarton and Gustavo Henrique Paetzold published the book *Quality Estimation for Machine Translation*.
There was research on word-level quality estimation and paragraph-level quality estimation.

In 2020, [ModelFront](/industry/companies.md#modelfront) launched a multilingual quality estimation API.
Tharindu Ranasinghe released pretrained models.
Facebook Research launched unsupervised quality estimation internally.

A growing set of frameworks, models, and systems are generally available.

### Frameworks

Frameworks from academia and industry are available as open-source code and models.

The first framework, QuEst, was released in 2013.

| Name       | Owner                       | Approach
| ---------- | --------------------------- | --------------------------- |
| [QuEst](https://github.com/lspecia/quest) | University of Sheffield | Feature engineering |
| [QuEst++](https://www.quest.dcs.shef.ac.uk/) | University of Sheffield     | Feature engineering |
| [DeepQuest](https://github.com/sheffieldnlp/deepQuest) | University of Sheffield     | Deep learning     |
| [OpenKiwi](https://github.com/Unbabel/OpenKiwi) | Unbabel                     | Deep learning     |
| [TransQuest](https://github.com/TharinduDR/TransQuest) | Tharindu Ranasinghe, University of Wolverhampton | Deep learning |

TransQuest also includes pretrained models.  The models were pretrained with [WMT](/associations/wmt.md) data.


### Providers

ModelFront launched a standalone production system for quality estimation.
By 2020, it was generally available and supported more than 10000 language pairs.
It is provided as an API, so it can be integrated into other systems and products.

There are also providers that offer a quality estimation feature within another product.

| Provider | Product | Availability | Approach |
| --- | --- | --- | --- |
| [KantanAI](/industry/companies.md#kantanmt) | [KantanQES](https://www.kantanai.io/kantanqes-home/) | Feature of machine translation API | Glassbox |
| [ModelFront](/industry/companies.md#modelfront) | [ModelFront quality prediction](https://modelfront.com) | Product with cloud API and console | Deep learning, multilingual, blackbox |
| [Omniscien](/industry/companies.md#omniscien-technologies) | [Translation Confidence Scoring and Quality Estimates](https://omniscien.com/products/language-studio/) | Feature of machine translation API | Glassbox |


### Features and integrations

A few translation management systems have launched generally available features for quality estimation.

| Product | Feature | Provider |
| ---| --- | --- |
| [KantanStream](/industry/companies.md#kantanmt) | [KantanQES](https://www.kantanai.io/kantanqes-home/) | KantanAI |
| PhraseTMS | [MT quality estimation](https://support.phrase.com/hc/en-us/articles/5709672289180-MT-Quality-Estimation-TMS-)  | Phrase |
| [translate5](https://translate5.net) | Risk prediction | ModelFront |
| [GlobalDoc](https://globaldoc.com) LangXpert | Effort estimation | ModelFront |

translate5 is open-source.


### Internal systems

More companies have researched or launched quality estimation internally.
They do not provide quality estimation to others.
- Amazon
- Microsoft
- VMware
- Facebook AI Research
- eBay
- SAP
- MusixMatch
- Wayfair
- Unbabel
- Transperfect
- CrossLang
- Fair Trade Translation

*Note: This list is incomplete.*

## Types

Quality estimation is typically implemented as classification or regression.

### Supervised
Supervised quality estimation trains on parallel data that includes human labels or human post-edits.

### Unsupervised
Unsupervised quality estimation trains on monolingual data or parallel data only.
Supervised quality estimation relies on labeled or post-edited data.

### Glassbox
Glassbox approaches are tied to the machine translation system itself.
A glassbox system makes a prediction based on the internal variables of the machine translation model.
It is like a confidence score.

### Blackbox
Blackbox approaches are independent of the machine translation system.
They are not necessarily trained on the same data, and can be used with any machine translation system.

## Approaches

### Feature engineering
Early quality estimation approaches use machine learning with feature engineering.

Examples of specific features are the number of noun or prepositional phrases in the source and target, the number of named entities, etc.
Based on these features, a quality estimation model is built using machine learning techniques.

### Deep learning
With the rise of deep learning, quality estimation technology resorts to deep learning architectures based on artificial neural networks.

### Single-language-pair
Early quality estimation approaches created one model or system per language pair, similar to most machine translation systems at the time.

### Multilingual
Multilingual quality estimation uses one model or system for many language pairs, similar to multilingual machine translation systems.

---

### See also

- [Hybrid translation](/workflows/hybrid-translation.md)
