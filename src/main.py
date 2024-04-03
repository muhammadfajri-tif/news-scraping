from utils import get_html_content

def main():
    site_url = "https://www.republika.co.id/"

    # crawl the site
    html_content = get_html_content(site_url)

if __name__=="__main__": 
    main()
