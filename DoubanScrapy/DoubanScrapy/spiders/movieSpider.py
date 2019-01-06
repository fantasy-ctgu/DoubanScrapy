# -*- coding: utf-8 -*-
import scrapy
from DoubanScrapy.items import DoubanMovieItem

class MoviespiderSpider(scrapy.Spider):
    name = 'movieSpider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250/']

    def parse(self, response):
        movieList = response.xpath(
            "//div[@class='article']/ol[@class='grid_view']//li")
        for movie in movieList:
            movieItem = DoubanMovieItem()
            movieItem['id'] = movie.xpath(".//em/text()").extract_first()
            movieItem['name'] = movie.xpath(
                ".//div[@class='hd']/a/span[@class='title']//text()").extract_first()
            movieItem['figure'] = "".join(movie.xpath(
                ".//div[@class='info']/div[@class='bd']/p[1]//text()").extract_first().strip().split()[:-1])
            movieItem['types'] = movie.xpath(
                ".//div[@class='info']/div[@class='bd']/p//text()").extract()[1].strip().replace('\xa0', ' ')
            movieItem['star'] = movie.xpath(
                ".//div[@class='star']/span[@class='rating_num']//text()").extract_first()
            movieItem['comments'] = movie.xpath(
                ".//div[@class='star']/span[4]//text()").extract_first()
            movieItem['describe'] = movie.xpath(
                ".//div[@class='bd']/p[@class='quote']/span[@class='inq']/text()").extract_first()
            yield movieItem
        next_link = response.xpath(
            "//div[@class='paginator']/span[@class='next']/a/@href").extract_first()
        if next_link:
            # yield scrapy.Request("http://movie.douban.com/top250/"+next_link,callback=self.parse)
            yield scrapy.Request(response.urljoin(next_link), callback=self.parse)
