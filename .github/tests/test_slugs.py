import os
from bs4 import BeautifulSoup

def test_unique_slugs():

    # Get the directory of the current script (./github/tests)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the sitemap.xml file in the root directory
    sitemap_path = os.path.join(script_dir, '..', '..', '_site', 'sitemap.xml')

    # Read the local sitemap file
    with open(sitemap_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'xml')

    url_elements = soup.find_all('loc')

    skip_slugs = ['integrations', 'routers', 'quality-estimation', 'automatic-post-editing', 'models']
    slugs = []
    for url_element in url_elements:
        url_text = url_element.text.split('/')[-1]
        slug = url_text
        
        # Skip mentioned dirs in skip_slugs
        path_segments = url_element.text.split('/')[3:]
        if any(segment in skip_slugs for segment in path_segments):
            continue

        # Check duplicate/conflicting slugs
        assert slug not in slugs, f'Duplicate Slug {slug} for the URL {url_element.text}: {slug} or unnecessary trailing slash'
        slugs.append(slug)

        # Check path without 'files' prefix
        check_path = url_element.text.split('/')[-2]
        
        if check_path in skip_slugs:
            continue

        # Check that URL is one level deep
        if check_path != 'files':
            assert check_path == 'machinetranslate.org', f'{url_element.text}: Paths should be 1 level deep e.g URL/slug'
