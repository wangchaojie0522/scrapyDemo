'''
Author: chaojiewang chaojiewang@deepglint.com
Date: 2023-08-10 15:02:11
LastEditors: chaojiewang chaojiewang@deepglint.com
LastEditTime: 2023-08-10 15:02:33
FilePath: /mySpider/mySpider/randomAgentMiddleware.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import scrapy
from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random
 

class MyUserAgentMiddleware(UserAgentMiddleware):
    '''
    设置User-Agent
    '''
 
    def __init__(self, user_agent):
        self.user_agent = user_agent
 
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent=crawler.settings.get('USER_AGENTS_LIST')
        )
 
    def process_request(self, request, spider):
        agent = random.choice(self.user_agent)
        request.headers['User-Agent'] = agent
