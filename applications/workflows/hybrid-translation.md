---
nav_order: 2
grand_parent: Application areas
parent: Translation and localisation
title: Hybrid translation
description: Workflow with both human translations and pure machine translations
---

In a **hybrid translation** workflow, some raw machine translations are never seen or edited by a human translator.

Hybrid translation can be faster and cheaper than full human [post-editing](/post-editing).

Hybrid translation requires good machine translation.
A signification portion of the machine translated segments should be usable as-is.

> ### Workflow diagram
> The hybrid translation workflow was first presented by Microsoft, VMWare and [Unbabel](/unbabel).
>
> ##### Slide from a [ModelFront](/quality-estimation/modelfront) presentation
> <img title='Hybrid translation workflow' src='/applications/workflows/hybrid-translation-workflow.png' width='700' style='padding: 1em;' />

A risk **threshold** is set.
Each new machine translation is automatically classified as high-quality or low-quality.

A high-quality machine translation is used as-is and skips human post-editing.

A low-quality translation is still sent to a human translator for post-editing.

In the translation management system (TMS) and computer-aided translation (CAT) tool, the high-quality machine translations are handled like exact matches from the translation memory.
They are marked as translated or approved, and potentially even locked.

### Technology

The key technology for a hybrid translation workflow is translation [**quality prediction**](/quality-estimation), which is known as *machine translation quality estimation* in the [research](/building-and-research) world.

### Adoption

At first, companies like Microsoft, [Unbabel](/unbabel), VMWare and Wayfair implemented hybrid translation by researching and developing their own machine translation quality estimation.

With the launch of the [ModelFront](/quality-estimation/modelfront) translation quality prediction API, more companies started to adopt the hybrid translation workflow within commercially available translation management systems.


---

### See also

- [**Quality estimation**](/quality-estimation)
