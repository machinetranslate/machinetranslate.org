---
nav_order: 3
has_children: no
title: Calls for papers
description: Calls for papers for machine translation events and publications
seo:
    type: ItemList
    name: Calls for papers for machine translation events and publications
---

{% assign current_date = "now" | date: "%Y-%m-%d" %}
{% assign all_events = site.data.events | concat: site.data.wmt_events | where_exp: "event", "event.calls_for_papers_deadline" | concat: site.data.calls_for_papers %}
{% assign sorted_events = all_events | sort: "calls_for_papers_deadline" | reverse %}


### Calls for papers

| Deadline | Publication |
| --- | --- | --- |
{%- for event in sorted_events -%}{% if current_date  < event.calls_for_papers_deadline %}
| **{{ event.calls_for_papers_deadline | date: "%d %B %Y" }}** | **[{{ event.name }}]({% if event.id -%}/{{ event.id }}{% else -%}{{ event.url }}{% endif -%})** | {% else %}
| {{ event.calls_for_papers_deadline | date: "%d %B %Y" }} | [{{ event.name }}]({% if event.id %}/{{ event.id }}{% else %}{{ event.url }}{% endif -%}) | {% endif %}{% endfor %}
| 1 October 2023 | [DNLP 2024](https://aisca2024.org/dnlp/index) |
| 10 September 2023 | [*International Journal on Natural Language Computing*](https://airccse.org/journal/ijnlc/) |
| 5 September 2023 | [WMT23](/wmt23) |
| 15 August 2023 | [AMTA 2023](/amta-2023) |
| 15 July | [MT Marathon](/mtm2023) |
| 7 July 2023 | [WAT 2023](/wat2023) |
| 16 July 2023 | [CoCo4MT 2](/coco4mt-2) |
| 15 May 2023 | [MT Summit 2023 papers](/mtsummit2023) |
| 17 April 2023 | [MT Summit 2023 workshops and tutorials](/mtsummit2023) |
| 15 April 2023 | [AmericasNLP](/americasnlp2023) |
| 31 March 2023 | [*The Role of Context in Neural Machine Translation Systems and its Evaluation*](https://sites.google.com/dcu.ie/nlecontextnmt/home) |
| 31 March 2023 | [AT4SSL 2023](/at4ssl2023) |
| 10 March 2023 | [EAMT 2023 papers](/eamt-2023) |
| 3 March 2023 | [EAMT 2023 tutorials](/eamt-2023) |
| 2 March 2023 | [LoResMT 2023](/loresmt2023) |
| 20 February 2023 | [EAMT 2023 workshops](/eamt-2023) |
| 23 December 2022 | [*Machine translation evaluation in the context of scholarly communication*](https://www.operas-eu.org/machine-translation-evaluation-in-the-context-of-scholarly-communication-open-call/) |
| 15 November 2022 | [*Web-based machine translation in language teaching*](https://calico.org/calico-journal-special-issue-machine-translation-call-for-papers/) |
| 30 September 2022 | [AAMT 2022](https://www.aamt.info/event/aamttokyo2022/aamttokyo2022-kobo/) |
| 30 September 2022 | [AmericasNLP Competition](http://turing.iimas.unam.mx/americasnlp/st.html) |
| 7 September 2022 | [WMT22](/wmt22) |
| 28 July | [MTMA22](/mtma2022) | 
| 15 July 2022 | [MTM22](/mtm2022) |
| 11 July 2022 | [WAT 2022](/wat2022) |
| 1 July 2022 | [MUMTTT 2022](/mumttt2022) |
| 30 June 2022 | [*Special Issue on Translation Platforms*](https://www.aclweb.org/portal/content/special-issue-translation-platforms) |
| 29 June 2022 | [CoCo4MT](https://sites.google.com/view/coco4mt) |
| 24 June 2022 | [EMNLP 2022](https://2022.emnlp.org/calls/papers/Overview) |
| 13 June 2022 | [AMTA 2022](/amta-2022) |
| 6 June 2022 | [Literary Translation and AI: assessing changes in translation theory, practice and creativity](/lit-translation-and-ai) |
| 1 June 2022 | [Special issue on Translation Automation and Sustainability](https://jostrans.org/2b.3%20Jostrans%20SI%2041.pdf) |
| 1 May 2022 | [Automatic Simultaneous Translation 3](https://autosimtrans.github.io/cfp) |
| 1 April 2022 | [*The impact of Machine Translation in the Audiovisual Translation environment*](https://lans-tts.uantwerpen.be/index.php/LANS-TTS/announcement/view/21) |
| 1 April 2022 | [EAMT 2022](/eamt-2022) |
| 15 March 2022 | [NETTT 2022](/nettt2022) |
| 13 March 2022 | [IWSLT 2022](/iwslt2022) |
| 15 January | [NAACL 2022](https://2022.naacl.org/calls/papers/#paper-submission-details) |