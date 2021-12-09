import pandas as pd
dates = ['2017-01-01','Jan 5 , 2017','01/06/2017','2017.05.01','20170501']

df1 = pd.to_datetime(dates)
print(df1)

dates1 = ['2017-01-01 2:30:00 pm','Jan 5 , 2017','01/06/2017','2017.05.01','20170501']

df2 = pd.to_datetime(dates1)
print(df2)


#日期风格
a = pd.to_datetime('2017-01-01')
print(a)
#选定第一个数是天数
b = pd.to_datetime('12-11-2017',dayfirst=True)
print(b)
c = pd.to_datetime('2017|06|01',format='%Y|%m|%d')
print(c)
d = pd.to_datetime('2017,06,01',format='%Y,%m,%d')
print(d)
#面对一些无效数据的时候把这些无效数据替换掉
e = pd.to_datetime(['2017-01-01','2017-09-32'],errors='coerce')
print(e)

#时间戳处理
f = pd.to_datetime(1501325555,unit='s')
print(f)
print(type(f))
#把时间戳数据类型变为时间类型类型
e = pd.to_datetime([1501325555],unit='s')
print(e)