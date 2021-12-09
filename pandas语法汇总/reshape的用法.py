import pandas as pd
import numpy as np
import datetime
import pytz

invoices = pd.read_csv('./data/invoices.csv')
#设置可以展示的行数
pd.set_option('display.max_rows',10)
pd.set_option('display.max_columns',10)

#数据转换
df1 = invoices.head(10).T


df = pd.DataFrame({
    "A":[12,4,5,44,1],
    "B":[5,2,54,44,2],
    "C":[20,16,7,3,8],
    "D":[14,3,17,2,6]

})

df2 = df.melt(id_vars=["A"],value_vars=['B'])
print(df2)
#
df3 = pd.get_dummies(invoices['Type of Meal'])
print(df3)
                    #索引
df4 = invoices.groupby(['Company Id','Type of Meal']).agg({'Meal Price':np.mean})
print(df4)

df5 = pd.DataFrame({
    "A":['John','Body',"Mina"],
    "B":['Masters','Graduate','Graduate'],
    "C":[27,23,21]
})
#3D数据，类似Excel的透视表
print(df5.pivot("A","B",'C'))