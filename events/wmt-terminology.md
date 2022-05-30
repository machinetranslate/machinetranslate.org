---
parent: Events
title: WMT Terminology 
description: Terminology for understanding WMT results
---

## TrueSkill

TrueSkill is an adaptative model of competitions originally developed by Microsoft Research for the Xbox Live online gaming community.
[WMT](wmt.md) developed a variation of the TrueSkill model adapted to the human evaluation of machine translation output.
During [WMT15](wmt15.md) and [WMT16](wmt16.md), the human ranking for each task was produced using TrueSkill in the following manner:

First, 1,000 bootstrap-resampled runs are produced over all of the available data.
A rank range for each system is then computed.
To compute the rank range, the absolute rank of each system is collected in each fold and thrown out the top and bottom 2.5%.
Then systems are clustered into equivalence classes, containing systems with overlapping ranges.
The ranges yield a partial ordering over systems at the 95% confidence level.

## Relative ranking

From 2014 to 2016, the relative ranking approach was the official scoring mechanism of the WMT conference. 

In relative ranking, annotators rank five system outputs for a given segment in comparison to one another.
From these rankings, pairwise translation comparisons are generated. 
Overall system rankings are then produced by means of the TrueSkill algorithm. 

The pairwise comparisons denote only relative ability between a pair of systems and cannot be used to infer their absolute quality. 

## Direct assessment

WMT16 added direct assessment scoring of system outputs as an investigatory ranking.
Since [WMT17](wmt17.md), the approach has been the official scoring mechanism of the conference.

In direct assessment, annotators provide a direct assessment of the quality of a single machine-translated output compared to a single reference, using an analog scale. 

### Monolingual or reference-based evaluation

In this configuration, the human assessors rate the system output by comparing it to the human-generated reference without considering the source input.

### Bilingual or source-based evaluation

In this configuration, the human assessors rate the source input and system output without any reference translation.

## Average score and z-score

There are two main types of scores produced by WMT: average scores and z-scores.
The average z-score is used as the official ranking of the conference results.
The z-score shows how many standard deviations below or above the mean an average or raw score is.

To compute the z-score,
1. Human assessment scores for translations are standardized according to each human assessor’s overall mean and standard deviation score.
2. Average z-scores for individual segments belonging to a given system are computed.
3. The final overall direct assessment score for that system is computed as the average standard of its segment scores.

The average scores for systems are computed in the same way but without any score standardization applied.
