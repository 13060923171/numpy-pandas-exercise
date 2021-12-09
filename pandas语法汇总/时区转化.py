import pandas as pd
#查看所有时区
from pytz import all_timezones

df = pd.read_csv('./data/msft.csv',header=1,parse_dates=True,index_col='Date Time')
print(df.head())
#把索引替换成美国时间的索引
df.index = df.index.tz_localize(tz='US/Eastern')
#再把dataframe进行欧洲时间的转换，快速计算美国的时间
df = df.tz_convert('Europe/Berlin')
# df = df.tz_localize(tz='US/Eastern')
print(df)

print(all_timezones)


#data_range 带有时区
london = pd.date_range('2012/3/6 8:00:00',periods=12,freq='H',tz='Europe/Berlin')
print(london)
s = pd.Series(range(12),index=london)
print(s)
s1 = s.tz_convert('US/Eastern')
print(s1)