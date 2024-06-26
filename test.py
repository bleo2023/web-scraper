from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def main():
    url = "https://www.squarespace.com/websites/create-a-blog?channel=pnb&subchannel=go&campaign=pnb-go-us-en-core_verticals_blog_tier1-e&subcampaign=(blog_blog-sites_e)&&cid=13842267311&aid=125919727178&tid=kwd-21745091&mt=e&eid=&loc_p_ms=9004166&loc_i_ms=&nw=g&d=c&adid=532615424535&channel2=pnb&subchannel2=go&gad_source=1&gclid=CjwKCAjw-O6zBhASEiwAOHeGxWUYL5OS3R5zJ2Fx923S2WkghCD6VlgrQDMnTBQ83JOrZWgFr_kGTBoCa6oQAvD_BwE&gclsrc=aw.ds"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    with open('extracted-data.txt', 'a', encoding='utf-8') as file:
        for element in soup.find_all(attrs='feature-text__right'):
            # Find <h1> tag inside each found <div>
            paragraphs = element.find("p")
            if paragraphs:
                file.write(paragraphs.text.strip() + '\n')


if __name__ == "__main__":
    main()
