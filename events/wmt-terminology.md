---
parent: Events
title: WMT terminology 
description: Terminology used in WMT results
---

## TrueSkill

**TrueSkill** is a gaming rating system. Microsoft Research originally developed it for the Xbox Live gaming community. 
For [WMT](wmt.md), TrueSkill was adapted to machine translation evaluation. During [WMT15](wmt15.md) and [WMT16](wmt16.md), TrueSkill was introduced as the human evaluation ranking for all WMT translation tasks. 

### Process

1. 1,000 samples are extracted from the available data.
2. TrueSkill is run over each dataset.
3. A rank range for each system is computed. 

## Relative ranking

From 2014 to 2016, the **relative ranking** approach was the official scoring mechanism of the WMT conference. 

### Process

1. Annotators use relative ranking to rate the outputs of five different systems for each input.
2. These rankings generate compared pairs of translations.
3. WMT produces overall system rankings using the TrueSkill algorithm. The compared pairs denote only relative ability between system pairs. They cannot be used to infer their absolute quality. 

## Direct assessment

WMT16 added **direct assessment** scoring of system outputs as an investigatory ranking. Since [WMT17](wmt17.md), the approach has been the official scoring mechanism of the conference.

Annotators use direct assessment to evaluate the system output quality relative to a reference translation.

### Monolingual or reference-based evaluation

Human assessors use **monolingual or reference-based evaluation** to rate the system output. They compare the output to the human-generated reference without considering the source input.

### Bilingual or source-based evaluation

Human assessors use **bilingual or source-based evaluation** to rate the source input and system output without any reference translation.

## Average score and z-score

**Average score and z-score** are the main scores used in WMT.
The **average z-score** has been the official ranking of the conference results since 2017.
The average z-score shows the distance between an **average score** and the mean.

### Process

1. Human assessment scores for translations are standardised according to each human assessor's overall mean and standard deviation.
2. Standardised scores of a given system are computed at the segment level.
3. With the segment-level results, the system-level average z-score is computed. The average scores for systems are computed similarly, but without any score standardisation applied.
