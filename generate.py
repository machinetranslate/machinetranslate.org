# -*- coding: utf-8 -*-
import json
import yaml
from datetime import datetime
from os.path import exists

from jsonschema import validate
from unidecode import unidecode


SCRIPTS = None
LANGUAGES = None
APIS = None
LANGUAGE_FAMILIES = None
QUALITY_ESTIMATION = None
EVENTS = None
EVENTS_SCHEMA = None
WMT_EVENTS = None
WMT_EVENTS_SCHEMA = None
CALLS_FOR_PAPERS = None
CALLS_FOR_PAPERS_SCHEMA = None
MODELS = None
AUTOMATIC_POST_EDITING = None


### Read scripts
with open('_data/scripts.json', 'r', encoding='utf-8') as stream:
  SCRIPTS = json.load(stream)

### Read languages
with open('_data/languages.json', 'r', encoding='utf-8') as stream:
  LANGUAGES = json.load(stream)

### Read language families
with open('_data/language_families.json', 'r', encoding='utf-8') as stream:
  LANGUAGE_FAMILIES = json.load(stream)

### Read APIs
with open('_data/apis.json', 'r', encoding='utf-8') as stream:
  APIS = json.load(stream)

### Read API-language conversions
with open('_data/api_language.json', 'r', encoding='utf-8') as stream:
  API_LANGUAGE = json.load(stream)

### Read translation management systems
with open('_data/integrations.json', 'r', encoding='utf-8') as stream:
  INTEGRATIONS = json.load(stream)

### Read aggregators
with open('_data/aggregators.json', 'r', encoding='utf-8') as stream:
  AGGREGATORS = json.load(stream)

### Read quality estimation companies
with open ('_data/quality_estimation.json', 'r', encoding='utf-8') as stream:
  QUALITY_ESTIMATION = json.load(stream)

### Read events and events schema
with open ('_data/events.json', 'r', encoding='utf-8') as f:
  EVENTS = json.load(f)

with open('_data/_events_schema.json', 'r', encoding='utf-8') as f:
  EVENTS_SCHEMA = json.load(f)

### Read WMT events and WMT events schema
with open ('_data/wmt_events.json', 'r', encoding='utf-8') as f:
  WMT_EVENTS = json.load(f)

with open('_data/_wmt_events_schema.json', 'r', encoding='utf-8') as f:
  WMT_EVENTS_SCHEMA = json.load(f)

### Read external Calls For Papers and Calls For Papers schema
with open ('_data/calls_for_papers.json', 'r', encoding='utf-8') as f:
  CALLS_FOR_PAPERS = json.load(f)

with open('_data/_calls_for_papers_schema.json', 'r', encoding='utf-8') as f:
  CALLS_FOR_PAPERS_SCHEMA = json.load(f)

with open('_data/models.json', 'r', encoding='utf-8') as f:
  MODELS = json.load(f)

### Read automatic post-editing companies
with open ('_data/automatic_post_editing.json', 'r', encoding='utf-8') as stream:
  AUTOMATIC_POST_EDITING = json.load(stream)

def base_language_code(locale_code):
  locale_code = locale_code.replace('_', '-')
  return locale_code.split('-')[0]

def normalize_locale_casing(locale_code):
  return '-'.join([ part.capitalize() if len(part) == 4 and '-' in locale_code else part.lower() for part in locale_code.split('-') ])

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

# TODO: Move this to a .json file
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
  name = unidecode(name)
  return name.lower().replace(' ', '-').replace('.', '')

def flatten(l):
  _ = []
  for item in l:
    if isinstance(item, list):
      _ += flatten(item)
    else:
      _.append(item)
  return _

def read_content(filepath):
  content = ''
  if not exists(filepath):
    return ''
  with open(filepath, 'r', encoding='utf-8') as f:
    page = f.read()
    i = page.find('\n---\n', 3)
    i += len('\n---\n')
    return page[i:].strip()
  
def get_tms_by_id_and_key(id, key: str):
  integrations = []
  for tms in INTEGRATIONS:
    for i in tms.get(key, []):
      if i == id:
        integrations.append({
          'slug': tms['id'],
          'name': tms['name']
        })
      elif isinstance(i, dict):
        _id = next(iter(i))
        if _id == id:
          integrations.append({
            'slug': tms['id'],
            'name': tms['name'],
            **i[id]
          })
  return integrations

def supported_language_base_codes(file_name):
  SUPPORTED_LANGUAGE_BASE_CODES = {}
  for api in file_name:
    api_id = api['id']
    codes = flatten(api['languages'])

    def normalize(code):
      return normalize_language_code(code, api_id)
    
    codes = map(normalize, codes)
    codes = map(base_language_code, codes)

    SUPPORTED_LANGUAGE_BASE_CODES[api_id] = list(set(codes))
  return SUPPORTED_LANGUAGE_BASE_CODES


UNLISTED_LANGUAGES = {}

### Generate apis
for api in APIS:

  name = api['name']
  if not isinstance(name, str):
    raise Exception(name)

  api_id = api['id']
  if not isinstance(api_id, str):
    raise Exception(api_id)

  languages = api['languages']
  if not isinstance(languages, list):
    raise Exception(languages)
  
  models = []
  for model in api.get('models', [None]):
      if model:
        models.append({
          'name': model,
          'slug': slugify(model)
        })

  urls = api['urls']
  privacy_url = api.get('privacy_url', None)
  for url in urls + [privacy_url]:
    if not url:
      continue
    if '/es/' in url or '/de/' in url:
      raise Exception('Use /en/ if valid: ' + name + ' - ' + url)

  self_serve = api.get('self-serve', None)

  prompt_required = api.get('prompt_required', False)

  more_languages_by_request = api.get('more_languages_by_request', False)

  customisation = []
  if prompt_required:
    customisation.append('Prompting')
  if api.get('adaptive', False):
    customisation.append('Adaptive')
  if api.get('glossary', False):
    customisation.append('Glossary')
  if api.get('formality', False):
    customisation.append('Formality')
  if api.get('fine-tuning', False):
    customisation.append('Fine-tuning')

  inputs = api.get('inputs', None)

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
        language_name = language.get('names', [None])[0]
        language_slug = slugify(language_name) if language_name else base_code
        break
    if len(base_code) == 2 and not language_name:
      # This is usually a typo.
      raise Exception('2-letter language codes should be in languages.json.  No name found for: ' + base_code + '(' + api_id + ')')
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
      if base_code in UNLISTED_LANGUAGES:
        UNLISTED_LANGUAGES[base_code] += 1
      else:
        UNLISTED_LANGUAGES[base_code] = 1

  integrations = get_tms_by_id_and_key(api_id, 'api_integrations')

  if prompt_required:
    desc = f'The { name } API for machine translation'
  else:
    desc = f'The { name } machine translation API'

  frontmatter = {
    'autogenerated': True,
    'autogenerated_from': 'apis.json',
    'nav_order': 1000 - (len(supported_languages) + len(integrations)),
    'layout': 'api',
    'title': name,
    'description': desc,
    'id': api_id,
    'parent': 'APIs',
    'urls': urls,
    'privacy_url': privacy_url,
    'self_serve': self_serve,
    'prompt_required': prompt_required,
    'customisation': customisation,
    'inputs': inputs,
    'supported_languages': supported_languages,
    'more_languages_by_request': more_languages_by_request,
    'integrations': integrations,
    'models': models,
    'active': api.get('active', True),
    'seo': {
      'name': desc,
      'type': 'Product'
    }
  }

  name_slug = slugify(name)
  if name_slug != api_id:
    frontmatter['redirect_from'] = name_slug

  filepath = f'apis/{ api_id }.md'

  content = read_content(filepath)

  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False, allow_unicode=True) }
---
{ content }
''')


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
    if code in language.get('family', [None]):
      language_name = language.get('names', [None])[0]
      languages.append({
        'slug': slugify(language_name),
        'name': language_name
      })
  languages.sort(key=lambda language: language['name'])

  desc = f'Machine translation for the { name } language family'

  frontmatter = {
    'autogenerated': True,
    'nav_exclude': True,
    'nav_order': 1000 - len(languages),
    'parent': 'Language families',
    'layout': 'language_family',
    'title': name,
    'description': desc,
    'code': code,
    'languages': languages,
    'seo': {
      'name': desc,
      'type': 'Language'
    }
  }

  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False, allow_unicode=True) }
---
{ content }
''')


### Add unlisted languages to languages.json
for code, _ in UNLISTED_LANGUAGES.items():
  unlisted_languages = {
    'codes': [
      code
    ]
  }

  filepath = '_data/languages.json'

  with open(filepath, 'r', encoding='utf-8') as file:
    existing_data = json.load(file)
  if unlisted_languages not in existing_data:
    existing_data.append(unlisted_languages)

  with open(filepath, 'w', encoding='utf-8') as file:
    json.dump(existing_data, file, ensure_ascii=False, indent=4)


### Write languages
API_SUPPORTED_LANGUAGE_BASE_CODES = supported_language_base_codes(APIS)
QE_API_SUPPORTED_LANGUAGE_BASE_CODES = supported_language_base_codes(QUALITY_ESTIMATION)
for language in LANGUAGES:
  code = language['codes'][0]
  if not isinstance(language['codes'], list):
    raise Exception(language)

  name = language.get('names', [None])[0]
  if name:
    if not isinstance(language['names'], list):
      raise Exception(language)

  family = []
  for language_family_code in language.get('family', []):
    language_family_name = LANGUAGE_FAMILIES[language_family_code]
    family.append({
      'slug': slugify(language_family_name),
      'name': language_family_name
    })

  # "Join"
  supported_apis = []
  for api in APIS:
    codes = API_SUPPORTED_LANGUAGE_BASE_CODES[api['id']]
    if code in codes:
      supported_apis.append({
        'id': api['id'],
        'name': api['name'],
        'supported_language_count': len(codes)
      })

  supported_apis.sort(key=lambda api: api['supported_language_count'])
  for api in supported_apis:
    del api['supported_language_count']

  supported_qe_apis =[]
  for qe_api in QUALITY_ESTIMATION:
    codes = QE_API_SUPPORTED_LANGUAGE_BASE_CODES[qe_api['id']]
    if code in codes:
      supported_qe_apis.append({
        'slug': slugify(qe_api['name']),
        'id': qe_api['id'],
        'name': qe_api['name'],
        'supported_language_count': len(codes)
      })

  supported_qe_apis.sort(key=lambda api: api['supported_language_count'])
  for qe_api in supported_qe_apis:
    del qe_api['supported_language_count']

  desc = f'Machine translation for { name or f"<code>{code}</code>"}'

  frontmatter = {
    'autogenerated': True,
    'autogenerated_from': 'languages.json',
    'nav_order': 1000 - len(supported_apis),
    'nav_exclude': True,
    'parent': 'Languages',
    'layout': 'language',
    'title': name or f'<code>{code}</code>',
    'description': desc,
    **language,
    'family': family,
    'supported_apis': supported_apis,
    'supported_qe_apis': supported_qe_apis,
    'seo': {
      'name': desc,
      'type': 'Language'
    }
  }

  slug = slugify(name) if name else code

  filepath = f'languages/{ slug }.md'

  content = read_content(filepath)

  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False, allow_unicode=True) }
---
{ content }
''')

print('Codes to add to languages.md')

for code, count in sorted(UNLISTED_LANGUAGES.items(), key=lambda x: x[1] * 10 - len(x[0]), reverse=True):
  text = f"{code}: {str(count)}"
  if count > 1 or len(code) == 2:
    text = '**' + text + '**'
  base_code = code.split('-')[0].lower()

  link = f'https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes#{ base_code }' if len(base_code) == 2 else f'https://en.wikipedia.org/wiki/ISO_639:{ base_code }'

  print(f'[{ text }]({ link })')


# Generate TMS files
QE_APIS_BY_ID = {api['id']: api for api in QUALITY_ESTIMATION}
APIS_BY_ID = {api['id']: api for api in APIS + AGGREGATORS}
APE_APIS_BY_ID = {api['id']: api for api in AUTOMATIC_POST_EDITING}
for tms in INTEGRATIONS:
    tms_id = tms['id']
    print(tms_id)
    tms_name = tms['name']
    tms_url = tms['tms_url']
    tms_type = tms['type']
    fuzzy_repair = tms.get('fuzzy_repair', False)
    tms_open_source = tms.get('open_source', False)
    tms_qe_api_integrations = tms.get('quality_estimation_integrations', [])

    qe_api_integrations = []
    for qe_integration in tms_qe_api_integrations:
      try:
        qe_integration_data = {}
        if isinstance(qe_integration, dict):
          qe_integration_slug = list(qe_integration.keys())[0]
          qe_integration_data['slug'] = qe_integration_slug
          for k, v in qe_integration[qe_integration_slug].items():
            qe_integration_data[k] = v 
        else:
          qe_integration_slug = qe_integration
          qe_integration_data['slug'] = qe_integration_slug
        
        qe_integration_data['name'] = QE_APIS_BY_ID[qe_integration_slug]['name']

        qe_api_integrations.append(qe_integration_data)
      except KeyError:
        pass

    api_integrations = []
    for integration in tms['api_integrations']:
      try:
        integration_data = {}
        if isinstance(integration, dict):
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

    ape_integrations = []
    for integration in tms.get('automatic_post_editing_integrations', []):
      try:
        integration_data = {}
        if isinstance(integration, dict):
          integration_slug = list(integration.keys())[0]
          integration_data['slug'] = integration_slug
          for k, v in integration[integration_slug].items():
            integration_data[k] = v 
        else:
          integration_slug = integration
          integration_data['slug'] = integration_slug
        
        integration_data['name'] = APE_APIS_BY_ID[integration_slug]['name']

        ape_integrations.append(integration_data)
      except KeyError:
        pass

    if 'tms' in tms_type:
      tms_type_description = 'translation management system'
    elif 'cat':
      tms_type_description = 'computer-aided translation tool'
    else:
      raise 'TMS type must include `tms` or `cat`.'

    desc = f'Machine translation API integrations in { tms_name }'

    frontmatter = {
      'autogenerated': True,
      'autogenerated_from': 'integrations.json',
      'layout': 'integration',
      'nav_order': 1000 - (len(api_integrations) + len(tms_qe_api_integrations)),
      'title':  tms_name,
      'description': desc,
      'id': tms_id,
      'parent': 'Integrations',
      'type': tms_type,
      'type_description': tms_type_description,
      'tms_url': tms_url,
      'api_integrations': api_integrations,
      'fuzzy_repair': fuzzy_repair,
      'open-source': tms_open_source,
      'quality_estimation_integrations': qe_api_integrations,
      'automatic_post_editing_integrations': ape_integrations,
      'seo': {
        'name': desc,
        'type': 'Product'
      }
    }

    filepath = f'integrations/{tms_id}.md'

    content = read_content(filepath)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False, allow_unicode=True) }
---
{ content }
''')


### Generate Aggregators files
for a in AGGREGATORS:
    a_id = a['id']
    a_name = a['name']
    a_urls = a['urls']
    a_self_serve = a.get('self-serve', False)

    a_supported_apis = []
    for a in a['supported_apis']:
      try:
        a_data = {}
        if isinstance(a, dict):
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
    
    integrations = get_tms_by_id_and_key(a_id, 'api_integrations')

    desc = f'The { a_name } machine translation API aggregator'

    frontmatter = {
      'autogenerated': True,
      'autogenerated_from': 'aggregators.json',
      'layout': 'aggregator',
      'nav_order': 1000 - len(a_supported_apis),
      'title': a_name,
      'description': desc,
      'id': a_id,
      'parent': 'Aggregators',
      'urls': a_urls,
      'supported_apis': a_supported_apis,
      'integrations': integrations,
      'self-serve': a_self_serve,
      'seo': {
        'name': desc,
        'type': 'Product'
      }
    }
    
    filepath = f'aggregators/{a_id}.md'

    content = read_content(filepath)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False, allow_unicode=True) }
---
{ content }
''')


### Generate Quality Estimation files
for estimation in QUALITY_ESTIMATION:

  name = estimation['name']
  if not isinstance(name, str):
    raise Exception(name)

  company_id = estimation['id']
  if not isinstance(company_id, str):
    raise Exception(company_id)
  
  company = estimation['company'].replace('-',' ')
  if not isinstance(company, str):
    raise Exception(company)

  languages = estimation['languages']
  if not isinstance(languages, list):
    raise Exception(languages)

  urls = estimation['urls']
  if not isinstance(urls, list):
    raise Exception(urls)

  tagline = estimation.get('tagline', False)

  only_compatible_mt_api = []
  only_compatible_mt_api_id = estimation.get('only_compatible_mt_api', False)
  if only_compatible_mt_api_id:
    api_name = next((api['name'] for api in APIS if only_compatible_mt_api_id and \
                    api['id'].lower() == only_compatible_mt_api_id.lower()), only_compatible_mt_api_id)
    only_compatible_mt_api.append({
      'id': only_compatible_mt_api_id,
      'name': api_name
    })
  else:
    only_compatible_mt_api = only_compatible_mt_api_id

  only_compatible_tms = []
  only_compatible_tms_id = estimation.get('only_compatible_tms', False)
  if only_compatible_tms_id:
    tms_name = next((tms['name'] for tms in INTEGRATIONS if only_compatible_tms_id and \
                    tms['id'].lower() == only_compatible_tms_id.lower()), only_compatible_tms_id)
    only_compatible_tms.append({
      'id': only_compatible_tms_id,
      'name': tms_name
    })
  else:
    only_compatible_tms = only_compatible_tms_id

  customisation = estimation.get('customisation', False)

  supported_language_codes = list(set(flatten(languages)))
  supported_language_codes.sort()
  
  supported_languages = []
  for code in supported_language_codes:
    language_name = None
    language_slug = None
    for lang in LANGUAGES:
      normalized_code = normalize_language_code(code, company_id)
      base_code = base_language_code(normalized_code)
      if base_code in lang['codes']:
        language_name = lang.get('names', [None])[0]
        language_slug = slugify(language_name) if language_name else code
        break
    variant_name = get_language_variant_name(code, company_id)
    supported_languages.append({
      'slug': language_slug,
      'code': code,
      'base_code': base_code,
      'name': language_name,
      'variant_name': variant_name
    })

  integrations = get_tms_by_id_and_key(company_id, 'quality_estimation_integrations')

  desc = f'The {name} translation quality estimation API'

  frontmatter = {
    'autogenerated': True,
    'autogenerated_from': 'quality_estimation.json',
    'nav_order': 1000 - len(supported_languages),
    'layout': 'quality_estimation',
    'title': name,
    'description': desc,
    'tagline': tagline,
    'id': company_id,
    'company': company,
    'parent': 'Quality estimation',
    'urls': urls,
    'supported_languages': supported_languages,
    'only_compatible_mt_api': only_compatible_mt_api,
    'only_compatible_tms': only_compatible_tms,
    'customisation': customisation,
    'integrations': integrations,
    'seo': {
      'name': desc,
      'type': 'Product'
    }
  }

  slug = slugify(name)

  filepath = f'quality-estimation/{ slug }.md'

  content = read_content(filepath)

  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False, allow_unicode=True) }
---
{ content }
''')
    

### Generate Automatic post-editing files
for ape in AUTOMATIC_POST_EDITING:
    ape_id = ape['id']
    ape_name = ape['name']
    ape_urls = ape['urls']
    ape_languages = ape['languages']

    supported_language_codes = list(set(flatten(ape_languages)))
    supported_language_codes.sort()
    
    ape_supported_languages = []
    for code in supported_language_codes:
      language_name = None
      language_slug = None
      for lang in LANGUAGES:
        normalized_code = normalize_language_code(code, ape_id)
        base_code = base_language_code(normalized_code)
        if base_code in lang['codes']:
          language_name = lang.get('names', [None])[0]
          language_slug = slugify(language_name) if language_name else code
          break
      variant_name = get_language_variant_name(code, ape_id)
      ape_supported_languages.append({
        'slug': language_slug,
        'code': code,
        'normalized_code': normalized_code,
        'base_code': base_code,
        'name': language_name,
        'variant_name': variant_name
      })

    integrations = get_tms_by_id_and_key(ape_id, 'automatic_post_editing_integrations')

    desc = f'The { ape_name } automatic post-editing API'

    frontmatter = {
      'autogenerated': True,
      'autogenerated_from': 'automatic_post_editing.json',
      'layout': 'automatic_post_editing',
      'nav_order': 1000 - len(ape_supported_languages),
      'title': ape_name,
      'description': desc,
      'id': ape_id,
      'parent': 'Automatic post-editing',
      'urls': ape_urls,
      'supported_languages': ape_supported_languages,
      'integrations': integrations,
      'seo': {
        'name': desc,
        'type': 'Product'
      }
    }
    
    filepath = f'automatic-post-editing/{ape_id}.md'

    content = read_content(filepath)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False, allow_unicode=True) }
---
{ content }
''')

  
### Generate Events
for event in EVENTS:

  # Validate events.json entries
  validate(instance=event, schema=EVENTS_SCHEMA)

  name = event['name']

  # startDate is necessary for listing the event on events.md
  start_date = datetime.strptime(event['start_date'], '%Y-%m-%d').date()

  if event.get('end_date', None):
    end_date = datetime.strptime(event['end_date'], '%Y-%m-%d').date()
  else:
    end_date = start_date

  # Generate SEO and location
  description = event.get('description', None)
  _location = event.get('location', {})
  location_name = _location.get('location', 'Online')
  is_online = _location.get('online', False)
  if is_online:
      location_type = 'VirtualLocation'
      event_attendance_mode = 'OnlineEventAttendanceMode'
  elif 'online' in location_name.lower():
      location_type = 'Hybrid'
      event_attendance_mode = 'MixedEventAttendanceMode'
  else:
      location_type = 'Place'
      event_attendance_mode = 'OfflineEventAttendanceMode'

  if event.get('organizer', None):
    organizer_name = event['organizer'].get('name', None)
    organizer_url = event['organizer'].get('url', None)
    organizer_type = event['organizer'].get('type', None)

  date = f'from {datetime.strftime(start_date, "%d %B") } to {datetime.strftime(end_date, "%d %B, %Y")}' if start_date != end_date else f'on {datetime.strftime(start_date, "%d %B, %Y")}'
  location = f'in {location_name}' if location_name.lower() != 'online' else location_name
  future_tense_opening_paragraph = f'The {description} (<strong>{name}</strong>) will take place {location} {date}.'
  past_tense_opening_paragraph = f'The {description} (<strong>{name}</strong>) took place {location} {date}.'

  

  frontmatter = {
    'autogenerated': True,
    'autogenerated_from': 'events.json',
    'parent': 'Events',
    'nav_order': int(event['start_date'].split('-')[0]),
    'layout': 'event',
    'title': name,
    'end_date': str(end_date),
    'future_tense_opening_paragraph': future_tense_opening_paragraph,
    'past_tense_opening_paragraph': past_tense_opening_paragraph,
    **event,
    'location': location_name,
    'seo': {
      'type': 'Event',
      'name': name,
      'description': description,
      'startDate': str(start_date),
      'endDate': str(end_date),
      'eventAttendanceMode': event_attendance_mode,
      'eventStatus': 'EventScheduled',
      'location': {
        'type': location_type,
        'name': location_name
      },
      'organizer': {
        'type': organizer_type,
        'name': organizer_name,
        'url': organizer_url
      }
    },
  }

  # Doesn't create a file if it's an external event, since external events should not have an id
  if not event.get('id', None):
    continue

  slug = slugify(name)
  filepath = f'events/{ slug }.md'

  content = read_content(filepath)

  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False, allow_unicode=True) }
---
{content}
''')


### Generate WMT events
for event in WMT_EVENTS:

  # Validate wmt_events.json entries
  validate(instance=event, schema=WMT_EVENTS_SCHEMA)

  name = event['name']

  # startDate is necessary for listing the event on events.md
  start_date = datetime.strptime(event['start_date'], '%Y-%m-%d').date()

  if event.get('end_date', None):
    end_date = datetime.strptime(event['end_date'], '%Y-%m-%d').date()
  else:
    end_date = start_date

  # Generate SEO and location
  description = event.get('description', None)
  location = event.get('location', {})
  location_name = location.get('location', 'Online')
  is_online = location.get('online', False)
  if is_online:
      location_type = 'VirtualLocation'
      event_attendance_mode = 'OnlineEventAttendanceMode'
  elif 'online' in location_name.lower():
      location_type = 'Hybrid'
      event_attendance_mode = 'MixedEventAttendanceMode'
  else:
      location_type = 'Place'
      event_attendance_mode = 'OfflineEventAttendanceMode'

  if event.get('organizer', None):
    organizer_name = event['organizer'].get('name', None)
    organizer_url = event['organizer'].get('url', None)
    organizer_type = event['organizer'].get('type', None)

  # Generate opening pagaraph in future/past tense
  date = f'from {datetime.strftime(start_date, "%d %B") } to {datetime.strftime(end_date, "%d %B, %Y")}'
  location = f'in {location_name}' if location_name.lower() != 'online' else location_name
  future_tense_opening_paragraph = f'The {description} (<strong>{name}</strong>) will take place {location} {date}.'
  past_tense_opening_paragraph = f'The {description} (<strong>{name}</strong>) took place {location} {date}.'

  frontmatter = {
    'autogenerated': True,
    'autogenerated_from': 'wmt_events.json',
    'parent': 'Events',
    'nav_order': event['start_date'].split('-')[0],
    'layout': 'wmt_event',
    'title': name,
    'end_date': str(end_date),
    'future_tense_opening_paragraph': future_tense_opening_paragraph,
    'past_tense_opening_paragraph': past_tense_opening_paragraph,
    **event,
    'location': location_name,
    'seo': {
      'type': 'Event',
      'name': name,
      'description': description,
      'startDate': str(start_date),
      'endDate': str(end_date),
      'eventAttendanceMode': event_attendance_mode,
      'eventStatus': 'EventScheduled',
      'location': {
        'type': location_type,
        'name': location_name
      },
      'organizer': {
        'type': organizer_type,
        'name': organizer_name,
        'url': organizer_url
      }
    }
  }

  # Doesn't create a file if it's an external event, as external events should not have an id
  if not event.get('id', None):
    continue

  slug = slugify(name)
  filepath = f'events/{ slug }.md'

  content = read_content(filepath)

  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False, allow_unicode=True) }
---
{content}
''')


### Validate Calls For Papers
for entry in CALLS_FOR_PAPERS:

  # Validate date format
  datetime.strptime(entry['calls_for_papers_deadline'], '%Y-%m-%d').date()

  # Validate calls_for_papers.json entries
  validate(instance=entry, schema=CALLS_FOR_PAPERS_SCHEMA)


#Generate models
for model in MODELS:

  name = model['name']
  if not isinstance(name, str):
    raise Exception(name)

  model_id = model['id']
  if not isinstance(model_id, str):
    raise Exception(model_id)

  apis = []
  for api in model['apis']:
    apis.append({
      "name": api,
      "slug": slugify(api)
    })

  urls = model['urls']
  for url in urls:
    if not url:
      continue
    if '/es/' in url or '/de/' in url:
      raise Exception('Use /en/ if valid: ' + name + ' - ' + url)

  self_serve = model.get('self_serve', None)

  desc = f'The { name } model for translation'

  frontmatter = {
    'autogenerated': True,
    'autogenerated_from': 'models.json',
    'nav_order': 1000 - len(supported_apis),
    'layout': 'model',
    'title': name,
    'description': desc,
    'id': model_id,
    'parent': 'Models',
    'urls': urls,
    'self_serve': self_serve,
    'apis': apis,
    'seo': {
      'name': desc,
      'type': 'Product'
    }
  }

  name_slug = slugify(name)
  if name_slug != model_id:
    frontmatter['redirect_from'] = name_slug

  filepath = f'models/{ model_id }.md'

  content = read_content(filepath)

  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(f'''\
---
{ yaml.dump(frontmatter, sort_keys=False, allow_unicode=True) }
---
{ content }
''')
