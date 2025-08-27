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

The most common type of customisation is [fine-tuning](/fine-tuning) on [parallel data](/parallel-data).

{% assign customisable_apis = '' | split: ',' %}

{% for api in site.data.apis %}
  {% if api.custom_languages or api.glossary or api.formality or api.adaptive or api.fine-tuning or api.prompt_required %}
    {% unless customisable_apis contains api %}
      {% assign customisable_apis = customisable_apis | push: api %}
    {% endunless %}
  {% endif %}
{% endfor %}


{% assign customisable_qe_apis = site.data.quality_estimation | where: "customisation" , true %}

{{ customisable_apis | size }} machine translation APIs and {{ customisable_qe_apis | size }} quality estimation APIs support customisation.


<h2>Machine translation</h2>
  <details>
    <summary>
      <strong>{{ customisable_apis | size }}</strong> machine translation APIs support customisation.
      <p class="preview hint">
        {{ customisable_apis | slice: 0, 5 | map: 'name' | join: ', ' }}
        {% if customisable_apis.size > 5 %}, …{% endif %}
      </p>
    </summary>
    <ul>
    {% for api in customisable_apis %}
      <li>
          <a href="/{{ api.id }}">{{ api.name }}</a> {% if api.plugin %}(plugin){% endif %}
            {% if api.custom_languages or api.fine-tuning %}| <strong>fine-tuning</strong> support{% endif %}
            {% if api.glossary %}| <strong>glossary</strong> support{% endif %}
            {% if api.formality %}| <strong>formality</strong> support{% endif %}
            {% if api.adaptive %}| <strong>adaptive</strong> support{% endif %}
            {% if api.prompt_required %}| <strong>prompt</strong> support{% endif %}
      </li>
    {% endfor %}
    </ul>
  </details>

<h2>Quality estimation</h2>
  <details>
    <summary>
      <strong>{{ customisable_qe_apis | size }}</strong> quality estimation APIs support customisation.
      <p class="preview hint">
        {{ customisable_qe_apis | slice: 0, 5 | map: 'name' | join: ', ' }}
        {% if customisable_qe_apis.size > 5 %}, …{% endif %}
      </p>
    </summary>
    <ul>
    {% for qe in customisable_qe_apis %}
      <li>
        <a href="/{{ qe.id }}">{{ qe.name }}</a> {% if qe.plugin %}(plugin){% endif %}
            | <strong>fine-tuning</strong> support
      </li>
    {% endfor %}
    </ul>
  </details>

