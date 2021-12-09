import pandas as pd

#parse_dates指定哪一列为时间列
df = pd.read_csv('./data/nyc_weather.csv',parse_dates=['EST'])
print(df)
print(df.info())
#如何处理空值
#使用fillna填充空值,当存在空值的时候全部为0
newdf = df.fillna(0)
print(newdf)

#设置不同列的空值填充内容不同
newdf1 = df.fillna(
    {
        'temperature':0,
        'Events':'to Event',
    }
)


#ffill方式填充
#ffill拿前面的一行来填充空值
newdf2 = df.fillna(method='ffill')
print(newdf2)
#拿后面的一行来填充空值
newdf3 = df.fillna(method='bfill')
print(newdf3)


#interpolate
df1 = df.set_index('EST')
#用拟合的方式去处理nan，但是索引要是时间类型才行
newdf4 = df1.interpolate(method='time')
print(newdf4)

#dropna直接删除全部的包含nan的那一行
#在how里面有all和any，all代表的是那一行必须全部都是缺失才删除，any是指只要出现一个any就要全部删除
newdf5 = df.dropna(how='any')
print(newdf5)

#对应就是在缺失的那一列，只要存在1个数值就不会缺失，把1改为2，那么就是要存在2个数值才不会被删除
newdf6 = df.dropna(thresh=1)
print(newdf6)


