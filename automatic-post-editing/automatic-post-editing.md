---
nav_order: 67
has_children: true
has_toc: false
permalink: /:basename
# parent: Building and research
title: Automatic post-editing
description: Automatic post-editing of machine translation
---

**Automatic post-editing (APE)** is the task of automatically correcting the output of a machine translation system. Like in manual human [post-editing](/post-editing), the objective is to improve the quality of a machine translation output. For example, automatic post-editing can be used to correct errors or apply a certain style.
Automatic post-editing systems should meet multiple requirements:
- detect and fix machine translation errors
- avoid making overcorrections, especially those that add new errors


### Evolution
The evolution of automatic post-editing systems is similar to that of machine translation. The first systems took [rule-based approaches](/rule-based-machine-translation), later systems took [statistical approaches](/statistical-machine-translation) and then [neural approaches](/neural-machine-translation).


### Use cases
Automatic post-editing can be applied in several use cases:
- fixing errors in machine translation outputs
- adapting the output of a machine translation system to a custom domain
- providing alternative translation suggestions in translation tools, for example [OpenTIPE](https://aclanthology.org/2023.acl-demo.19.pdf)


### Training
Automatic post-editing systems are usually trained with parallel triplets containing
- a source text
- the machine-translated version of this source text
- the post-edited version of the machine-translated text

| Source | Machine translation | Human post-edited translation|
| How are you?	| ¿Cómo estás?	| ¿Cómo está?|
| Computer| Computadora| Ordenador|
| … | … | …|


### Datasets
The datasets from the [quality estimation](/quality-estimation) shared task at [WMT](/wmt) can be used for training and evaluating automatic post-editing systems.

When human post-edited translations are not available, synthetic post-editing data can be created from ordinary translation data. For example, [eSCAPE (Synthetic Corpus for Automatic Post-Editing)]( https://aclanthology.org/L18-1004.pdf) creates synthetic data by inserting a machine translation.


### Evaluation
Automatic post-editing systems can be evaluated like machine translation systems:

-	Automatic, reference-based evaluation [metrics](/metrics), like [TER](/ter) or [BLEU](/bleu)
-	[Human evaluation](/human-evaluation-metrics), like [direct assessment](/human-evaluation-metrics#direct-assessment)

Evaluation reveals how many sentences were improved. Precision can be calculated by dividing the number of improved sentences by the total number of modified sentences. Another common metric is the average number of edits per segment.

---

{% assign ape_pages = "" | split: "" %}

{% for page in site.pages %}
  {% if page.path contains 'automatic-post-editing/' %}
    {% unless page.path == 'automatic-post-editing/automatic-post-editing.md' %}
        {% assign ape_pages = ape_pages | push: page %}
    {% endunless %}
  {% endif %}
{% endfor %}

{% assign max_count = 0 %}
{% for page in ape_pages %}
  {% assign lang_count = page.supported_languages | size | default: 0 %}
  {% if lang_count > max_count %}
    {% assign max_count = lang_count %}
  {% endif %}
{% endfor %}

{% for count in (0..max_count) reversed -%}
  {% for page in ape_pages -%}
    {% assign lang_count = page.supported_languages | size | default: 0 -%}
    {% if lang_count == count %}
- [{{ page.title }}](/automatic-post-editing/{{ page.id }}) {% if page.active == false %}`inactive`{% endif %}{% endif %}{% endfor %}{% endfor %}