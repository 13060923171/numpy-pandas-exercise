import pandas as pd
import numpy as np
df = pd.DataFrame({'a':[1,3,np.nan],'b':[4,np.nan,np.nan]})

# 使用a列平均数填充列的空值，inplace true表示就地填充
df["a"].fillna(df["a"].mean(), inplace=True)
print(df)