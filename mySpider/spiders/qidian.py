'''
Author: chaojiewang chaojiewang@deepglint.com
Date: 2023-08-10 11:25:26
LastEditors: chaojiewang chaojiewang@deepglint.com
LastEditTime: 2023-08-10 14:26:15
FilePath: /mySpider/mySpider/spiders/Qidian.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import scrapy
from mySpider.items import QidianspiderItem

class QidianSpider(scrapy.Spider):
    name = "qidian"
    allowed_domains = ["www.qidian.com"]
    start_urls = ["https://www.qidian.com/all"]
    template_url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=%d'
    page_num = 2
    def parse(self, response):
        # TODO 2.数据解析
        li_list = response.xpath('//div[@class="all-book-list"]/div/ul/li')
        for li in li_list:
            # 实例化 QidianspiderItem 对象
            item = QidianspiderItem()
            # 使用xpath提取小说中的标题及详情页的链接
            title = li.xpath('./div[2]/h2/a/text()').extract_first()
            detail_url = response.urljoin(li.xpath('./div[2]/h2/a/@href').extract_first())
            item['title'] = title   # 标题直接放入 Item 中
            # author 需要深度挖掘，打开新的链接页面获得
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})
            
        if self.page_num <= 5:
            new_url = format(self.template_url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        author = response.xpath('//p[@class="author-name"]/span[1]/text()').extract_first()  
        item['author'] = author
        yield item    # 把控制权给管道
