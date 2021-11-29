---
description: Quality estimation for machine translation
---

# Quality Estimation

**Quality estimation** \(**QE**\) is a method for automatically assessing the quality of the machine translation output without human intervention. QE scores are independent from the expected translation output.

English original:
`July 30th, 2021`

Translation into French:
`30 juillet 2021`

Quality estimation:
`Good`



English original:
`This is my home.`

Translation into Spanish:
`Este es mi inicio.`

Quality estimation:
`Bad`


Evaluation metrics like BLEU or post-editing distance require human reference translations, but there are no human reference translations for new content.

QE predicts the quality based on either specific features or neural networks. Examples of specific features are the number of noun or prepositional phrases in the source and target, the number of named entities, etc. Based on these features, a QE model is built using machine learning techniques.


### Use cases

Quality estimation has offline and production use cases:
- Comparing machine translation systems or translation models
- [Hybrid translation](workflows/hybrid-translations.md)
- Estimating [post-editing](wordflows/post-editing.md) effort
- Validating final human translations
- Filtering training data for machine translation


### Granularity

- Word-level
- Phrase-level
- Sentence-level
- Document-level

Sentence-level scores can be aggregated into paragraph-level scores or document-level scores.
Word-, phrase- and sentence-level scores can indicate if a machine translation output needs to be post-edited. Document-level scores indicate if a machine translation output can be used without human post-editing.

### Approaches

Supervised quality estimation trains on parallel data that includes human labels or human post-edits. Unsupervised quality estimation trains on monolingual data or parallel data only.
Supervised quality estimation relies on features. Glass-box features are extracted from the machine translation system itself. Blackbox features are system-independent.

Early quality estimation approaches use machine learning with feature engineering. With the rise of deep learning, quality estimation technology resorts to deep learning architectures based on artificial neural networks.

Multilingual quality estimation trains one model or system for many language pairs.

### Systems

| Name  | Tool | Developer  |
|---|---|---|
| QuEst++ | Framework | University of Sheffield |
| DeepQuest | Framework | University of Sheffield |
| OpenKiwi | Framework | Unbabel |
| TransQuest | Pretrained models | University of Wolverhampton |
| KantanQES | Feature of machine translation API | KantanAI |
| ModelFront | API | ModelFront |


### Research

In 2012, [Lucia Specia](people/lucia-specia.md) and Radu Soricut organized the first Shared Task on Quality Estimation.
In 2018, Lucia Specia, Carolina Scarton and Gustavo Henrique Paetzold published the book Quality Estimation for Machine Translation.
There is also research on word-level quality estimation and paragraph-level quality estimation.
In 2020, ModelFront launched a multilingual quality estimation API, Tharindu Rasinghe openly published pretrained quality estimation models and Facebook Research launched unsupervised quality estimation internally.

### Challenges

QE models are likely to guess translation quality rather than estimate it if trained with publicly available datasets.
