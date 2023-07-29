---
nav_order: 985
parent: Languages
layout: language
title: Burmese
description: Machine translation for Burmese
code: my
codes:
- my
- mya
- bur
names:
- Burmese
- Myanmar
- Myanmarese
- Birmese
family:
- slug: sino-tibetan
  name: Sino-Tibetan
scripts:
- Mymr
typology:
  word_order:
  - SOV
  morphosyntax:
  - analytic
  - isolating
territories:
- mm
supported_apis:
- id: t-tact-an-zin
  name: T-tact-AN-ZIN
  supported_language_count: 14
- id: textra
  name: TexTra
  supported_language_count: 30
- id: xl8
  name: XL8
  supported_language_count: 41
- id: language-weaver
  name: Language Weaver
  supported_language_count: 58
- id: omniscien
  name: Omniscien Technologies
  supported_language_count: 58
- id: lilt
  name: Lilt
  supported_language_count: 72
- id: yandex
  name: Yandex Translate
  supported_language_count: 93
- id: microsoft
  name: Microsoft Translator
  supported_language_count: 103
- id: lingvanex
  name: LingvaNex
  supported_language_count: 108
- id: youdao
  name: Youdao Translate
  supported_language_count: 110
- id: google
  name: Google Translate
  supported_language_count: 132
- id: modernmt
  name: ModernMT
  supported_language_count: 195
- id: baidu
  name: Baidu Translate
  supported_language_count: 197
- id: alibaba
  name: Alibaba Translate
  supported_language_count: 212
- id: niutrans
  name: Niutrans
  supported_language_count: 381

---
## Character encoding

Burmese characters can be represented in Unicode or Zawgyi.
Zawgyi is a variation on Unicode which interprets some code points differently but otherwise encodes code points with standard encodings such as UTF-8.
If Zawgyi text is interpreted as Unicode, some characters will appear garbled.

Burmese text data from across the web is a mixture of Burmese Unicode and Burmese Zawgyi encoding.
This can lead to fragmentation of some of the vocabulary unless the data is first normalized.
