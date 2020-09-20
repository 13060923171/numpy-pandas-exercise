import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,6,7])
#打印一个序列从20200901到20200906
data = pd.date_range('20200901',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=data,columns=["a","b","c","d"])
# print(df)
# print(df.T)
# print(df.sort_index(axis=0,ascending=False))
#
# print(df.sort_values(by='a'))
#打印所有行，标签定义是把a,b两列的所有行打印出来,纯标签筛选
print(df.loc[:,["a","b"]])
#打印第三行，所有列的内容，纯数字筛选
print(df.iloc[3])
print(df.iloc[[1,3,4],1:3])
#打印这个列表里面a列大于0.5的所有行
print(df[df.a >0.5])
#选定A列，其中A列中有大于0的全部定义为1
# df.a[df.a>0]=1
# print(df)
# df["b"] = np.nan
# print(df)
#在一个列表里面添加新的一列，怎么添加一样的保证列正确，就是要对准行即可
df['e'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20200901',periods=6))
print(df)

df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
#当存在有nan的时候，把该行全部移除掉
# print(df.dropna(axis=0,how='any'))
#当检测出存在nan的时候，把nan的值全部换成0
# print(df.fillna(value=0))
#检测这个表是否存在nan，如果存在，那么返回一个true值，这样方便我们用来检测，一般用于数据量很大的表格
print(np.any(df.isnull()) == True)