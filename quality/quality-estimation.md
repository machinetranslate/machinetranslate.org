# Quality Estimation

Quality estimation (QE) is a reference-independent method to provide a quality indication for machine translation output. 
Unlike quality evaluation with reference-based metrics, QE provides an estimate of translation quality without comparing it to a gold standard. 
It predicts the quality based on either specific features, such as the number of noun or prepositional phrases in the source and target, 
the number of named entities, etc., or neural networks. Based on these features, a QE model is built using machine learning techniques. 
The model yields a score that represents the estimation of the translation quality. 

### Motivation
QE is less time and labor-intensive as opposed to automatic MT evaluation metrics given it does not require human reference translation. 
QE helps users understand whether the translation is reliable in cases when the user does not have a command of the source language. 
One of the challenges is that QE models are likely to guess translation quality rather than estimate it if trained on publicly available datasets. 

QE can be performed at various levels of granularity: 
* word-level
* phrase-level
* sentence-level
* document-level

QE at the word level assigns a score for words based on whether the correct translation was produced or not, or whether there are missing words. 

Phrase-level QE is concerned with predicting the quality of translated sequences of adjacent words based on incorrect word order or the number of missing words. 

Sentence-level QE aims to predict if a translation is good enough or needs to be edited. The score can also be assigned based on the number of edits needed. 

QE at the document level assigns a quality score by measuring the impact of accuracy and fluency errors on the overall meaning of the whole document. 
