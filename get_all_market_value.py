# -*- coding: utf-8 -*-

from datetime import datetime
import pandas as pd
from jqdatasdk import *
import sys
phone = sys.argv[1]
psw = sys.argv[2]
auth(phone,psw) #账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位

# 获取全市场股票PE
query_date = datetime.now().strftime('%Y-%m-%d')
all_stock = get_all_securities(['stock'], date=query_date)
stocks = list(all_stock.index)
print ( "whole chinese market has ", len(stocks), " stocks")

stock1 = stocks[:2000]
stock2 = stocks[2000:]

q1 = query(
    valuation.code, valuation.day, valuation.pe_ratio, valuation.pb_ratio
).filter(
    valuation.code.in_(stock1)
)
df1 = get_fundamentals(q1, date=query_date)
print ( df1.head(30) ) 
# df1.to_sql(name='stock_valuations', if_exists='append', con=conn, index=False)

q2 = query(
    valuation.code, valuation.day, valuation.pe_ratio, valuation.pb_ratio
).filter(
    valuation.code.in_(stock2)
)
df2 = get_fundamentals(q2, date=query_date)
# df2.to_sql(name='stock_valuations', if_exists='append', con=conn, index=False)

stock_fund = pd.concat([df1, df2]).set_index('code')

# 计算全市场等权PE
# pe_ew = len(stock_fund["pe_ratio"]) / stock_fund["pe_ratio"].apply(get_pe_trans).sum()
# print(" 全市场等权PE=", pe_ew)

# 计算全市场等权PB
# pb_ew = len(stock_fund["pb_ratio"]) / stock_fund["pb_ratio"].apply(get_pe_trans).sum()
# print(" 全市场等权PB=", pb_ew)