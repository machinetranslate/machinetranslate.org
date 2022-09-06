# -*- coding: utf-8 -*-
import yaml
from os.path import exists

LANGUAGES = None
ENGINES = None

### Read languages
with open('_data/languages.yml', 'r') as stream:
  LANGUAGES = yaml.safe_load(stream)

### Read engines
with open('_data/engines.yml', 'r') as stream:
  ENGINES = yaml.safe_load(stream)

def slugify(name):
  # Should work *exactly* like in Liquid!
  return name.lower().replace(' ', '-')

def flatten(l):
  _ = []
  for item in l:
    if type(item) is list:
      _ += flatten(item)
    else:
      _.append(item)
  return _

def base_language_code(locale_code):
  return locale_code.split('-')[0]

def read_content(filepth):
  content = ''
  if not exists(filepath):
    return ''
  with open(filepath, 'r') as f:
    page = f.read()
    i = page.find('\n---\n', 3)
    i += len('\n---\n')
    return page[i:].strip()

### Write languages
for language in LANGUAGES:
  code = language['codes'][0]
  if type(language['codes']) is not list:
    raise Exception(language)
  
  name = language['names'][0]
  if type(language['names']) is not list:
    raise Exception(language)

  # "Join"
  supported_engines = []
  for engine in ENGINES:
    if code in map(base_language_code, flatten(engine['languages'])):
      supported_engines.append({
        'id': engine['id'],
        'name': engine['name']
      })

  frontmatter = {
    'layout': 'language',
    'title': name,
    'description': f'Machine translation for { name }',
    'code': code,
    'parent': 'Languages',
    'supported_engines': supported_engines
  }

  slug = slugify(name)
  filepath = f'languages/{ slug }.md'

  content = read_content(filepath)

  with open(filepath, 'w', encoding='utf8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False) }
---

{ content }
''')


### Generate engines

for engine in ENGINES:
  name = engine['name']
  if type(name) is not str:
    raise Exception(name)
  slug = engine['id']
  if type(slug) is not str:
    raise Exception(slug)
  languages = engine['languages']
  if type(languages) is not list:
    raise Exception(languages)

  # "Join"
  supported_language_codes = list(map(base_language_code, flatten(languages)))
  # TODO: language *pairs*

  supported_languages = []
  for language in LANGUAGES:
    for code in language['codes']:
      if code in supported_language_codes:
        language_name = language['names'][0]
        supported_languages.append({
          'slug': slugify(language_name),
          'code': code,
          'name': language_name
        })

  # TODO: *order* engines in the nav (nav_order: ) by number of supported language pairs

  frontmatter = {
    'layout': 'engine',
    'title': name,
    'description': f'The { name } machine translation API',
    'id': slug,
    'parent': 'Engines',
    'supported_languages': supported_languages,
    'nav_order': len(LANGUAGES) - len(supported_languages)
  }

  filepath = f'engines/{ slug }.md'
  with open(filepath, 'w', encoding='utf8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False) }
---

{ content }
''')
