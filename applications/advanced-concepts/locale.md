---
parent: Building and research
title: Locale
description: Specification of language variants
---

A **locale** is an identifier of a language and region plus an optional writing script.
The locale is used in [machine translation APIs](/apis/apis.md) to specify the language and variation of the language of both the source and target text.
Locales are commonly used to set the default language on mobile phones and computers.
Locales are also an important concept when [web crawling](/customisation/crawling.md) to build [training data](/customisation/crawling.md).

Example: `frCA` means french (fr) as spoken in Canada (CA)

Language codes are typically specified in two or three characters according to ISO 639.
Regions are typically specified in two characters according to ISO 3166.
Scripts are sometimes specified according to ISO 15924, such as `sr-Cyrl_RS` for Serbian written in Cyrllic script in Serbia.

## API Support

These language variations are supported by many API vendors:

- Chinese (`zh`): Chinese, Simplified (`zh-cn`, also `zh-Hans`), Chinese, Traditional (`zh-tw`, also `zh-Hant`)
- Portuguese (`pr`): Portugal (`pr-pr`), Brazil (`pr-br`)
- French (`fr`): France (`fr-fr`), Canada (`fr-ca`)
- Spanish (`es`): Spain (`es-es`), Mexico (`es-mx`), Latin America (`es-419`)
- English (`en`): United States (`en-us`), Great Britain (`en-gb`)
- Serbian (`sr`): Serbia, Cyrillic script (`sr-Cyrl-rs`), Serbia, Latin script (`sr-Latn-rs`)
- Norwegian (`no`): Norwegian Bokmål (`nb`, `nob`), Norwegian Nynorsk (`nn`, `nno`)

## Challenges

- When a region and script are not specified, the underlying MT model may be built for the most common language variant or it may be built on a mix of variants
- Not all languages or variants have standardized locale codes
- In some cases the locale codes have changed over time. For example, old systems may represent Cantonese as `zhHK` while newer systems use the newer language code `yue`

