'''
Author: chaojiewang chaojiewang@deepglint.com
Date: 2023-08-10 10:56:15
LastEditors: chaojiewang chaojiewang@deepglint.com
LastEditTime: 2023-08-29 17:55:29
FilePath: /mySpider/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import matplotlib.pyplot as plt
from pylab import mpl  
import numpy as np
import pandas as pd
import tushare as ts
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签 
mpl.rcParams['axes.unicode_minus']=False  # 用来正常显示负号
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000',
                periods=1000))
ts = ts.cumsum()
ts.plot(figsize=(12,8))
#利用tushare包抓取股票数据并画图
#得到的是DataFrame的数据结构
df=ts.get_k_data('sh',start='1990-01-01')
df.index=pd.to_datetime(df['date'])
df['close'].plot(figsize=(12,8))
plt.title("上证指数走势")