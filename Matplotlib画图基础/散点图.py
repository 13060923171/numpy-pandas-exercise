import numpy as np
import matplotlib.pyplot as plt
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
# plt.scatter(x,y,marker='o')
# plt.show()

#seabron画图
import seaborn as sns
import pandas as pd

df = pd.DataFrame({'x':x,'y':y})
sns.jointplot(x='x',y='y',data=df,kind='scatter')
plt.show()