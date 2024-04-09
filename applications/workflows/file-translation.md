---
nav_order: 3
grand_parent: Application areas
parent: Translation and localisation
title: File Translation
description: Translating various types of files from one language to another while preserving formatting and content
---

**File translation** refers to the process of converting data stored in a specific format on one computer or system to a different format that can be used by the same or a different processing system on another computer. This process involves translating data from the source file into a target file that can be read and processed by the target system. File translation is often necessary when transferring information systems from one computer to another, as it allows for the preservation of data integrity and functionality across different systems and platforms.

File translation can involve various file types, including text files, markdown files, HTML files, XML files, JSON files, Microsoft Office files, and image files, among others. The translation process can be manual, involving the writing of specific translation programs for each file pair, or automated using generalized translation algorithms and machine learning techniques.

The benefits of file translation include the ability to transfer information across linguistic and system barriers, expanding the reach and accessibility of information to a wider audience. File translation also enables the preservation of data integrity and functionality across different systems and platforms, ensuring that data can be used and processed effectively in its translated form.


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
