from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from the_scraper.items import TheScraperItem
from the_scraper.selectors import SELECTORS


class ArticleSpider(CrawlSpider):
    name = "article"
    allowed_domains = [
        ".".join(SELECTORS["website"].split(".")[1:]),
    ]
    start_urls = [SELECTORS["website"]]

    rules = [
        Rule(
            LinkExtractor(),
            callback="parse_item",
            follow=True,
        )
    ]

    def parse_item(self, response):
        item = TheScraperItem()

        if response.url.find(self.allowed_domains[0]) != -1:
            item["url"] = response.url
            item["title"] = response.css(SELECTORS["title"]).get()
            item["content"] = response.css(SELECTORS["content"]).get()
            item["pub_date"] = response.css(SELECTORS["pub_date"]).get()
            item["author"] = response.css(SELECTORS["author"]).get()
            item["number_of_comments"] = response.css(
                SELECTORS["number_of_comments"],
            ).get()

            video_url = response.css(SELECTORS["video_url"]).get()
            if video_url is not None:
                item["has_video"] = "True"
                item["video_url"] = video_url
            else:
                item["has_video"] = "False"
                item["video_url"] = "-"

        yield item
