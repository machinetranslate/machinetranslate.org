---
parent: Input modes
nav_order: 2
has_toc: false
title: Speech
description: Speech input to machine translation APIs
---

**Speech input**, also known as **voice input** or **audio input**, is a feature of machine translation APIs required for speech translation.

There are different types of speech translation.

- Live (simultaneous) speech translation
- Offline (asynchronous) speech translation

Speech input can be combined with different types of output.

- Speech-to-speech machine translation (dubbing)
- Speech-to-text machine translation (subtitles)

Often, speech recognition (transcription) and translation are separate APIs or API calls, that can be combined to effectively support speech translation.

Speech translation APIs are typically slower than [text](/text) translation APIs.

{% assign apis = site.data.apis | where_exp: 'api', 'api.inputs contains "speech"' %}

### API support
<details>
<summary>{{apis.size}} machine translation APIs support speech translation.</summary>

{% capture api_content %}
{% for api in apis %}
- [{{ api.name }}](/{{ api.id }})
{% endfor %}
{% endcapture %}

{{ api_content | markdownify }}
</details>