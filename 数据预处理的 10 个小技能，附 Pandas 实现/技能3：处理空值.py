import pandas as pd
import numpy as np
df = pd.DataFrame({'a':[1,3,np.nan],'b':[4,np.nan,np.nan]})
# axis 0 表示按照行，all 此行所有值都为 nan
df.dropna(axis=0, how='all')
print(df)