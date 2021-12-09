import pandas as pd

weather_data = {
    'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017'],
    'temperature':[32,31,26,28,19],
    'windspeed':[6,3,5,4,2],
    'event':['Rain','Snow','Sunny','Sunny','Sunny']
}

df = pd.DataFrame(weather_data)
print(df)
#查看形状
print(df.shape)
#查看前5行的内容
print(df.head())
#查看尾部
print(df.tail())
#找出第一行的位置
print(df[0:1])
#访问列的内容
print(df.day)
#访问多列的内容
print(df[['day','temperature']])
#找出该列的最大值
print(df.temperature.max())
#加一个筛选条件，返回筛选后的列表
df2 = df[df.temperature > 20]
print(df2)
#加一个筛选条件，返回筛选后对应列的内容
df3 = df.day[df.temperature > 20]
print(df3)

#把某一列设为索引
df4 = df.set_index('day')
print(df4)
#恢复索引
df5 = df4.reset_index()
print(df5)


