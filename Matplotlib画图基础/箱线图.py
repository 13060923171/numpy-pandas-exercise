# 数据准备
# ⽣成0-1之间的10*4维度数据(10行，4列的数组)
import numpy as np

data = np.random.normal(size=(10, 4))
lables = ['A', 'B', 'C', 'D']

# ⽤Matplotlib画箱线图
# boxplot(x,labels=None)函数，x代表绘图数据，labels是缺省值，可以为箱线图添加标签。
import matplotlib.pyplot as plt

plt.boxplot(data, labels=lables)  # 注意单词labels和lables
plt.show()

# ⽤Seaborn画箱线图
# boxplot(x=None,y=None,data=None)函数。data为DataFrame类型，x、y是data中的变量。
import seaborn as sns
import pandas as pd

df = pd.DataFrame(data, columns=lables)
sns.boxplot(data=df)
plt.show()
