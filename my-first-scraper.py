# import urllib.request

# def download(url):
#     return urllib.request.urlopen(url).read()

# # Aqui temos erro se a url passada não existir:
# ## erro de digitação, página não encontrada ou qualquer outro motivo
# print(download("http://example.webscraping.com"))


# Um meio mais robusto de construir esse scraper seria:
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url, num_retries=2):
    print('Downloading: ', url)
    try:
        html = urllib.request.urlopen(url).read()
        print('Url fetched')
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error: ', e.reason, e.code)
        html = None
        # verifica se ainda existem tentativas
        if num_retries > 0:
            print("Ainda temos tentativas")
            # verifica por erros HTTP 5xx
            if hasattr(e, 'code') and 400 <= e.code < 600:
                # faz novas tentativas recursivamente
                return download(url, num_retries - 1)
    return html

target_url = "http://httpstat.us/500"
download(target_url)
# retorna 403 FORBIDDEN pois não tem UserAgent