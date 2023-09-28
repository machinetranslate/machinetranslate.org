---
nav_order: 1
parent: Features
has_children: true
title: Customisation
description: Customisation of machine translation
seo:
  name: Customisation of machine translation
---

**Customisation** of machine translation is used to accurately translate for the domain and reflect a specific terminology and style.

The most common type of customisation is [fine-tuning](fine-tuning.md) on [parallel data](parallel-data.md).

{% assign customisable_apis_size = site.data.apis | where: "customisation_languages", true | concat: site.data.apis | where: "glossary", true | concat: site.data.apis | where: "formality", true | concat: site.data.apis | where: "adaptive", true | concat: site.data.apis | where: "fine-tuning", true %}

{% assign customisable_qe_apis_size = site.data.quality-estimation | where: "customisation" , true %}

{{ customisable_apis_size | size }} machine translation APIs and {{ customisable_qe_apis_size | size }} quality estimation APIs support customisation.


<h2>Machine translation</h2>
  <details>
    <summary>
      <strong>{{ customisable_apis_size | size }}</strong> machine translation APIs support customisation.
      <p class="preview hint">
        {{ customisable_apis_size | slice: 0, 5 | map: 'name' | join: ', ' }}
        {% if customisable_apis_size.size > 5 %}, …{% endif %}
      </p>
    </summary>
    <ul>
    {% for api in customisable_apis_size %}
      <li>
          <a href="/{{ api.slug }}">{{ api.name }}</a> {% if api.plugin %}(plugin){% endif %}
            {% if api.custom %}| <strong>fine-tuning</strong> support{% endif %}
            {% if api.glossary %}| <strong>glossary</strong> support{% endif %}
            {% if api.formality %}| <strong>formality</strong> support{% endif %}
      </li>
    {% endfor %}
    </ul>
  </details>

<h2>Quality estimation</h2>
  <details>
    <summary>
      <strong>{{ customisable_qe_apis_size | size }}</strong> quality estimation APIs support customisation.
      <p class="preview hint">
        {{ customisable_qe_apis_size | slice: 0, 5 | map: 'name' | join: ', ' }}
        {% if customisable_qe_apis_size.size > 5 %}, …{% endif %}
      </p>
    </summary>
    <ul>
    {% for qe in customisable_qe_apis_size %}
      <li>
        <a href="/{{ qe.slug }}">{{ qe.name }}</a> {% if qe.plugin %}(plugin){% endif %}
            | <strong>fine-tuning</strong> support
      </li>
    {% endfor %}
    </ul>
  </details>

