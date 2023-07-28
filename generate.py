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

### Read APIs
with open('_data/apis.yml', 'r', encoding='utf8') as stream:
  APIS = yaml.safe_load(stream)

### Read API-language conversions
with open('_data/api-language.yml', 'r', encoding='utf8') as stream:
  API_LANGUAGE = yaml.safe_load(stream)

### Read translation management systems
with open('_data/translation-management-systems.yml', 'r', encoding='utf8') as stream:
  TRANSLATION_MANAGEMENT_SYSTEMS = yaml.safe_load(stream)

### Read aggregators
with open('_data/aggregators.yml', 'r', encoding='utf8') as stream:
  AGGREGATORS = yaml.safe_load(stream)

def base_language_code(locale_code):
  locale_code = locale_code.replace('_', '-')
  return locale_code.split('-')[0]

def normalize_locale_casing(locale_code):
  return '-'.join([ part.capitalize() if len(part) == 4 else part.lower() for part in locale_code.split('-') ])

def normalize_locale(locale_code):
  locale_code = locale_code.replace('_', '-')
  locale_code = normalize_locale_casing(locale_code)
  return locale_code

def _normalize_language_code(locale_code, api_id):
  if api_id not in API_LANGUAGE:
    return None
  if locale_code not in API_LANGUAGE[api_id]:
    return None
  return API_LANGUAGE[api_id][locale_code]

def normalize_language_code(locale_code, api_id, drop_variant=True):
  locale_code = normalize_locale(locale_code)
  return _normalize_language_code(base_language_code(locale_code), api_id) \
    or _normalize_language_code(locale_code, '*') \
    or (drop_variant and _normalize_language_code(base_language_code(locale_code), '*')) \
    or locale_code

# TODO: Move this to a .yaml file
TERRITORY_NAMES = {
  'ca': 'Canada',
  'fr': 'France',
  'es': 'Spain',
  'br': 'Brazil',
  'pt': 'Portugal',
  'us': 'United States',
  'uk': 'United Kingdom',
  'gb': 'Great Britain',
  '419': 'Latin America',
}

def get_language_variant_name(locale_code, api_id):
  locale_code = normalize_locale(locale_code)
  parts = (_normalize_language_code(locale_code, '*') or locale_code).split('-')
  names = []
  lang_code = parts[0]
  if lang_code == 'lzh':
    names.append('Literary') # Chinese
  if lang_code == 'fa' and 'af' in parts:
    names.append('Dari') # Persian
  for part in parts[1:]:
    if part in SCRIPTS:
      names.append(SCRIPTS[part])
    elif part in TERRITORY_NAMES:
      names.append(TERRITORY_NAMES[part])
  if not names:
    return None
  return ' - '.join(names)

def slugify(name):
  # Should work *exactly* like in Liquid!
  return name.lower().replace(' ', '-').replace('.', '')

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
  with open(filepath, 'r', encoding='utf8') as f:
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
  privacy_url = api.get('privacy_url', None)

  self_serve = api.get('self-serve', None)

  more_languages_by_request = api.get('more_languages_by_request', False)

  customisation = []
  if api.get('adaptive', False):
    customisation.append('Adaptive')
  if api.get('glossary', False):
    customisation.append('Glossary')
  if api.get('formality', False):
    customisation.append('Formality')
  if api.get('fine-tuning', False):
    customisation.append('Fine-tuning')

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
    if api_id not in [ 'alibaba', 'baidu', 'niutrans' ] and len(base_code) == 2 and not language_name:
      # This is usually a typo.
      raise Exception('2-letter language codes should be in languages.yml.  No name found for: ' + base_code + '(' + api_id + ')')
    variant_name = get_language_variant_name(code, api_id)
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

  integrations = []
  for tms in TRANSLATION_MANAGEMENT_SYSTEMS:
    for i in tms['api_integrations']:
      if i == api_id:
        integrations.append({
          'slug': tms['id'],
          'name': tms['name']
        })
      elif type(i) == dict:
        id = next(iter(i))
        if id == api_id:
          integrations.append({
            'slug': tms['id'],
            'name': tms['name'],
            **i[api_id]
          })

  frontmatter = {
    'layout': 'api',
    'title': name,
    'description': f'The { name } machine translation API',
    'id': api_id,
    'parent': 'APIs',
    'urls': urls,
    'privacy_url': privacy_url,
    'self_serve': self_serve,
    'customisation': customisation,
    'supported_languages': supported_languages,
    'more_languages_by_request': more_languages_by_request,
    'integrations': integrations,
    'nav_order': 1000 - len(supported_languages),
    'active': api.get('active', True),
  }

  name_slug = slugify(name)
  if name_slug != api_id:
    frontmatter['redirect_from'] = name_slug

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

# Generate TMS files

for tms in TRANSLATION_MANAGEMENT_SYSTEMS:
    tms_id = tms['id']
    tms_name = tms['name']
    tms_url = tms['tms_url']
    tms_type = tms['type']
    fuzzy_repair = tms.get('fuzzy_repair', False)
    tms_open_source = tms.get('open_source', False)
    tms_quality_estimation_api_integrations = tms.get('quality_estimation_api_integrations', None)
    APIS_BY_ID = {api['id']: api for api in APIS + AGGREGATORS}
    
    api_integrations = []
    for integration in tms['api_integrations']:
      try:
        integration_data = {}
        if type(integration) == type({}):
          integration_slug = list(integration.keys())[0]
          integration_data['slug'] = integration_slug
          for k, v in integration[integration_slug].items():
            integration_data[k] = v 
        else:
          integration_slug = integration
          integration_data['slug'] = integration_slug
        
        integration_data['name'] = APIS_BY_ID[integration_slug]['name']

        api_integrations.append(integration_data)
      except KeyError:
        pass

    if 'tms' in tms_type:
      tms_type_description = 'translation management system'
    elif 'cat':
      tms_type_description = 'computer-aided translation tool'
    else:
      raise 'TMS type must include `tms` or `cat`.'

    frontmatter = {
        'layout': 'translation-management-system',
        'title':  tms_name,
        'description': f'Machine translation API integrations in { tms_name }',
        'id': tms_id,
        'parent': 'Translation management systems',
        'type': tms_type,
        'type_description': tms_type_description,
        'tms_url': tms_url,
        'api_integrations': api_integrations,
        'fuzzy_repair': fuzzy_repair,
        'open-source': tms_open_source,
        'quality_estimation_api_integrations': tms_quality_estimation_api_integrations,
    }

    content = read_content(filepath)

    filepath = f'translation-management-systems/{tms_id}.md'
    with open(filepath, 'w', encoding='utf8') as f:
        f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False) }
---
{ content }
''')


### Generate Aggregators files

for a in AGGREGATORS:
    a_id = a['id']
    a_name = a['name']
    a_urls = a['urls']
    a_self_serve = a.get('self-serve', False)
    APIS_BY_ID = {api['id']: api for api in APIS}

    a_supported_apis = []
    for a in a['supported_apis']:
      try:
        a_data = {}
        if type(a) == type({}):
          a_slug = list(a.keys())[0]
          a_data['slug'] = a_slug
          for k, v in a[a_slug].items():
            a_data[k] = v 
        else:
          a_slug = a
          a_data['slug'] = a_slug
        
        a_data['name'] = APIS_BY_ID[a_slug]['name']

        a_supported_apis.append(a_data)
      except KeyError:
        pass

    frontmatter = {
        'layout': 'aggregator',
        'title': a_name,
        'description': f'The { a_name } aggregator',
        'id': a_id,
        'parent': 'Aggregators',
        'urls': a_urls,
        'supported_apis': a_supported_apis,
        'self-serve': a_self_serve,
    }
    
    content = read_content(filepath)

    filepath = f'aggregators/{a_id}.md'
    with open(filepath, 'w', encoding='utf8') as f:
        f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False) }
---
{ content }
''')

