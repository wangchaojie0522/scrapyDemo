'''
Author: chaojiewang chaojiewang@deepglint.com
Date: 2023-08-10 14:33:00
LastEditors: chaojiewang chaojiewang@deepglint.com
LastEditTime: 2023-08-10 14:48:36
FilePath: /mySpider/mySpider/spiders/doubanTop.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import scrapy
from mySpider.items import DoubanItem

class DoubantopSpider(scrapy.Spider):
    name = "doubanTop"
    allowed_domains = ["www.movie.douban.com"]
    start_urls = ["http://www.movie.douban.com/top250"]
    template_url = "https://movie.douban.com/top250?start=%d&filter="
    page_num = 2
    def parse(self, response):
         # TODO 2.数据解析
        li_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')

        for li in li_list:
             # 实例化 QidianspiderItem 对象
            item = DoubanItem()
            ranking = li.xpath('./div/div[1]/em/text()').extract_first()
            name = li.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract_first()
            ratingNum = li.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract_first()
            item['ranking'] = ranking[0]
            item['name'] = name[0]
            item['ratingNum'] = ratingNum[0]
            yield

        if self.page_num <= 10:
            new_url = format(self.template_url % (self.page_num-1)*25)
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)
