from scrapy.spiders import Spider
from the_scraper.items import TrainingSetItem


class TrainingSetSpider(Spider):

    name = "trset"
    allowed_domains = ["senego.com"]
    start_urls = ["https://www.senego.com/"]

    custom_settings = {"CLOSESPIDER_PAGECOUNT": 120}

    def parse(self, response):
        # article_urls = response.css(
        #     "div.module_news_item_content > a.module_news_item_title::attr('href')"
        # ).extract()
        # for url in article_urls:
        #     yield response.follow(url, callback=self.parse_article)
        article_urls = response.css("a.posts-list-link::attr('href')").extract()
        for url in article_urls:
            yield response.follow(url, callback=self.parse_article)

        next_page = response.css("div.listPagination .next-post::attr('href')").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_article(self, response):
        item = TrainingSetItem()
        item["body"] = response.css("body").get()

        yield item
