import urllib.request
import re

from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url, num_retries=2, user_agent='wswp', charset='utf-8'):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        # cs = resp.headers.get_content_charset()
        # if not cs:
        cs = charset
        html = resp.read().decode(cs)
        # print(html)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error: ', e.reason)
        html = 'Deu ruim em alguma coisa aí'
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # sitemap is returning None for some reason I don't know yet XD
    # extract the sitemap links 
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here

crawl_sitemap('http://example.webscraping.com/sitemap.xml')