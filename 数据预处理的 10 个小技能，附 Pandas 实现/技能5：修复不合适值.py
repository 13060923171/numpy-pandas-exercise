import pandas as pd
import numpy as np
df = pd.DataFrame({'a':[1,3,np.nan],'b':[4,np.nan,np.nan]})

df.loc[(df['a'] < -2,'a')] = 0
df.loc[(df['a'] >= 100,'a')] = 100
print(df)