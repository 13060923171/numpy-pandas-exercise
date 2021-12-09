import pandas as pd
import numpy as np
import datetime
import pytz

invoices = pd.read_csv('./data/invoices.csv')
#设置可以展示的行数
pd.set_option('display.max_rows',4)
invoices['Date of Meal'] = pd.to_datetime(invoices['Date of Meal'],utc=True)
#年月日的提取
print(invoices['Date of Meal'].dt.date)
# #查看是星期几
# print(invoices['Date of Meal'].dt.weekday_name)
#月份
print(invoices['Date of Meal'].dt.month)
#日
print(invoices['Date of Meal'].dt.day)
#这个月有多少天
print(invoices['Date of Meal'].dt.days_in_month)
#季度
print(invoices['Date of Meal'].dt.quarter)
#年
print(invoices['Date of Meal'].dt.year)
#是否是该月的最后一天
print(invoices['Date of Meal'].dt.is_month_end)
#把该月的最后一天展示出来
print(invoices[invoices['Date of Meal'].dt.is_month_end])
#全部小写
invoices['Type of Meal'] = invoices['Type of Meal'].str.lower()
#全部大写
invoices['Type of Meal'] = invoices['Type of Meal'].str.upper()
#左对齐
invoices['Type of Meal'] = invoices['Type of Meal'].str.zfill(width=15)
#把小写变大写，大写变小写
invoices['Type of Meal'] = invoices['Type of Meal'].str.swapcase()
#重复自身的倍数
invoices['Type of Meal'] = invoices['Type of Meal'].str.repeat(2)
#查看是否存在ast
invoices['Type of Meal'] = invoices['Type of Meal'].str.endswith('ast')
#先全部小写，然后再把首字母变成大写
invoices['Type of Meal'] = invoices['Type of Meal'].str.lower().str.title()
#模糊查询
invoices['Type of Meal'] = invoices['Type of Meal'].str.contains('David')
#该列是否有排序过
invoices['Type of Meal'] = invoices['Type of Meal'].cat.ordered
#找出有多少个类
invoices['Type of Meal'] = invoices['Type of Meal'].cat.categories
#查看排序的规律
invoices['Type of Meal'] = invoices['Type of Meal'].cat.codes