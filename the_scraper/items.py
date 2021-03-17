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
    video_url = Field()
    has_video = Field()
    number_of_comments = Field()

    # TODO ADD COMMENTS FIELD


class TrainingSetItem(Item):
    body = Field()