---
nav_order: 988
parent: Languages
layout: language
title: Burmese
description: Machine translation for Burmese
code: my
family:
- slug: sino-tibetan
  name: Sino-Tibetan
supported_apis:
- id: textra
  name: TexTra
  supported_language_count: 19
- id: xl8
  name: XL8
  supported_language_count: 29
- id: language-weaver
  name: Language Weaver
  supported_language_count: 54
- id: omniscien
  name: Omniscien Technologies
  supported_language_count: 58
- id: yandex
  name: Yandex Translate
  supported_language_count: 93
- id: microsoft
  name: Microsoft Translator
  supported_language_count: 103
- id: google
  name: Google Translate
  supported_language_count: 108
- id: lingvanex
  name: LingvaNex
  supported_language_count: 108
- id: youdao
  name: Youdao Translate
  supported_language_count: 110
- id: baidu
  name: Baidu Translate
  supported_language_count: 197
- id: alibaba
  name: Alibaba Translate
  supported_language_count: 212
- id: niutrans
  name: Niutrans
  supported_language_count: 383

---

## Character encoding

Burmese characters can be represented in Unicode or Zawgyi.
Zawgyi is a variation on Unicode which interprets some code points differently but otherwise encodes code points with standard encodings such as UTF-8.
If Zawgyi text is interpreted as Unicode, some characters will appear garbled.

Burmese text data from across the web is a mixture of Burmese Unicode and Burmese Zawgyi encoding.
This can lead to fragmentation of some of the vocabulary unless the data is first normalized.
