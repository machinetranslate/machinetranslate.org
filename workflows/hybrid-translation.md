---
nav_order: 2
grand_parent: Application areas
parent: Translation and localisation
title: Hybrid translation
description: Workflow with both human translations and pure machine translations
---

In a **hybrid translation** workflow, some raw machine translations are never seen or touched by a human translator.

Hybrid translation can be faster and cheaper than full human [post-editing](post-editing.md).

Hybrid translation requires good machine translation.
A signification portion of the machine translated segments should be usable as-is.

> ### Workflow diagram
> The hybrid translation workflow was first presented by Microsoft, VMWare and [Unbabel](/industry/companies.md#unbabel).
>
> ##### Slide from a [ModelFront](/industry/companies.md#modelfront) presentation
> <img title='Hybrid translation workflow' src='/workflows/hybrid-translation-workflow.png' width='700' style='padding: 1em;' />

A risk **threshold** is set.
Each new machine translation is automatically classified as high-risk or low-risk.

A low-risk machine translation is machine-approved as-is.

A high-risk translation is still sent to a human translator for post-editing.

In the translation management system (TMS) and computer-aided translation (CAT) tool, the machine-approved machine translations are handled like translation memory matches.
They are either locked or marked as approved.

### Technology

The key technology for a hybrid translation workflow is [**translation risk prediction**](/quality/quality-estimation.md), which is known as *quality estimation* in the research world.

### Adoption

The first companies to adopt a hybrid translation workflow built with quality estimation internally were:
- Microsoft
- Unbabel
- VMWare
- Wayfair

---

### See also

- [**Quality estimation**](/quality/quality-estimation.md)
