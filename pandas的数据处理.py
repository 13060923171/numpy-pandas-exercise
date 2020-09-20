import pandas as pd
import numpy as np
dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['a','b','c','d'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
#这句的意思的首先，在【0,1】,【1,2】的位置出现了NAN的值，我们写这行的目的就是去掉这行如果存在nan的值那么就把这整行给删掉，
#如果把axis改成1的话，那么处理的就是整列的信息
#how的值可以是any或者all，当how的值等于any的时候那么，只有这一行或者列存在有一个nan的值，那么这一整行或者列就要被删掉
#当how的值等于all的时候那么，只有当这行或者列都为nan的时候，那么这一整行或者列就要被删掉
# print(df.dropna(axis=0,how='any'))
#这句话的作用就是当这个列表出现有nan的值的时候，那么这个nan的值就是被替换成VALUE的值，我这里value的值为0,那么我的nan值也被替换成0
print(df.fillna(value=0))
