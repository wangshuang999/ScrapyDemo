# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydemoItem(scrapy.Item):
    # define the fields for your item here like:
    pass


class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()



class TencentHrItem(scrapy.Item):
    info = scrapy.Field()
    type = scrapy.Field()
    num = scrapy.Field()
    address = scrapy.Field()
    time = scrapy.Field()

class DouyuItem(scrapy.Item):
    name = scrapy.Field()
    image_urls = scrapy.Field()
    # two
    src_link = scrapy.Field()


class CrawlSpiderTestItem(scrapy.Item):
    saler = scrapy.Field()
    info = scrapy.Field()



