---
parent: Workflows
title: Hybrid translation
description: Workflow with both human translations and pure machine translations
---

In a **hybrid translation** workflow, some raw machine translations are never seen or touched by a human translator.

Hybrid translation can be faster and cheaper than full human [post-editing](post-editing.md).
It requires machine translation to be accurate enough that a signification portion of the machine translations are usable as-is.

The key technology for a hybrid translation workflow is [**translation risk prediction**](/quality/quality-estimation.md).

Each machine translation is automatically classified as high-risk or low-risk, based on whether it is below or above the chosen risk **threshold**.

A low-risk machine translation is machine-approved as-is, while a high-risk translation is still sent to a human translator for post-editing.

In the TMS and CAT tool, the machine-approved machine translations are visible but locked, just like translation memory matches.
