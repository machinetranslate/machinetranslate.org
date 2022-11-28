# -*- coding: utf-8 -*-
import yaml
from os.path import exists

SCRIPTS = None
LANGUAGES = None
APIS = None
LANGUAGE_FAMILIES = None


### Read scripts
with open('_data/scripts.yml', 'r', encoding='utf8') as stream:
  SCRIPTS = yaml.safe_load(stream)

### Read languages
with open('_data/languages.yml', 'r', encoding='utf8') as stream:
  LANGUAGES = yaml.safe_load(stream)

### Read language families
with open('_data/language-families.yml', 'r', encoding='utf8') as stream:
  LANGUAGE_FAMILIES = yaml.safe_load(stream)

### Read apis
with open('_data/apis.yml', 'r', encoding='utf8') as stream:
  APIS = yaml.safe_load(stream)

### Read api-language conversions
with open('_data/api-language.yml', 'r', encoding='utf8') as stream:
  API_LANGUAGE = yaml.safe_load(stream)

def base_language_code(locale_code):
  locale_code = locale_code.replace('_', '-')
  return locale_code.split('-')[0]

def normalize_locale_casing(locale_code):
  return '-'.join([ part.capitalize() if len(part) == 4 else part.lower() for part in locale_code.split('-') ])

def _normalize_language_code(locale_code, api_id):
  if api_id not in API_LANGUAGE:
    return None
  if locale_code not in API_LANGUAGE[api_id]:
    return None
  return API_LANGUAGE[api_id][locale_code]

def normalize_language_code(locale_code, api_id):
  locale_code = locale_code.replace('_', '-')
  locale_code = normalize_locale_casing(locale_code)
  return _normalize_language_code(base_language_code(locale_code), api_id) \
    or _normalize_language_code(locale_code, '*') \
    or _normalize_language_code(base_language_code(locale_code), '*') \
    or locale_code

def get_language_variant_name(locale_code):
  parts = normalize_locale_casing(locale_code.replace('_', '-')).split('-')
  names = []
  if parts == 'lzh':
    names.append('Literary')
  for part in parts[1:]:
    if part in SCRIPTS:
      names.append(SCRIPTS[part])
    # TODO: if part in country
  print(locale_code, names)
  if not names:
    return None
  return ' - '.join(names)

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
for api in APIS:
  api_id = api['id']

  codes = flatten(api['languages'])



  def normalize(code):
    return normalize_language_code(code, api_id)

  codes = map(normalize, codes)

  codes = map(base_language_code, codes)


  SUPPORTED_LANGUAGE_BASE_CODES[api_id] = list(set(codes))


### Write language families
for code in LANGUAGE_FAMILIES:

  name = LANGUAGE_FAMILIES[code]

  slug = slugify(name)
  filepath = f'languages/{ slug }.md'

  # TODO: check that it won't be overwritten by a language

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
  languages.sort(key=lambda language: language['name'])

  frontmatter = {
    'nav_exclude': True,
    'parent': 'Language families',
    'layout': 'language_family',
    'title': name,
    'description': f'Machine translation for the { name } language family',
    'code': code,
    'languages': languages
  }

  with open(filepath, 'w', encoding='utf8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False) }
---
{ content }
''')


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
  supported_apis = []
  for api in APIS:
    codes = SUPPORTED_LANGUAGE_BASE_CODES[api['id']]
    if code in codes:
      supported_apis.append({
        'id': api['id'],
        'name': api['name'],
        'supported_language_count': len(codes)
      })

  supported_apis.sort(key=lambda api: api['supported_language_count'])

  frontmatter = {
    'nav_order': 1000 - len(supported_apis),
    'parent': 'Languages',
    'layout': 'language',
    'title': name,
    'description': f'Machine translation for { name }',
    'code': code,
    'family': family,
    'supported_apis': supported_apis
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


UNLISTED_LANGUAGES = {}

### Generate apis
for api in APIS:

  name = api['name']
  if type(name) is not str:
    raise Exception(name)

  api_id = api['id']
  if type(api_id) is not str:
    raise Exception(api_id)

  languages = api['languages']
  if type(languages) is not list:
    raise Exception(languages)

  urls = api['urls']

  self_serve = api.get('self-serve', True)

  customization = []
  if api.get('adaptive', False):
    customization.append('Adaptive')
  if api.get('glossary', False):
    customization.append('Glossary')
  if api.get('formality', False):
    customization.append('Formality')

  # "Join"
  # TODO: use language/api mapping
  supported_language_codes = list(set(flatten(languages)))
  supported_language_codes.sort()
  # TODO: language *pairs*

  supported_languages = []

  for code in supported_language_codes:
    language_name = None
    language_slug = None
    for language in LANGUAGES:
      normalized_code = normalize_language_code(code, api_id)
      base_code = base_language_code(normalized_code)
      if base_code in language['codes']:
        language_name = language['names'][0]
        language_slug = slugify(language_name)
        break
    variant_name = get_language_variant_name(code)
    supported_languages.append({
      'slug': language_slug,
      'code': code,
      'normalized_code': normalized_code,
      'base_code': base_code,
      'name': language_name,
      'variant_name': variant_name
    })
    if not language_slug:
      if code in UNLISTED_LANGUAGES:
        UNLISTED_LANGUAGES[code] += 1
      else:
        UNLISTED_LANGUAGES[code] = 1

  frontmatter = {
    'layout': 'api',
    'title': name,
    'description': f'The { name } machine translation API',
    'id': api_id,
    'parent': 'APIs',
    'urls': urls,
    'self_serve': self_serve,
    'customization': customization,
    'supported_languages': supported_languages,
    'nav_order': 1000 - len(supported_languages)
  }

  content = read_content(filepath)

  filepath = f'apis/{ api_id }.md'
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
