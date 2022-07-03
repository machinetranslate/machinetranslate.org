# -*- coding: utf-8 -*-
import yaml
from os.path import exists

### Generate languages
with open('_data/languages.yml', 'r') as stream:
    data = yaml.safe_load(stream)
    for language in data:
      code = language['codes'][0]
      name = language['names'][0]
      if type(language['codes']) is not list:
        raise Exception(language)
      if type(language['names']) is not list:
        raise Exception(language)

      filename = name.lower().replace(' ', '-')
      filepath = f'languages/{ filename }.md'
      if not exists(filepath):
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
