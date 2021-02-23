# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class TheScraperItem(Item):
    # define the fields for your item here like:
    title = Field()
    content = Field()
    pub_date = Field()
    author = Field()
    url = Field()
