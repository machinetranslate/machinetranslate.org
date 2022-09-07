# -*- coding: utf-8 -*-
import yaml
from os.path import exists

LANGUAGES = None
ENGINES = None
LANGUAGE_FAMILIES = None


### Read languages
with open('_data/languages.yml', 'r') as stream:
  LANGUAGES = yaml.safe_load(stream)

### Read language familiy
with open('_data/language_families.yml', 'r') as stream:
  LANGUAGE_FAMILIES = yaml.safe_load(stream)

### Read engines
with open('_data/engines.yml', 'r') as stream:
  ENGINES = yaml.safe_load(stream)

### Read engine-language conversions
with open('_data/engine_language.yml', 'r') as stream:
  ENGINE_LANGUAGE = yaml.safe_load(stream)

def base_language_code(locale_code):
  locale_code = locale_code.replace('_', '-')
  return locale_code.split('-')[0]

def normalize_locale_casing(locale_code):
  return '-'.join([ part.capitalize() if len(part) == 4 else part.lower() for part in locale_code.split('-') ])

def _normalize_language_code(locale_code, engine_id):
  if engine_id not in ENGINE_LANGUAGE:
    return None
  if locale_code not in ENGINE_LANGUAGE[engine_id]:
    return None
  return ENGINE_LANGUAGE[engine_id][locale_code]

def normalize_language_code(locale_code, engine_id):
  locale_code = locale_code.replace('_', '-')
  locale_code = normalize_locale_casing(locale_code)
  return _normalize_language_code(base_language_code(locale_code), engine_id) \
    or _normalize_language_code(locale_code, '*') \
    or _normalize_language_code(base_language_code(locale_code), '*') \
    or normalize_locale_casing(locale_code)

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

def read_content(filepth):
  content = ''
  if not exists(filepath):
    return ''
  with open(filepath, 'r') as f:
    page = f.read()
    i = page.find('\n---\n', 3)
    i += len('\n---\n')
    return page[i:].strip()

SUPPORTED_LANGUAGE_BASE_CODES = {}
for engine in ENGINES:
  engine_id = engine['id']

  codes = flatten(engine['languages'])

  def normalize(code):
    return normalize_language_code(code, engine_id)

  codes = map(normalize, codes)

  codes = map(base_language_code, codes)

  SUPPORTED_LANGUAGE_BASE_CODES[engine_id] = list(set(codes))

### Write languages
for language in LANGUAGES:
  code = language['codes'][0]
  if type(language['codes']) is not list:
    raise Exception(language)
  
  name = language['names'][0]
  if type(language['names']) is not list:
    raise Exception(language)

  family = []
  for language_family_code in language['family']:
    language_family_name = LANGUAGE_FAMILIES[language_family_code]
    family.append({
      'slug': slugify(language_family_name),
      'name': language_family_name
    })

  # "Join"
  supported_engines = []
  for engine in ENGINES:
    codes = SUPPORTED_LANGUAGE_BASE_CODES[engine['id']]
    if code in codes:
      supported_engines.append({
        'id': engine['id'],
        'name': engine['name'],
        'supported_language_count': len(codes)
      })

  supported_engines.sort(key=lambda engine: engine['supported_language_count'])

  frontmatter = {
    'layout': 'language',
    'title': name,
    'description': f'Machine translation for { name }',
    'code': code,
    'family': family,
    'parent': 'Languages',
    'supported_engines': supported_engines,
    'nav_order': 1000 - len(supported_engines)
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

### Write language families
for code in LANGUAGE_FAMILIES:

  name = LANGUAGE_FAMILIES[code]

  slug = slugify(name)
  filepath = f'language_families/{ slug }.md'

  content = read_content(filepath)

  # "Join"
  languages = []
  for language in LANGUAGES:
    if code in language['family']:
      language_name = language['names'][0]
      languages.append({
        'slug': slugify(language_name),
        'name': language_name
      })

  frontmatter = {
    'layout': 'language_family',
    'title': name,
    'description': f'Machine translation for the { name } language family',
    'code': code,
    'languages': languages,
  }

  with open(filepath, 'w', encoding='utf8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False) }
---

{ content }
''')

UNLISTED_LANGUAGES = {}

### Generate engines
for engine in ENGINES:

  name = engine['name']
  if type(name) is not str:
    raise Exception(name)

  engine_id = engine['id']
  if type(engine_id) is not str:
    raise Exception(engine_id)

  languages = engine['languages']
  if type(languages) is not list:
    raise Exception(languages)

  urls = engine['urls']

  self_serve = engine.get('self-serve', True)

  customization = []
  if engine.get('adaptive', False):
    customization.append('Adaptive')
  if engine.get('glossary', False):
    customization.append('Glossary')
  if engine.get('formality', False):
    customization.append('Formality')

  # "Join"
  # TODO: use language/engine mapping
  supported_language_codes = list(set(flatten(languages)))
  supported_language_codes.sort()
  # TODO: language *pairs*

  supported_languages = []

  for code in supported_language_codes:
    language_name = None
    language_slug = None
    for language in LANGUAGES:
      normalized_code = normalize_language_code(code, engine_id)
      base_code = base_language_code(normalized_code)
      if base_code in language['codes']:
        language_name = language['names'][0]
        language_slug = slugify(language_name)
        break
    supported_languages.append({
      'slug': language_slug,
      'code': code,
      'normalized_code': normalized_code,
      'base_code': base_code,
      'name': language_name
    })
    if not language_slug:
      if code in UNLISTED_LANGUAGES:
        UNLISTED_LANGUAGES[code] += 1
      else:
        UNLISTED_LANGUAGES[code] = 1
  
  frontmatter = {
    'layout': 'engine',
    'title': name,
    'description': f'The { name } machine translation API',
    'id': engine_id,
    'parent': 'Engines',
    'urls': urls,
    'self_serve': self_serve,
    'customization': customization,
    'supported_languages': supported_languages,
    'nav_order': 1000 - len(supported_languages)
  }

  content = read_content(filepath)

  filepath = f'engines/{ engine_id }.md'
  with open(filepath, 'w', encoding='utf8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False) }
---

{ content }
''')

print('Codes to add to languages.md')

for code, count in sorted(UNLISTED_LANGUAGES.items(), key=lambda x: x[1] * 10 - len(x[0]), reverse=True):
  text = code + ': ' + str(count)
  if count > 1 or len(code) == 2:
    text = '**' + text + '**'
  base_code = code.split('-')[0].lower()
  
  link = f'https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes#{ base_code }' if len(base_code) == 2 else f'https://en.wikipedia.org/wiki/ISO_639:{ base_code }'

  print(f'[{ text }]({ link })')
