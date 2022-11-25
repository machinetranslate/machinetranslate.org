---
parent: Events
title: Machine translation meetup 2
description: Meetup organised by Machine Translate
location: online
startDate: 2022-10-21
name: Machine translation meetup 2
seo:
  type: Event
  name: Machine translation meetup 2
  description: Meetup organised by Machine Translate
  startDate: 2022-10-21
  endDate: 2022-10-21
  eventAttendanceMode: OnlineEventAttendanceMode
  eventStatus: EventScheduled

  location:
  type: VirtualLocation
  url: https://www.meetup.com/machinetranslate/events/289057267/

  organizer:
    type: Organization
    name: Machine Translate
    url: https://machinetranslate.org/about/
---

The second **machine translation meetup** took place online on 21 October, 2022.

A panel of guests discussed ***machine translation for low-resource languages***.

## Panel

- Francisco Guzman, Meta AI
- John E. Ortega, AmericasNLP
- Atul Kr. Ojha, LoResMT
- Ayushman Dash, NeuralSpace
- Idris Abdulmumin, Masakhane

The machine translation meetup was organised by Machine Translate.

[machinetranslate.org/meetup](http://machinetranslate.org/meetup)


## Answers to audience questions

There was not enough time to answer all of the audience questions during the meetup.  The guests kindly answered those questions in writing.

> ### What causes a low-resource language to get on the radar of researchers, or to get launched in major products?
>
> Francisco Guzman:
>
> > I think a number of factors might be at play:
> >  - Number of speakers of the languages
> >  - Availability of basic resources (online monolingual text, dictionaries, etc)
> >  - Availability of professional translators to help create more data/evaluate
> >  - Influence from advocacy groups

> ### Are your approaches also applicable to historical / dead languages, which are mostly “very low-resource”?
>
> Francisco Guzman:
>
> > Although it’s interesting to see historical languages as low-resource,
> > I’m focusing my research on languages that would be most impactful to bridge language barriers of living people.
> >
> > As such, historical languages are not very impactful.

> ### Concretely, how much training data is the minimum for obtaining useful results?
>
> Francisco Guzman:
>
> > Quality of translation depends on a myriad of factors, not only the amount of training data.
> >
> > For example, whether there is a related language that you can co-train or not.
> >
> > However, in No Languages Left Behind we found that a clean seed data of approximately 6 thousand sentence pairs was useful to bootstrap mining, backtranslation and training.
>
> Idris Abdulmumin:
>
> > In machine translation, and natural language processing in general, quality is most associated with performance on some metrics, and seldom, on some form of human evaluation.
> >
> > But this is most times constraint on the test set in consideration.
> > The actual ‘quality’ of translation systems that don’t get the required attention in research is the ability of these systems to meet some decent performance after deployment, where actual users supply all kinds of unstructured, informal data for translation.
> >
> > To achieve this, we need way more than the 6 thousand sentences that was suggested in No Languages Left Behind.

> ### How effective is crowdsourcing machine translation data?
>
> Francisco Guzman:
>
> > Generating translations of data is expensive and time consuming.
> >
> > For benchmark data (like [FLORES](/customisation/parallel-data.md)) crowdsourcing translation is not appropriate, as it lacks the quality process needed.
> >
> > It’s possible that it is more appropriate for bilingual training data, which is OK if it’s noisy.
> >
> > I think there is a lot of potential for monolingual data generation, which is not readily available in many low-resource languages.

> ### Marcin from Microsoft says that a lot of low-resource machine translation is just taking high-res language datasets and making them smaller, but this doesn’t really reflect a real low-resource scenario.  How are low-resource language datasets in reality?
>
> Francisco Guzman:
>
> > I agree with this observation.
> >
> > As a reviewer, I push back when people label “ablated” datasets, that is, smaller versions of a larger dataset, as low-resource.
> >
> > Real low-resource languages are noisier, include code-switching, have different scripts, non standardized orthography (that is, same word can be spelled differently in the same dataset).
>
> Idris Abdulmumin:
>
> > This is sadly true.
> >
> > A lot of researchers work on these big datasets and then simulate low resource conditions on the high resource datasets just to generalize their findings.
> >
> > Simulated low resource dataset usually consist of random text and, as a result, lacks the authenticity of document level texts.
> >
> > Actual low resource data is more structured and also more restrictive in its coverage of the actual language in consideration while simulation just produces a lot of different texts.

> ### Do you have any advice on useful approaches, tools and methods for creating parallel corpora from scratch?
>
> Francisco Guzman:
>
> > Always check that you’re not paying human translation price for machine translation price.
> >
> > That is, if you’re asking an language service provider to provide translations, verify that translators are not post-editing Google Translate, Microsoft Translator, Amazon Translate, or that the post-editing rates are clearly stated.
> >
> > This is super important if you want to build a benchmark.
> >
> > You don’t want to limit the research community to what the current translation engines are capable of.
>
> Idris Abdulmumin:
>
> > I have seen situations where non-natives are paid to translate for a language just because they are from a country where that language is spoken, or where translators have not lived within the community for a long time.
> >
> > It is worthwhile ensuring that translators should not only be speakers of the language but should live where the language is spoken.
> >
> > Language changes with time.

> ### Do we need different quality evaluations for assimilation and for dissemination?
>
> Francisco Guzman:
>
> > Probably.
> >
> > Most of the evaluation metrics right (say in the metrics task at [WMT](/associations/wmt.md)) are focused on cases where minute differences of high-quality translations are important (dissemination), while others like [BLEU](/metrics/bleu.md)/XSTS are more than adequate for assimilation use cases.

> ### What is the minimum investment in terms of training set size to make machine translation for a low-resource language usable?
>
> Idris Abdulmumin:
>
> > With the availability of pre-trained language models and other supporting resources, it will be advisable to have at least 50 thousand to 100 thousand of qualitative and diverse human translations.

> ### What have been the major factors for low-resource languages progress? Datasets? Multilingual models?
>
> Francisco Guzman:
>
> > The availability of training data, multilingual models and evaluation benchmarks.
