from scrapy.spiders import Spider
from the_scraper.items import TheScraperItem


class SenegoSpider(Spider):

    name = "senego"
    allowed_domains = ["senego.com"]
    start_urls = ["https://senego.com/"]

    def parse(self, response):
        article_urls = response.css("a.posts-list-link::attr('href')").extract()
        for url in article_urls:
            yield response.follow(url, callback=self.parse_article)

        next_page = response.css("div.listPagination .next-post::attr('href')").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_article(self, response):
        item = TheScraperItem()

        item["url"] = response.url
        item["title"] = response.css("h1.entry-title::text").get()
        item["pub_date"] = response.css("time.single-post-time::attr(datetime)").get()
        item["author"] = response.css("div.author_name::text").get()
        item["content"] = response.css("div.entry-content").get()

        is_video = response.css("div.entry-content > p > iframe::attr('src')").get()
        if is_video is not None:
            item["has_video"] = "True"
            item["video_url"] = is_video
        else:
            item["has_video"] = "False"
            item["video_url"] = "-"

        yield item
