---
parent: Building and research
nav_order: 163
title: Locale
description: Specification of language variants
---

A **locale** is an identifier of a [language](/languages/languages.md) and region, plus an optional writing script.
The locale is used in [machine translation APIs](/apis/apis.md) to specify the language of the source and target text.
Locales are used to indicate the language of documents in [web crawling](/customisation/crawling.md) to build [training data](/customisation/crawling.md).

Example: `frCA` means French (fr) as spoken in Canada (CA)

The formatting varies from one system to another.
`frCA`, `fr-ca`, and `fr_CA` are all common formats.

Language codes are typically specified in two or three characters according to ISO 639.
Regions are typically specified in two characters according to ISO 3166.
Scripts are optionally specified according to ISO 15924, such as `sr-Cyrl_RS` for Serbian written in Cyrillic script in Serbia.

## API support

These language variations are supported by many API vendors:

- Chinese (`zh`):
    - Chinese, Simplified (`zh-cn`, also `zh-Hans`)
    - Chinese, Traditional (`zh-tw`, also `zh-Hant`)
- Portuguese (`pr`):
    - Portugal (`pr-pr`)
    - Brazil (`pr-br`)
- French (`fr`):
    - France (`fr-fr`)
    - Canada (`fr-ca`)
- Spanish (`es`):
    - Spain (`es-es`)
    - Mexico (`es-mx`)
    - Latin America and Caribbean region (`es-419`)
- English (`en`):
    - United States (`en-us`)
    - Great Britain (`en-gb`)
- Serbian (`sr`):
    - Serbia, Cyrillic script (`sr-Cyrl-rs`)
    - Serbia, Latin script (`sr-Latn-rs`)
- Norwegian (`no`):
    - Norwegian Bokmål (`nb`, `nob`)
    - Norwegian Nynorsk (`nn`, `nno`)

## Challenges

- When a translation API uses only a language code without a region code or script, it can be unclear what locale is being translated.
- Not all languages or variants have standardised locale codes, leading to differences between different APIs.
- In some cases, the locale codes have changed over time. For example, old systems may represent Cantonese as `zhHK` while newer systems use the newer language code `yue`.

## See also

- [Languages](/languages/languages.md)
