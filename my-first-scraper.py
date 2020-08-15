# import urllib.request

# def download(url):
#     return urllib.request.urlopen(url).read()

# # Aqui temos erro se a url passada não existir:
# ## erro de digitação, página não encontrada ou qualquer outro motivo
# print(download("http://example.webscrapping.cm"))


# Um meio mais robusto de construir esse scraper seria:
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url):
    print('Downloading: ', url)
    try:
        html = urllib.request.urlopen(url).read()
        print('Url fetched')
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error: ', e.reason)
        html = None
    return html

download("http://example.webscraping.om")