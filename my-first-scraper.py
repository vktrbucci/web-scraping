# import urllib.request

# def download(url):
#     return urllib.request.urlopen(url).read()

# # Aqui temos erro se a url passada não existir:
# ## erro de digitação, página não encontrada ou qualquer outro motivo
# print(download("http://example.webscraping.com"))


# Um meio mais robusto de construir esse scraper seria:
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

# Sem um user-agent definido, muitas requisições retornam 403 FORBIDDEN
def download(url, num_retries, user_agent='wswp'):
    print('Downloading: ', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        html = urllib.request.urlopen(request).read()
        print('Url fetched')
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error: ', e.reason)
        html = None
        # verifica se ainda existem tentativas
        if num_retries > 0:
            # verifica por erros HTTP 5xx
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # faz novas tentativas recursivamente
                return download(url, num_retries - 1)
    return html

target_url = 'https://www.fundamentus.com.br/detalhes.php?papel=WHRL4'
download(target_url, 2)
