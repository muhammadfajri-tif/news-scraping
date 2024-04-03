import requests
from bs4 import BeautifulSoup


def get_html_content(uri):
    # request headers
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
            }
    # get html content
    print(f'[INFO] Fetching html content from: {uri} ...')
    url = requests.get(uri, headers=headers)
    if url.status_code == 200 or url.reason == "OK":
        print("[INFO] Success fetching html content.")
        html_content = BeautifulSoup(url.text, "html.parser")
        return html_content
    else:
        raise Exception(f'[ERRO] Failed to fetch data from {uri} with status code: {url.status_code}. {url.raise_for_status()}')

