# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjxfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    district = scrapy.Field()
    region = scrapy.Field()
    address = scrapy.Field()
    status = scrapy.Field()
    money = scrapy.Field()
    # pass
