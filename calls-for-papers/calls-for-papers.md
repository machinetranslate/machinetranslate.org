---
nav_order: 3
has_children: no
title: Calls for papers
description: Calls for papers for machine translation events and publications
seo:
    type: ItemList
    name: Calls for papers for machine translation events and publications
---

### Calls for papers

<table>
  <thead>
    <tr>
      <th>Deadline</th>
      <th>Publication</th>
      <th>Organisers</th>
    </tr>
  </thead>
  <tbody>
    {% assign current_date = site.time | date: "%Y-%m-%d" %}
    {% assign all_events = site.data.events | concat: site.data.wmt_events | where_exp: "event", "event.callsForPapersDeadline" %}
    {% assign sorted_events = all_events | sort: "startDate" | reverse %}
    {% for event in sorted_events %}
      <tr>
        <td>{% if current_date < event.callsForPapersDeadline %}<strong>{{ event.callsForPapersDeadline }}</strong>{% else %}{{ event.date }}{% endif %}</td>
        <td>{% if current_date < event.callsForPapersDeadline %}<strong><a href="/{{ event.id }}">{{ event.name }}</a></strong>{% else %}<a href="/{{ event.id }}">{{ event.name }}</a>{% endif %}</td>
        <td>{{ event.location }}</td>
      </tr>
    {% endfor %}
    <tr>
        <td><strong>1 April 2024</strong></td>
        <td><strong><em><a href='https://lans-tts.uantwerpen.be/index.php/LANS-TTS/announcement/view/24'>Machine and Computer-assisted Interpreting</a></em></strong></td>
        <td>LANS-TTS</td>
    </tr>
    <tr>
        <td>1 October 2023</td>
        <td><a href='https://aisca2024.org/dnlp/index'>DNLP 2024</a></td>
        <td>LANS-TTS</td>
    </tr>
    <tr>
        <td>10 September 2023</td>
        <td><strong><em><a href='https://airccse.org/journal/ijnlc/'>International Journal on Natural Language Computing</a></em></strong></td>
        <td></td>
    </tr>
    <tr>
        <td>5 September 2023</td>
        <td><a href='/wmt23'>WMT23</a></td>
        <td>Singapore</td>
    </tr>
    <tr>
        <td>15 August 2023</td>
        <td><a href='/amta2023'>AMTA 2023</a></td>
        <td>online</td>
    </tr>
    <tr>
        <td>15 July</td>
        <td><a href='/mtm2023'>MT Marathon</a></td>
        <td>Tartu, Estonia</td>
    </tr>
    <tr>
        <td>7 July 2023</td>
        <td><a href='/wat2023'>WAT 2023</a></td>
        <td>Macau SAR, China</td>
    </tr>
    <tr>
        <td>16 July 2023</td>
        <td><a href='/coco4mt-2'>CoCo4MT 2</a></td>
        <td>Macau SAR, China</td>
    </tr>
    <tr>
        <td>15 May 2023</td>
        <td><a href='/mtsummit2023'>MT Summit 2023 papers</a></td>
        <td>Macau SAR, China</td>
    </tr>
    <tr>
        <td>17 April 2023</td>
        <td><a href='/mtsummit2023'>MT Summit 2023 workshops and tutorials</a></td>
        <td>Macau SAR, China</td>
    </tr>
    <tr>
        <td>15 April 2023</td>
        <td><a href='/americasnlp2023'>AmericasNLP</a></td>
        <td>Toronto, Canada</td>
    </tr>
    <tr>
        <td>31 March 2023</td>
        <td><em><a href='https://sites.google.com/dcu.ie/nlecontextnmt/home'>The Role of Context in Neural Machine Translation Systems and its Evaluation</a></em></td>
        <td>JNLE</td>
    </tr>
    <tr>
        <td>31 March 2023</td>
        <td><a href='/at4ssl2023'>AT4SSL 2023</a></td>
        <td>Tampere, Finland</td>
    </tr>
    <tr>
        <td>10 March 2023</td>
        <td><a href='/eamt2023'>EAMT 2023 papers</a></td>
        <td>Tampere, Finland</td>
    </tr>
    <tr>
        <td>3 March 2023</td>
        <td><a href='/eamt2023'>EAMT 2023 tutorials</a></td>
        <td>Tampere, Finland</td>
    </tr>
    <tr>
        <td>2 March 2023</td>
        <td><a href='/loresmt2023'>LoResMT 2023</a></td>
        <td>Dubrovnik, Croatia</td>
    </tr>
    <tr>
        <td>20 February 2023</td>
        <td><a href='/eamt2023'>EAMT 2023 workshops</a></td>
        <td>Tampere, Finland</td>
    </tr>
    <tr>
        <td>23 December 2022</td>
        <td><em><a href='https://www.operas-eu.org/machine-translation-evaluation-in-the-context-of-scholarly-communication-open-call/'>Machine translation evaluation in the context of scholarly communication</a></em></td>
        <td>OPERAS</td>
    </tr>
    <tr>
        <td>15 November 2022</td>
        <td><em><a href='https://calico.org/calico-journal-special-issue-machine-translation-call-for-papers/'>Web-based machine translation in language teaching</a></em></td>
        <td>CALICO</td>
    </tr>
    <tr>
        <td>30 September 2022</td>
        <td><a href='https://www.aamt.info/event/aamttokyo2022/aamttokyo2022-kobo/'>AAMT 2022</a></td>
        <td>AAMT</td>
    </tr>
    <tr>
        <td>30 September 2022</td>
        <td><a href='http://turing.iimas.unam.mx/americasnlp/st.html'>AmericasNLP Competition</a></td>
        <td>NeurIPS</td>
    </tr>
    <tr>
        <td>7 September 2022</td>
        <td><a href='/wmt22'>WMT22</a></td>
        <td><a href='/wmt'>WMT</a></td>
    </tr>
    <tr>
        <td>28 July</td>
        <td><a href='/mtma2022'>MTMA22</a></td>
        <td></td>
    </tr>
    <tr>
        <td>15 July 2022</td>
        <td><a href='/mtm2022'>MTM22</a></td>
        <td></td>
    </tr>
    <tr>
        <td>11 July 2022</td>
        <td><a href='/wat2022'>WAT 2022</a></td>
    </tr>
    <tr>
        <td>1 July 2022</td>
        <td><a href='/mumttt2022'>MUMTTT 2022</a></td>
        <td></td>
    </tr>
    <tr>
        <td>30 June 2022</td>
        <td><em><a href='https://www.aclweb.org/portal/content/special-issue-translation-platforms'>Special Issue on Translation Platforms</a></em></td>
        <td>ACL</td>
    </tr>
    <tr>
        <td>29 June 2022</td>
        <td><a href='https://sites.google.com/view/coco4mt'>CoCo4MT</a></td>
        <td></td>
    </tr>
    <tr>
        <td>24 June 2022</td>
        <td><a href='https://2022.emnlp.org/calls/papers/Overview'>EMNLP 2022</a></td>
        <td>EMNLP</td>
    </tr>
    <tr>
        <td>13 June 2022</td>
        <td><a href='/amta2022'>AMTA 2022</a></td>
        <td><a href='/amta'>AMTA</a></td>
    </tr>
    <tr>
        <td>6 June 2022</td>
        <td><a href='/lit-translation-and-ai'>Literary Translation and AI: assessing changes in translation theory, practice and creativity</a></td>
        <td>TRACT</td>
    </tr>
    <tr>
        <td>1 June 2022</td>
        <td><a href='https://jostrans.org/2b.3%20Jostrans%20SI%2041.pdf'>Special issue on Translation Automation and Sustainability</a></td>
        <td>JosTrans</td>
    </tr>
    <tr>
        <td>1 May 2022</td>
        <td><a href='https://autosimtrans.github.io/cfp'>Automatic Simultaneous Translation 3</a></td>
        <td></td>
    </tr>
    <tr>
        <td>1 April 2022</td>
        <td><em><a href='https://lans-tts.uantwerpen.be/index.php/LANS-TTS/announcement/view/21'>The impact of Machine Translation in the Audiovisual Translation environment</a></em></td>
        <td>LANS – TTS</td>
    </tr>
    <tr>
        <td>1 April 2022</td>
        <td><a href='/eamt2022'>EAMT 2022</a></td>
        <td><a href='/eamt'>EAMT</a></td>
    </tr>
    <tr>
        <td>15 March 2022</td>
        <td><a href='/nettt2022'>NETTT 2022</a></td>
        <td></td>
    </tr>
    <tr>
        <td>13 March 2022</td>
        <td><a href='/iwslt2022'>IWSLT 2022</a></td>
        <td>IWSLT</td>
    </tr>
    <tr>
        <td>15 January</td>
        <td><a href='https://2022.naacl.org/calls/papers/#paper-submission-details'>NAACL 2022</a></td>
        <td>NAACL</td>
    </tr>
  </tbody>
</table>