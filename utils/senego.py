from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import TheScraperItem
from scrapy import Spider, Request


class SenegoSpider(Spider):
    name = "senego"
    start_urls = ["https://senego.com/"]

    def parse(self, response):
        urls = response.css(
            "#column_content > div.post-list-home > div > article > div.posts-list-detail > h2 > a::attr(href)"
        ).extract()

        for url in urls:
            yield Request(url, callback=self.parse_article)

    def parse_article(self, response):
        items = TheScraperItem()

        title = response.css("#primary > div.post_single_title > h1::text").extract()
        content = response.css("#primary > div.entry-content").extract()
        author = response.css("#primary > div.author_name::text").extract()
        pub_date = response.css("#primary > time::text").extract()

        items["title"] = title
        items["content"] = content
        items["author"] = author
        items["pub_date"] = pub_date

        yield items
