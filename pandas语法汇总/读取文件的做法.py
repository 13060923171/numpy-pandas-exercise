import pandas as pd

df = pd.read_csv('./data/nyc_weather.csv')

#读取headers
a = list(df.columns)
print(a)

def number(x):
    pass
#允许某一行调用函数功能
df1 = pd.read_excel('1.xlsx',sheet_name='sheet',converters={'price':number})


#合并两个dataframe
with pd.ExcelWriter('combine.xlsx')as write:
    df.to_excel(write,sheet_name='df1')
    df.to_excel(write,sheet_name='df2')

