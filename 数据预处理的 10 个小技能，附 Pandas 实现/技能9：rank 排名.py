import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[46, 98,99, 60, 43]})
d = df['a'].rank(ascending=False)
print(d)