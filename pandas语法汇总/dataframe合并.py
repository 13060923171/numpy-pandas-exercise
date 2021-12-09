import pandas as pd
import datetime
import numpy as np
invoices = pd.read_csv('./data/invoices.csv')
#设置可以展示的行数
pd.set_option('display.max_rows',8)
invoices['Date of Meal'] = pd.to_datetime(invoices['Date of Meal'],utc=True)
#把该列做一个汇总
a = invoices['Date of Meal'].dt.year.value_counts().sort_index()
y_2013 = invoices[invoices['Date of Meal'].dt.year == 2013].copy()
y_2014 = invoices[invoices['Date of Meal'].dt.year == 2014].copy()
#垂直连接
df1 = pd.concat([y_2013,y_2014],names=['year','original_index'])
print(df1)


range_a = pd.date_range(datetime.datetime(2019,1,2),datetime.datetime(2019,1,10))
df_a = pd.DataFrame(index=range_a,data = np.random.randint(2,10,size=len(range_a)),columns=['observations_A'])

range_b = pd.date_range(datetime.datetime(2019,1,5),datetime.datetime(2019,1,13))
df_b = pd.DataFrame(index=range_b,data=np.random.randint(2,10,size=len(range_b)),columns=['observations_B'])
#水平合并
df2 = pd.concat([df_a,df_b],axis=1)
print(df2)

order = pd.read_csv('./data/order_leads.csv',parse_dates=[3])
sales = pd.read_csv('./data/sales_team.csv')
#how的用法 inner并集 outer合集 left right对应就是左连接和右连接
# df3 = pd.merge(order,invoices,how='left')
# print(df3)
#on 类似数据库中的join，用哪一列作为连接字段，suffixes用法和on一样，只是_base该字符存在都可以直接使用
# df3 = pd.merge(order,invoices,on='Order Id',suffixes=('_base','_join'))
# print(df3)
#把两个表格进行查询
lookup = sales.set_index('Company Name')['Sales Rep']
order['Sales Rep'] = order['Company Name'].map(lookup)
print(order)