import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def content_parser(html_el):
    return html_el.text.strip()

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

def get_headlines_news(html_content):
    return html_content.find_all("div", class_="max-card__title")

def parse_headlines_news(headlines):
    data = []
    # parse headlines
    for headline in headlines:
        #get title
        title = content_parser(headline.find("h2", {"class": re.compile('headline-*')}))
        # get category and time published
        info = content_parser(headline.find("div", {"class": "date date-item__headline"}))
        # attach to dictionary
        data.append({
            "judul": title,
            "kategori": info.split('-')[0].strip(),
            "waktu_publish": info.split('-')[1].strip(),
            "waktu_scraping": datetime.now()
        })

    return data


