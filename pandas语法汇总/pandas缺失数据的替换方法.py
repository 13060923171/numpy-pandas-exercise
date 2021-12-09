import pandas as pd
import numpy as np

df = pd.read_csv('./data/nyc_weather.csv',parse_dates=['EST'])

#单值替换
newdf = df.replace(0,value=np.NAN)
print(newdf)

#替换多个值
newdf1 = df.replace(to_replace=[0,1],value=np.NAN)
print(newdf1)

#替换专门列

newdf2 = df.replace({
    'Events':'0'
},np.nan)
print(newdf2)

#使用map表进行数据替换
newdf3 = df.replace(
    {
        0:np.nan
    }
)
print(newdf3)


#正则替换
newdf4 = df.replace({
    'Events':'[A-Za-z]',
},'',regex=True)
print(newdf4)

#列表替换

df1 = pd.DataFrame({
    'score':['exceptional','average','good','poor']
})
df2 = df1.replace(['exceptional','average','good','poor'],[5,3,4,1])
print(df2)

