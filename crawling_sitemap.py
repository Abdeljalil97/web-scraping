import re
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
#Downloading a web page
def download(url,user_agent='wswp',num_retries=2,charset='utf-8'):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    print(request)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries>0:#retrying dowloading
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html
def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
    # scrape html here
    # ...

download('https://www.amazon.com/')