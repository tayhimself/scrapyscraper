import scrapy
import re

## This spider gets all youtube links from the railroader sleep website
## and writes them to a text file

class RrBotSpider(scrapy.Spider):
    name = 'rr_youtube'
    allowed_domains = ['railroadersleep.fra.dot.gov']
    start_urls = ['http://railroadersleep.fra.dot.gov/']
    links = []

    def __init__(self):
        self.links=[]
        self.links.append('http://railroadersleep.fra.dot.gov/')
        self.filename = f'rrsleep-youtube.txt'

    def parse(self, response):
        # get all youtube links
        for link in response.css("a.embededVideo"):
            link = link.css("a.embededVideo::attr(href)").get()
            if "youtube" in link and link not in self.links:
                # get the embed code from the youtube link
                embed_code = re.search(r"embed/([\w-]+)", link).group(1)
                # Construct the new URL
                new_url = f"https://www.youtube.com/embed/{embed_code} on{response.url}\r\n"
                self.links.append(new_url)
                with open(self.filename, 'a') as f:
                    yield f.write(new_url)

        # get all links to other pagesXB

        # get the next pages to crawl
        for href in response.css('a::attr(href)'):
            if "pdf" not in href.get() and "mailto" not in href.get():
                self.links.append(response.url)
                yield response.follow(href, self.parse)