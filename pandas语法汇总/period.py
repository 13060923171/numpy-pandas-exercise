import pandas as pd

#year period
y = pd.Period('2019')
print(y)
#开始时间
print(y.start_time)
#结束时间
print(y.end_time)
#判断是否是闰年
print(y.is_leap_year)


#月周期
m = pd.Period('2019-05')
print(m)
print(m.start_time)
print(m.end_time)
#下一个月
print(m+1)

d = pd.Period('2019-07-10',freq='D')
print(d)
print(d+10)

h = pd.Period('2019-07-10 23:00:00',freq='H')
print(h)
print(h+5)

#季度
q1 = pd.Period('2017q1',freq='q-dec')
print(q1)
print(q1.start_time)
print(q1.end_time)

#把季度转化为月份
print(q1.asfreq('M'))

#周
w = pd.Period('2017-07-06',freq='W')
print(w)
print(w-1)

#period index
r = pd.period_range('2011','2017',freq='q')
print(r)
print(r[0])

r1 = pd.period_range('2011','2017',freq='3m')
print(r1)

#数据案例
import numpy as np

ps = pd.Series(np.random.randn(len(r1)),r1)
print(ps)
print(ps['2016':'2017'])

df = pd.read_csv('./data/wmt.csv')
df = df.set_index('Line Item')
df = df.T
df.index = pd.PeriodIndex(df.index,freq='q-jan')
df['Start Date'] = df.index.map(lambda x:x.start_time)
df['End Date'] = df.index.map(lambda x:x.end_time)
print(df.index[0].start_time)

print(df)