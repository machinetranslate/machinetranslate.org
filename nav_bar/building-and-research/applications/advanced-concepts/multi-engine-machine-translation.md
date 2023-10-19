---
parent: Building and research
nav_order: 161
title: Multi-engine machine translation
description: Machine translation with multiple systems
---

**Multi-engine machine translation** is an approach for evaluating and picking a machine translation engine.
With multi-engine machine translation, the same input is sent to multiple machine-translation systems.
The translations are then ranked to select the best one.

The challenges of multi-engine machine translation are related to the translation output and the implementation:
- Lack of consistency across segments
- Increased complexity, latency, and cost


### Goals

The goal of multi-engine machine translation is to get higher quality translations than any single engine could achieve.
