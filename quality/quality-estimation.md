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

### Granularity

QE can be performed at various levels: 
* word-level
* phrase-level
* sentence-level
* document-level

Depending on the granularity level, QE results can be used for various purposes. 
Based on word-, phrase- and sentence-level QE, they can indicate whether a translation is worth being post-edited. 
Whereas document-level QE ranks whether a translation can be used in fully automated scenarios where no post-editing can be performed.  
