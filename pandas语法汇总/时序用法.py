import pandas as pd

df = pd.read_csv('./data/aapl.csv')


#加载时间序列
df1 = pd.read_csv('./data/aapl.csv',parse_dates=['Date'],index_col='Date')
print(df1)

# df2 = df1['2017-07-07']
# print(df2)

# 重新采样
df2 = df1.Close.head()
print(df2)

df3 = df1.Close.resample('M').mean()
print(df3)