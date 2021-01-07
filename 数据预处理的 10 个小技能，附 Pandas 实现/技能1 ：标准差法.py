import pandas as pd
import numpy as np
df = pd.DataFrame({'a':[1,3,np.nan],'b':[4,np.nan,np.nan]})

# 异常值平均值上下1.96个标准差区间以外的值
meangrade = df['a'].mean()
stdgrade = df['a'].std()
toprange = meangrade + stdgrade * 1.96
botrange = meangrade - stdgrade * 1.96

# 过滤区间外的值
copydf = df
copydf = copydf.drop(copydf[copydf['a']
        > toprange].index)
copydf = copydf.drop(copydf[copydf['a']
        < botrange].index)
print(copydf)