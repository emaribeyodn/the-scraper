# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3


class TheScraperPipeline:
    def __init__(self) -> None:
        self.create_connection()
        self.create_table()

    def create_connection(self) -> None:
        self.conn = sqlite3.connect("the_scraper.db")
        self.curr = self.conn.cursor()

    def create_table(self) -> None:
        self.curr.execute("""DROP TABLE IF EXISTS articles""")
        self.curr.execute(
            """CREATE TABLE articles(
                url TEXT,
                author TEXT,
                pub_date TEXT,
                title TEXT, 
                content TEXT,
                number_of_comments TEXT,
                has_video TEXT,
                video_url TEXT
            )"""
        )

    def process_item(self, item, spider):
        self.store_article(item)
        return item

    def store_article(self, item) -> None:
        self.curr.execute(
            """INSERT INTO articles values (?,?,?,?,?,?,?,?)""",
            (
                item["url"],
                item["author"],
                item["pub_date"],
                item["title"],
                item["content"],
                item["number_of_comments"],
                item["has_video"],
                item["video_url"],
            ),
        )

        self.conn.commit()
