import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
#Downloading a web page
def download(url,user_agent='wswp',num_retries=2):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries>0:#retrying dowloading
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html


download('http://appcatalogo.ifema.es/waCatalogoWeb/index.html?feria=MF17&idioma=es&_ga=2.84562589.565538334.1608543158-1318591213.1608543158#LEMPRESAS&p=1&t=TODO&access&access&access&access&access&access')