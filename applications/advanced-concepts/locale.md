---
parent: Building and research
title: Locale
description: Specification of language variants
---

A **locale** is an identifier of a language and region plus an optional writing script.
The locale is used in machine translation APIs to specify the language and variation of the language of both the source and target text.
Locales are also used to select the desired language in mobile phones, on webpages to hints for web browsers and web crawlers, and in language identification.

Example: `frCA` means french (fr) as spoken in Canada (CA)

Language codes are typically specified in two or three characters according to ISO 639.
Regions are typically specified in two characters according to ISO 3166.
Scripts are sometimes specified according to ISO 15924, such as sr-Cyrl_RS for Serbian written in Cyrllic script in Serbia.

## API Support

These language variations are supported by many API vendors:

- Chinese (zh): zh-cn, zh-tw
- Portuguese (pr): pr-pr, pr-br
- French (fr): fr-fr, fr-ca
- Spanish (es): es-es, es-mx, es-419 (Latin America)
- English (en): en-us, en-gb
- Serbian (sr): sr-Cyrl-rs, sr-Latn-rs

## Challenges

- When a region code is not specified for a language with significant regional variation, the user may not know which regional variation will be used
- Some commonly-written languages do not have language codes. For example, Hinglish is not acknowledged as a distinct language from Hindi and English and does not have a language code
- A country code may be too specific at times, and region codes may not exist for all regions of interest
- A region code may not be specific enough if there is significant variation within a country
