import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

# file_path = '../../_site/sitemap.xml'
# tree = ET.parse(file_path)
# root = tree.getroot()
# urls = []

# for url_element in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
#     url_text = url_element.text.strip()  # Strip leading and trailing whitespaces
#     print(url_text)

#     # Add an assertion to check a condition
#     assert url_text.split('/')[-1] not in urls, f'Duplicate URL: {url_text}'

#     urls.append(url_text)
def test_unique_slugs():
    data = requests.get('https://machinetranslate.org/sitemap')
    soup = BeautifulSoup(data.text, 'xml')
    url_elements = soup.find_all('loc')
    urls = []

    for url_element in url_elements:
        # url_text = url_element.split('/')[-1]  # Strip leading and trailing whitespaces
        # print(url_text)
        slug = url_element.text.split('/')[-1]
        # Add an assertion to check a condition
        assert slug not in urls, f'Duplicate Slug {slug} for the URL {url_element.text}: {slug}'

        urls.append(slug)