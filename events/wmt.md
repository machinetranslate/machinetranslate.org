---
parent: Events
title: WMT
description: Conference on Machine Translation
name: WMT
---

**WMT** is the main event for machine translation and machine translation research.
The conference is held annually in connection with larger conferences on natural language processing.

> The conference aims to bring together academic scientists, researchers and industry representatives to exchange and share their experiences and research results. WMT plays a key role for the entire industry of computational linguistics and machine translation.

In 2006, the first **Workshop on Machine Translation** was held at the NAACL (North American Chapter of the Association for Computational Linguistics Annual Meeting).

In 2016, with the rise of [neural machine translation](../approaches/neural-machine-translation.md), WMT became a conference of its own.
The **Conference on Machine Translation** is still mainly known as *WMT*.

Universities, research laboratories and big technology companies consistently participate in the conference and are represented in the organising committee.

{% include collapsible_toc.html %}

## Events

|     |     |     |
| :-: | :-: | :-: |
| **[WMT22](wmt22.md)** | Eighth Conference on Machine Translation | EMNLP 2022 |
| [WMT21](wmt21.md) | Seventh Conference on Machine Translation | EMNLP 2021 |
| [WMT20](wmt20.md) | Sixth Conference on Machine Translation | EMNLP 2020 |
| [WMT19](wmt19.md) | Fourth Conference on Machine Translation | ACL 2019 |
| [WMT18](wmt18.md) | Third Conference on Machine Translation | EMNLP 2018 |
| [WMT17](wmt17.md) | Second Conference on Machine Translation | EMNLP 2017 |
| [WMT16](wmt16.md) | First Conference on Machine Translation | ACL 2016 |
| [WMT15](wmt15.md) | Workshop on Statistical Machine Translation | EMNLP 2015 |
| [WMT14](wmt14.md) | Workshop on Statistical Machine Translation | ACL 2014 |
| [WMT13](wmt13.md) | Workshop on Statistical Machine Translation | ACL 2013 |
| [WMT12](wmt12.md) | Workshop on Statistical Machine Translation | NAACL 2012 |
| [WMT11](wmt11.md) | Workshop on Statistical Machine Translation | EMNLP 2011 |
| WMT10 | Workshop on Statistical Machine Translation | ACL 2010 |
| WMT09 | Workshop on Statistical Machine Translation | EACL 2009 |
| WMT08 | Workshop on Statistical Machine Translation | ACL 2008 |
| WMT07 | Workshop on Statistical Machine Translation | ACL 2007 |
| WMT06 | Workshop on Statistical Machine Translation | NAACL 2006 |

## Shared tasks

WMT includes competitions on different aspects of machine translation.
These competitions are known as *shared tasks*.

Typically, the task organisers provide datasets and instructions.
Teams submit the output of their systems.
The submissions are ranked with human evaluation.
The results of the competition are ready before the conference takes place.

During the main conference, researchers present the results of the shared tasks and winners are announced.

WMT started in 2006 with a *translation* task.
In the following years, WMT included themes on all aspects of machine translation, corpus preparation, training, and evaluation.

The main task is the *General machine translation task*.
Until 2022, it was known as the *News task* because traditionally the content to be translated was news articles.

### Recurrent tasks

### Translation tasks

- General machine translation task (former News task)
- Biomedical translation task
- Multimodal translation task
- Unsupervised and very low resource translation task
- Lifelong learning in machine translation task
- Chat translation task
- Life-long learning in machine translation task
- Machine translation using terminologies task
- Sign language translation task
- Robustness translation task
- Triangular machine translation task
- Large-scale multilingual machine translation task

#### Evaluation tasks

- Metrics task
- Quality estimation task

#### Other tasks

- Automatic post-editing task

#### Discontinued tasks

- Medical text translation task
- Pronoun translation task
- Bilingual document alignment
- Similar language translation task
- Multilingual low-resource translation task for Indo-European languages
- Tuning task
- Parallel corpus filtering task
- Task on training of neural machine translation
- Task on bandit learning for machine translation

The published results from the shared tasks and the data sets released for WMT are standard benchmarks across machine translation research.

## Organisers
**Organisers** are the people responsible for the contents for the main event and the contents, guidelines, datasets and results for each shared task.

Some people have been organisers over many years:
- [Philipp Koehn](../people/philipp-koehn.md)
- Barry Haddow
- Loïc Barrault
- [Ondřej Bojar](/community/people/ondrej-bojar.md)
- [Lucia Specia](../people/lucia-specia.md)
- Marco Turchi
- Matt Post
- Rajen Chatterjee
- Christof Monz
- Matteo Negri
- Matthias Huck
- Christian Federmann
- Christof Monz
- Yvette Graham
- Mariana Neves
- Tom Kocmi

<details markdown=1>

<summary markdown=1>

## Evaluation
</summary>

### Average score and average z-score

For the **average score**, human assessment scores for translations are standardised according to each human assessor's overall mean and standard deviation.  Then a system-level score is computed.

**Average z-score** is a normalised version.  It shows the distance between the average score for a system and the mean average score across all systems.

Average score and average z-score are the main metrics used in the results for the translation shared task since WMT17.


### TrueSkill

**TrueSkill** is a gaming rating system. Microsoft Research originally developed it for the Xbox Live gaming community. 
For WMT, TrueSkill was adapted to machine translation evaluation.
For WMT14, WMT15 and WMT16, TrueSkill was used as the human evaluation ranking for all translation shared tasks.

### Relative ranking
In **relative ranking**, for each input, humans rank the outputs from all systems.
  
There is no absolute score or label, so there is no measure of absolute quality.
  
The sequence-level rankings are used to calculate system-level rankings, for example with TrueSkill.

Relative ranking was the official ranking for the translation shared task at from WMT07 to WMT16.


### Direct assessment
In **direct assessment**, for each input, humans rate the output from each system with an absolute score or label.

The sequence-level ratings can then be used to calculate system-level ranking.

Direct assessment was first added as investigatory ranking for WMT16.
Direct assessment is the official ranking for the translation shared task since WMT17.

There are different types of direct assessment.
- Monolingual: Human raters see the system output only.
- Bilingual: Human raters see the system input and output.
- Reference-based: Human raters see the system output and a reference output.


</details>
