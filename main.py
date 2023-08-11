'''
Author: chaojiewang chaojiewang@deepglint.com
Date: 2023-08-10 10:56:15
LastEditors: chaojiewang chaojiewang@deepglint.com
LastEditTime: 2023-08-10 11:19:01
FilePath: /mySpider/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from scrapy.cmdline import execute

import os 
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 如果要运行其他的网络爬虫，只需修改上面代码中字符串里面的命令即可 
execute(["scrapy", "crawl", "first_spider"," -o"," info.csv"])
#或者
# cmdline.execute("scrapy crawl itcast -o info.csv -t csv".split()) 