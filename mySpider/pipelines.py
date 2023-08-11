'''
Author: chaojiewang chaojiewang@deepglint.com
Date: 2023-03-05 15:53:58
LastEditors: chaojiewang chaojiewang@deepglint.com
LastEditTime: 2023-08-10 11:30:01
FilePath: /mySpider/mySpider/pipelines.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyspiderPipeline:
    # fp = None
    # 重写父类的一个方法: 该方法只在开始爬虫的时候被调用1次
    def open_spider(self, spider):
        print("开始爬虫。。。")
        # self.fp = open('blog.tex', 'w', encoding='utf8')
    # 专门用来处理 item类型的对象，该方法可以接收爬虫脚本提交过来的item对象
    # 注意: 该方法每接收到一个 item就会被调用一次
    def process_item(self, item, spider):
        print(item)
        return item
    def close_spider(self, spider):
        print('结束爬虫')
        # self.fp.close()
