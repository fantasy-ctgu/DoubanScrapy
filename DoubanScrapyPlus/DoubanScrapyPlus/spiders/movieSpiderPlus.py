# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from DoubanScrapyPlus.items import DoubanMovieItem

class MoviespiderplusSpider(scrapy.Spider):
    name = 'movieSpiderPlus'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250/']

    def parse(self, response):
        movieList = response.xpath(
            "//div[@class='article']/ol[@class='grid_view']//li")
        for movie in movieList:
            movieLoader = ItemLoader(DoubanMovieItem(),movie)
            movieLoader.add_xpath("id",".//em/text()")
            movieLoader.add_xpath('name',".//div[@class='hd']/a/span[@class='title']//text()")
            movieLoader.add_xpath('figure',".//div[@class='info']/div[@class='bd']/p[1]//text()")
            movieLoader.add_xpath('types',".//div[@class='info']/div[@class='bd']/p[1]//text()")
            movieLoader.add_xpath('star',".//div[@class='star']/span[@class='rating_num']//text()")
            movieLoader.add_xpath('comments',".//div[@class='star']/span[4]//text()")
            movieLoader.add_xpath('describe',".//div[@class='bd']/p[@class='quote']/span[@class='inq']/text()")
            yield movieLoader.load_item()
        next_link = response.xpath(
            "//div[@class='paginator']/span[@class='next']/a/@href").extract_first()
        if next_link:
            # yield scrapy.Request("http://movie.douban.com/top250/"+next_link,callback=self.parse)
            yield scrapy.Request(response.urljoin(next_link), callback=self.parse)
