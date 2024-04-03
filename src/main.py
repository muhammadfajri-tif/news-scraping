from utils import get_html_content, get_headlines_news


def main():
    site_url = "https://www.republika.co.id/"

    # crawl the site
    html_content = get_html_content(site_url)

    #get headline news/trending topics
    headlines = get_headlines_news(html_content)


if __name__=="__main__": 
    main()
