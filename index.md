---
nav_exclude: true
title: Machine Translate
description: Open resources and community for machine translation
permalink: /
seo:
  type: Organization
---

# Machine Translate

**Machine Translate** is building **open information and a community for machine translation**.

{% assign integration_count = 0 %}
{% for tms in site.data.integrations %}
  {% assign s = tms.api_integrations | size %}
  {% assign integration_count = integration_count | plus: s %}
{% endfor %}

<div style="display: flex; justify-content: center; gap: 20%; padding: 1em;">
  <div>
    <center>
      <a href="/apis">
        <h1>{{ site.data.apis | size }}</h1>
        APIs
      </a>
    </center>
  </div>
  <div>
    <center>
      <a href="/integrations">
        <h1>{{ integration_count }}</h1>
        integrations
      </a>
    </center>
  </div>
  <div>
    <center>
      <a href="/languages">
        <h1>{{ site.data.languages | size }}</h1>
        languages
      </a>
    </center>
  </div>
</div>

The content covers everything about machine translation, from products to research, and from history to news.


> #### Featured events
> - [AMTA 2023](/amta2023) - 8 November, online - **Call for papers deadline updated**
> - [WMT23](/wmt23) - 6-7 December, Singapore
> - [Machine translation meetup](/meetup)

>
> #### Featured articles
> - [Adaptive machine translation](/customisation/adaptive.md)
> - [Quality estimation](/quality/quality-estimation.md)
> - [Companies](/industry/companies.md)


## Stay connected

Join the community to ask and answer questions, and share your work.
Sign up for the newsletter to read news about machine translation.

<div style="display: flex; justify-content: center; gap: 20%;">
  <div>
    <center>
      <h2><a href="/community">Community</a></h2>
        <a href="/community">
          👥
        </a>
    </center>
  </div>
  <div>
    <center>
      <h2><a href="/newsletter">Newsletter</a></h2>
        <a href="/newsletter">
          📧
        </a>
    </center>
  </div>
</div>


Follow us on other platforms.

<center>
  <div class="social-links">
    {% include twitter.html %}
    {% include linkedin.html %}
    {% include facebook.html %}
  </div>
</center>

## Contributing

Machine Translate is open-source.
You can create or edit the content.

{% include contributions.html %}

<div style="display: flex; justify-content: center; gap: 20%;">
  <div>
    <center>
      👩🏻‍💻
      <h1>{{ site.github.contributors | size }}</h1>
      contributors
    </center>
  </div>
  <div>
    <center>
      ✏️
      <h1>{{ all_contributions }}</h1>
      contributions
    </center>
  </div>
</div>

[**Learn more about contributing →**](/contributing/contributing.md)

Watch and star the content source repository, browse and subscribe to issues and more!

<center>
  <div class="social-links">
    {% include github.html %}
  </div>
</center>



## About Machine Translate

Machine Translate is on a mission to make machine translation more accessible to more people.

Our mission is supported by people like you.

[**Learn more about the foundation →**](/about.md)
