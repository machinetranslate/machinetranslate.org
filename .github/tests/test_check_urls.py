import concurrent.futures
import requests
from bs4 import BeautifulSoup
import pytest


class TestSitemapRequests:
    """ Class for checking 404 pages """

    # Fixture to create a session for each test method
    @pytest.fixture
    def session(self):
        with requests.Session() as session:
            yield session

    # Helper function to fetch a URL with retries
    def fetch_url(self, session, url):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = session.get(url)
                response.raise_for_status()
                return url, response.status_code
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    print(f"Retrying {url} (Attempt {attempt + 1})")
                else:
                    print(f"Error for URL {url}: {e}")
                    return url, 0

    # Test method for sitemap requests
    def test_sitemap_requests(self, session):
        base_url = 'https://machinetranslate.org'
        sitemap_url = base_url + '/sitemap'

        # Timeout for HTTP requests
        timeout = 20

        # Fetch the sitemap
        response = session.get(sitemap_url, timeout=timeout)
        assert response.status_code == 200

        # Parse the sitemap using BeautifulSoup
        soup = BeautifulSoup(response.text, 'xml')
        url_elements = soup.find_all('loc')

        # Extract URLs from the sitemap
        urls = [url_element.text for url_element in url_elements]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.fetch_url, session, url) for url in urls]
        
        # Collect URLs with non-200 status codes
        not_found_urls = []
        for future in concurrent.futures.as_completed(futures):
            url, status_code = future.result()
            if status_code != 200:
                not_found_urls.append(url)

        # Assert that there are no URLs with non-200 status codes
        assert len(not_found_urls) == 0
