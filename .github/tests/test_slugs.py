import requests
from bs4 import BeautifulSoup


def test_unique_slugs():
    data = requests.get('https://machinetranslate.org/sitemap')
    soup = BeautifulSoup(data.text, 'xml')
    url_elements = soup.find_all('loc')

    slugs = []
    for url_element in url_elements:
        url_text = url_element.text.split('/')[-1]
        slug = url_text
        # Check duplicate/conflicting slugs
        assert slug not in slugs, f'Duplicate Slug {slug} for the URL {url_element.text}: {slug} or unneccessary trailing backlash'
        slugs.append(slug)
        check_path = url_element.text.split('/')[-2]
        # Check that URL is one level deep
        if check_path != 'files':
            assert check_path == 'machinetranslate.org', f'{url_element.text}: Paths should be 1 level deep e.g URL/slug'
