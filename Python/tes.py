import requests
import threading
import logging



def get_connections(url):
    r = requests.get(url)
    r.headers.update({'Content-Type': 'application/json'})
    for key in r.headers:
        print(key + ': ' + r.headers[key])
        if r.headers[key] == '200 OK':
            print('200 OK')
        for headers in r.cookies:
            print(headers + ': ' + r.cookies[headers])
    return url

def debug_url(url):
    r = requests.get(url)
    for key in r.headers:
        key = r.headers[key]
        print(key, end='\n', flush=True)
    return r


def debug_mode(url):
    r = requests.get(url)
    for debug_mode in r.headers:
        (debug_mode + ': ' + r.headers[debug_mode])
    return url


def logging_url(url):
    l = logging.getLogger(url)
    l.setLevel(logging.DEBUG)
    l.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    l.addHandler(logging.StreamHandler())
    l.info(url)
    return url

while True:
    logging.basicConfig(level=logging.DEBUG)
    logging.DEBUG_URL = debug_url('https://github.com/')
    current_thread = threading.current_thread()
    get_connections('https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/chunks/polyfills-220b45bce3a97adf0cc4.js')
    get_connections('https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/chunks/94a7ad86-033888364311d66830a4.js')
    get_connections('https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/chunks/pages/us/en/about/crypto-f5fbdec74ae340fff695.js')
    get_connections('https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/chunks/pages/_app-899177335c4fbfc759b0.js')
    debug_url('https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/chunks/pages/us/en/about/crypto-f5fbdec74ae340fff695.js')
    debug_url('https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/chunks/pages/_app-899177335c4fbfc759b0.js')
    debug_mode('https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/chunks/6283-04574aeeb0ddeadb3fd5.js')
    logging_url('https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/chunks/polyfills-220b45bce3a97adf0cc4.js')