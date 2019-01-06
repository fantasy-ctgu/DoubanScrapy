# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    figure = scrapy.Field()
    types = scrapy.Field()
    star = scrapy.Field()
    comments = scrapy.Field()
    describe = scrapy.Field()