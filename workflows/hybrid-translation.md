---
parent: Workflows
title: Hybrid translation
description: Workflow with both human translations and pure machine translations
---

In a **hybrid translation** workflow, some raw machine translations are never seen or touched by a human translator.

Hybrid translation can be faster and cheaper than full human [post-editing](post-editing.md).

Hybrid translation requires machine translation to be accurate enough that a signification portion of the machine translations are usable as-is.

Typically the decision is at the segment level.

> ### Workflow diagram
> The hybrid translation workflow was first presented by Microsoft, VMWare and [Unbabel](/industry/companies.md#unbabel).
>
> ##### Slide from a [ModelFront](/industry/companies.md#modelfront) presentation
> <img title='Hybrid translation workflow' src='/workflows/hybrid-translation-workflow.png' width='700' style='padding: 1em;' />

Each machine translation is automatically classified as high-risk or low-risk, based on whether it is below or above the chosen risk **threshold**.

A low-risk machine translation is machine-approved as-is.  A high-risk translation is still sent to a human translator for post-editing.

In the TMS and CAT tool, the machine-approved machine translations are handled like translation memory matches.  They are either locked or marked as approved.

### Technology

The key technology for a hybrid translation workflow is [**translation risk prediction**](/quality/quality-estimation.md).
