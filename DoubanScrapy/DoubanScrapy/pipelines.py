# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import DoubanScrapy.settings as settings

class DoubanscrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class  DoubanscrapyMoviePipeline(object):
    def __init__(self):
        print("this is doubanpipleine init")
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset="utf8",
            use_unicode=True
        )
        self.cursor = self.connect.cursor()
    
    def process_item(self,item,spider):
        print("this is doubanpipeline process_item")
        try:
            self.cursor.execute(
                """
                    select * from doubanmovies where id = %s
                """,
                item['id']
            )
            ans = self.cursor.fetchone()
            if ans:
                pass
            else:
                self.cursor.execute(
                    """insert into doubanmovies(id,name,figure,types,star,comments,describes) 
                    value(%s,%s,%s,%s,%s,%s,%s)""",
                    (item['id'],item['name'],item['figure'],item['types'],item['star'],
                    item['comments'],item['describe'])
                )
                self.connect.commit()
        except Exception as e:
            print(e)
        return item