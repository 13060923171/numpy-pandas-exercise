
import pandas as pd
import numpy as np
df = pd.read_excel('mydata.xlsx')

#去除重复行
df.drop_duplicates()
#改变数据类型
df['name'].astype('str')
df['name'].astype(np.int64)


#怎么删除左右两边的空格
df['chinese'] = df['chinese'].map(str.strip)
#怎么删除左两边的空格
df['chinese'] = df['chinese'].map(str.lstrip)
#怎么删除右两边的空格
df['chinese'] = df['chinese'].map(str.rstrip)

#去掉特殊符号
df['chinese'] = df['chinese'].str.strip('$')

#大小写转化
#全部大写
df.columns = df.columns.str.upper()
#全部大写
df.columns = df.columns.str.lower()
#首字母大写
df.columns = df.columns.str.title()

#对某一行进行大写转化
df['name'] = df['name'].apply(str.upper)

#比如要使用某个函数
def double_df(x):
    return 2*x
df['chinese'] = df['chinese'].apply(double_df)

#当较为复杂的函数要怎么处理
def plus(df,n,m):
    df['new'] = (df[u'语法']+df[u'数学']) *m
    df['new'] = (df[u'语法']+df[u'数学']) *n
    return df
df = df.apply(plus,axis=1,args=(2,3,))