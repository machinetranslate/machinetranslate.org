---
nav_order: 3
grand_parent: Application areas
parent: Translation and localisation
title: File Translation
description: Translating various types of files from one language to another while preserving formatting and content
---

**File translation** is the translation of data from an input file into an output file.
File translation preserves the file data integrity and functionality across different systems and platforms.

## File Types

File translation can involve various file types:

- Text
- Markdown
- HTML
- XML
- JSON
- Microsoft Office
- Image

The translation process can be manual, involving the writing of specific translation programs for each file pair, or automated using generalised translation algorithms and machine learning techniques.

{% assign apis = site.data.apis | where_exp: 'api', 'api.file_translation == true' %}

### API Support
<details>
<summary>{{apis.size}} machine translation APIs offer file translation</summary>

{% capture api_content %}
{% for api in apis %}
- [{{ api.name }}](/{{ api.id }})
{% endfor %}
{% endcapture %}

{{ api_content | markdownify }}

</details>
