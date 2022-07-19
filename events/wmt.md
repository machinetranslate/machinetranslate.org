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

|     |     |
| --- | --- |
| [WMT22](wmt22.md) Eighth Conference on Machine Translation | EMNLP 2022 |
| [WMT21](wmt21.md) Seventh Conference on Machine Translation | EMNLP 2021 |
| [WMT20](wmt20.md) Sixth Conference on Machine Translation | EMNLP 2020 |
| [WMT19](wmt19.md) Fourth Conference on Machine Translation | ACL 2019 |
| [WMT18](wmt18.md) Third Conference on Machine Translation | EMNLP 2018 |
| [WMT17](wmt17.md) - Second Conference on Machine Translation | EMNLP 2017 |
| [WMT16](wmt16.md) - First Conference on Machine Translation | ACL 2016 |
| [Workshop on Statistical Machine Translation](wmt15.md) | EMNLP 2015 |
| Workshop on Statistical Machine Translation | ACL 2014 |
| Workshop on Statistical Machine Translation | ACL 2013 |
| Workshop on Statistical Machine Translation | NAACL 2012 |
| [Workshop on Statistical Machine Translation](wmt11.md) | EMNLP 2011 |
| Workshop on Statistical Machine Translation | ACL 2010 |
| Workshop on Statistical Machine Translation | EACL 2009 |
| Workshop on Statistical Machine Translation | ACL 2008 |
| Workshop on Statistical Machine Translation | ACL 2007 |
| Workshop on Statistical Machine Translation | NAACL 2006 |

{% include collapsible_toc.html %}

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

### Long-time organisers

- [Philipp Koehn](../people/philipp-koehn.md)
- [Lucia Specia](../people/lucia-specia.md)
- Barry Haddow
- Loïc Barrault
- [Ondřej Bojar](/community/people/ondrej-bojar.md)
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

<details>
<summary><h2>Definitions</summary>

### TrueSkill

**TrueSkill** is a gaming rating system. Microsoft Research originally developed it for the Xbox Live gaming community. 
For [WMT](wmt.md), TrueSkill was adapted to machine translation evaluation. During [WMT15](wmt15.md) and [WMT16](wmt16.md), TrueSkill was introduced as the human evaluation ranking for all WMT translation tasks. 

#### Process

  1. 1,000 samples are extracted from the available data.
  2. TrueSkill is run over each dataset.
  3. A rank range for each system is computed. 

### Relative ranking

From 2014 to 2016, the **relative ranking** approach was the official scoring mechanism of the WMT conference. 

#### Process

  1. Annotators use relative ranking to rate the outputs of five different systems for each input.
  2. These rankings generate compared pairs of translations.
  3. WMT produces overall system rankings using the TrueSkill algorithm. The compared pairs denote only relative ability between system pairs. They cannot be used to infer their absolute quality. 

### Direct assessment

WMT16 added **direct assessment** scoring of system outputs as an investigatory ranking. Since [WMT17](wmt17.md), the approach has been the official scoring mechanism of the conference.

Annotators use direct assessment to evaluate the system output quality relative to a reference translation.

#### Monolingual or reference-based evaluation
  
  Human assessors use **monolingual or reference-based evaluation** to rate the system output. They compare the output to the human-generated reference without considering the source input.
  
#### Bilingual or source-based evaluation
  
  Human assessors use **bilingual or source-based evaluation** to rate the source input and system output without any reference translation.
  
### Average score and z-score

**Average score and z-score** are the main scores used in WMT.
The **average z-score** has been the official ranking of the conference results since 2017.
The average z-score shows the distance between an **average score** and the mean.

#### Process

  1. Human assessment scores for translations are standardised according to each human assessor's overall mean and standard deviation.
  2. Standardised scores of a given system are computed at the segment level.
  3. With the segment-level results, the system-level average z-score is computed. The average scores for systems are computed similarly, but without any score standardisation applied.
</details>
