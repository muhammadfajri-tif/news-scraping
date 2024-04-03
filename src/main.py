from file import get_filepath, save_to_json
from utils import get_html_content, get_headlines_news, parse_headlines_news


def main():
    site_url = "https://www.republika.co.id/"

    # crawl the site
    html_content = get_html_content(site_url)

    #get headline news/trending topics
    headlines = get_headlines_news(html_content)

    # parsed headline to dictionary
    parsed_headlines = parse_headlines_news(headlines)

    #save to json file
    save_to_json(parsed_headlines, get_filepath())

if __name__=="__main__": 
    main()
