'''
Author: chaojiewang chaojiewang@deepglint.com
Date: 2023-03-05 15:53:58
LastEditors: chaojiewang chaojiewang@deepglint.com
LastEditTime: 2023-08-10 14:40:30
FilePath: /mySpider/mySpider/items.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QidianspiderItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()

class DoubanItem(scrapy.Item):
    ranking = scrapy.Field()
    name = scrapy.Field()
    ratingNum = scrapy.Field()
