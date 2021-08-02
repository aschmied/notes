import requests
import requests.adapters
import urllib3.util

def main():
    url = 'http://localhost:32000'
    session = build_session(url)
    session.post(url, data={'yup': 'nope'})

def build_session(url):
    session = requests.Session()
    retry_policy = urllib3.util.Retry(total=3, method_whitelist=frozenset(['GET', 'POST']))
    session.mount(url, requests.adapters.HTTPAdapter(max_retries=retry_policy))
    return session

if __name__ == '__main__':
    main()
