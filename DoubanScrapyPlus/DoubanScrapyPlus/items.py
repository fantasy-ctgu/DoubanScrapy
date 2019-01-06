# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class DoubanscrapyplusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def replaceNull(value):
    return re.sub(r'[\n\xa0 ]','',value)

def figureFun(value):
    return replaceNull(value)

def typesFun(value):
    if re.findall(r'\d+',value):
        return replaceNull(value)

class DoubanMovieItem(scrapy.Item):
    id = scrapy.Field(output_processor = TakeFirst())
    name = scrapy.Field(output_processor = TakeFirst())
    figure = scrapy.Field(input_processor=MapCompose(figureFun),output_processor = TakeFirst())
    types = scrapy.Field(input_processor=MapCompose(typesFun),output_processor = TakeFirst())
    star = scrapy.Field(output_processor = TakeFirst())
    comments = scrapy.Field(output_processor = TakeFirst())
    describe = scrapy.Field(output_processor = TakeFirst())

    def getInsertSql(self):
        '''获取插入数据的sql语句'''
        insertSql = """
            insert into doubanmovies(id,name,figure,types,star,comments,describes) 
            value(%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE 
            name=VALUES(name),figure=VALUES(figure),types=VALUES(types),
            star=VALUES(star),comments=VALUES(comments),describes=VALUES(describes)
        """
        params = (self['id'],self['name'],self['figure'],self['types'],
        self['star'],self['comments'],self['describe'])
        return insertSql,params
