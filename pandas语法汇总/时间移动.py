import pandas as pd

df = pd.read_csv('./data/fb.csv',parse_dates=True,index_col= 'Date')
print(df)

#shift
print(df)
print(df.shift(1))

df['Prev Day Price'] = df['Price'].shift(1)
print(df.head())

df['Price Change'] = df['Price'] - df['Prev Day Price']
print(df.head())

df['5 day return'] = ((df['Price'] - df['Price'].shift(5)) / df['Price'].shift(5)) * 100
print(df.head(15))
#该索引值
df1 = df.tshift(1)


#diff
df2 = pd.DataFrame({
    'a':[1,2,3,4,5,6,7],
    'b':[1,2,3,4,5,6,7],
    'c':[1,2,3,4,5,6,7],
})

#下面的行减上面的行
df2 = df2.diff()
print(df2)
#列减
df2 = df.diff(axis=1)
print(df2)

#往前面减1天
df3 = df2.diff(periods=-1)
print(df3)

#diff = df - df.shift()
