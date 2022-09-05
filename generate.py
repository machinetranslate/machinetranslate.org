# -*- coding: utf-8 -*-
import yaml
from os.path import exists

OVERWRITE_LANGUAGES = False
OVERWRITE_ENGINES = False

### Generate languages
with open('_data/languages.yml', 'r') as stream:
    data = yaml.safe_load(stream)
    for language in data:

      code = language['codes'][0]
      if type(language['codes']) is not list:
        raise Exception(language)

      name = language['names'][0]
      if type(language['names']) is not list:
        raise Exception(language)

      slug = name.lower().replace(' ', '-') # Should work *exactly* like in Liquid!

      filepath = f'languages/{ slug }.md'
      if OVERWRITE_LANGUAGES or not exists(filepath):
        markdown = f'''\
---
layout: language
title: { name }
description: Machine translation for { name }
code: { code }
parent: Languages
---
'''
        with open(filepath, 'w', encoding='utf8') as f:
          f.write(markdown)


### Generate engines

def flatten(l):
  _ = []
  for item in l:
    if type(item) is list:
      _ += flatten(item)
    else:
      _.append(item)
  return _

with open('_data/engines.yml', 'r') as stream:
    data = yaml.safe_load(stream)
    for engine in data:
      print(engine)
      name = engine['name']
      if type(name) is not str:
        raise Exception(name)
      slug = engine['id']
      if type(slug) is not str:
        raise Exception(slug)
      languages = engine['languages']
      if type(languages) is not list:
        raise Exception(languages)
      engine['languages'] = flatten(languages)
      # TODO: language pairs
      # TODO: order them in the nav (nav_order: ) by number of supported language pairs

      filepath = f'engines/{ slug }.md'
      if OVERWRITE_ENGINES or not exists(filepath):
        markdown = f'''\
---
layout: engine
id: { slug }
title: { name }
description: The { name } machine translation API
parent: Engines
---
'''
        with open(filepath, 'w', encoding='utf8') as f:
          f.write(markdown)
