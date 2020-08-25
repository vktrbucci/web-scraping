import urllib.request
import itertools

from urllib.error import URLError, HTTPError, ContentTooShortError


def download(url, num_retries=2, user_agent='wswp', charset='utf-8'):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
        
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error: ', e.reason)
        html = 'Deu ruim em alguma coisa aí'
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html

def crawl_site(url):
    for page in itertools.count(1):
        page_url = '{}{}'.format(url, page)
        html = download(page_url)
        if html is None:
            break
        # success - scrape the result


crawl_site('http://example.webscraping.com/places/default/view/-')