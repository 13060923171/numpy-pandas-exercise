import pandas as pd
import numpy as np
df = pd.DataFrame({'a':[1,3,np.nan],'b':[4,np.nan,np.nan]})

q1 = df['a'].quantile(.25)
q3 = df['a'].quantile(.75)
iqr = q3-q1
toprange = q3 + iqr * 1.5
botrange = q1 - iqr * 1.5

copydf = df
copydf = copydf.drop(copydf[copydf['a']
        > toprange].index)
copydf = copydf.drop(copydf[copydf['a']
        < botrange].index)
print(copydf)