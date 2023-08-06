---
nav_exclude: true
community_search_exclude: true
title: Machine Translate
description: Open resources and community for machine translation
permalink: /
seo:
  type: Organization
---

# Machine Translate

**Machine Translate** is building **open information** and **community** for machine translation.

{% assign integration_count = 0 %}
{% for tms in site.data.integrations %}
  {% assign s = tms.api_integrations | size %}
  {% assign integration_count = integration_count | plus: s %}
{% endfor %}

<style>
  .big {
    font-size: 2em;
    background: -webkit-linear-gradient(45deg, #DA291C, #ed7f78, #DA291C, #71150f);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
</style>

<div style="display: flex; justify-content: center; gap: 20%; padding: 1em;">
  <div>
    <center>
      <a href="/apis">
        <span class="big">{{ site.data.apis | size }}</span><br/>
        APIs
      </a>
    </center>
  </div>
  <div>
    <center>
      <a href="/integrations">
        <span class="big">{{ integration_count }}</span><br/>
        integrations
      </a>
    </center>
  </div>
  <div>
    <center>
      <a href="/languages">
        <span class="big">{{ site.data.languages | size }}</span><br/>
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

> #### Featured articles
> - [Integrations](/integrations/integrations.md)
> - [Features](/products-and-applications/features.md)
> - [Adaptive machine translation](/customisation/adaptive.md)
> - [Quality estimation](/quality/quality-estimation.md)


## Stay connected

Join the community to ask and answer questions, and share your work.

[**Join the community →**](/community.md)

<div style="display: flex; justify-content: center; gap: 20%;">
  <div>
    <center>
      <a href="/community">
        👥<br/>
        <span class="big">Community</span>
      </a><br/>
      <span class="hint">700+ members</style>
    </center>
  </div>
</div>

Sign up to the newsletter to catch key news of the month.

[**Get the newsletter →**](/newsletter.md)

<div>
  <div>
    <center>
      <a href="/newsletter">
        📧<br/>
        <span class="big">Newsletter</span><br/>
      </a><br/>
      <span class="hint">1000+ readers</style>
    </center>
  </div>
</div>

Follow Machine Translate on other platforms.

<center>
  <div class="social-links">
    {% include twitter.html %}
    {% include linkedin.html %}
    {% include facebook.html %}
  </div>
</center>


---


## About Machine Translate

Machine Translate is on a mission to make machine translation more accessible to more people.

Our mission is supported by people like you.

[**About the foundation →**](/about.md)

Machine Translate is open-source.
You can create or edit the content.

{% include contributions.html %}

<div style="display: flex; justify-content: center; gap: 20%;">
  <div>
    <center>
      👩🏻‍💻<br/>
      <span class="big">{{ site.github.contributors | size }}</span><br/>
      contributors
    </center>
  </div>
  <div>
    <center>
      ✏️<br/>
      <span class="big">{{ all_contributions }}</span><br/>
      contributions
    </center>
  </div>
</div>

Watch and star the content source repository, browse and subscribe to issues and more!

[**Contributing →**](/contributing/contributing.md)

<center>
  <div class="social-links">
    {% include github.html %}
  </div>
</center>
