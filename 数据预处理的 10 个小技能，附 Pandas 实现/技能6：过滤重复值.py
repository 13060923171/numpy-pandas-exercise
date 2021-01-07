import pandas as pd
import numpy as np
df = pd.DataFrame({'a':[1,3,np.nan],'b':[4,np.nan,np.nan]})

df.drop_duplicates(['Names'], keep='last')
print(df)