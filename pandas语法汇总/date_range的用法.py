import pandas as pd

#加载时间序列
df1 = pd.read_csv('./data/aapl_no_dates.csv')
print(df1)

#生成时间序列,freq='B'特指工作日
rng = pd.date_range(start='6/1/2016',end='6/30/2016',freq='B')
df2 = df1.set_index(rng)
print(df2)

#快速找到缺失的日期
rng2 = pd.date_range(start='6/1/2016',end='6/30/2016')
rng3 = rng2.difference(rng)
print(rng3)

#时间范围，以小时为分割器
rng4 = pd.date_range(start='6/1/2016',end='6/30/2016',freq='12H')
print(rng4)

#以月为分割器
rng5 = pd.date_range(start='6/1/2016',end='11/30/2016',freq='M')
print(rng5)

#asfreq把空缺日期进行填充
df3 = df2.asfreq('D',method='pad')
print(df3)

#周的日期
df4 = df2.asfreq('W',method='pad')
print(df4)

#date_range第二种使用方法,从这天开始，生成60天
rng6 = pd.date_range(start='2016-07-01',periods=70)
print(rng6)

import numpy as np

ts = pd.Series(np.random.randint(0,10,len(rng)),index=rng)
print(ts.head())

df5 = pd.DataFrame(ts)
print(df5.head())

plt = df5['2016-06-01':'2016-06-07'].plot()

