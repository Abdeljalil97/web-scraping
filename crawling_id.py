import re
import itertools
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
def crawl_site(url, max_errors=5):
    for page in itertools.count(1):
        pg_url = '{}{}'.format(url, page)
        html = download(pg_url)
    if html is None:
        num_errors += 1
    if num_errors == max_errors:
    # max errors reached, exit loop
        break
    else:
        num_errors = 0
    # success - can scrape the result