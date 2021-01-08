# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user = scrapy.Field()
    review = scrapy.Field()
    topic = scrapy.Field()
    timestamp = scrapy.Field()
    source = scrapy.Field()
    pass
