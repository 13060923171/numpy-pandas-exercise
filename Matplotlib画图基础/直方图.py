# 数据准备：创建一个一维随机数组
import numpy as np
import random
import pandas as pd

a = np.random.randn(100)
x = pd.Series(a)  # Series是pandas中用来存放一维数组的数据格式

# ⽤Matplotlib画直⽅图；
"""
使用plt.hist(x, bins=10)函数
参数x是一维数组，bins代表小区间的数量，默认是10。
"""

import matplotlib.pyplot as plt

plt.hist(x, bins=10)
plt.show()

# ⽤Seaborn画直⽅图：
'''
使用sns.distplot(x, bins=10, kde=True)函数
参数x是一维数组，bins代表直方图中的小区间数量，kde代表显示核密度估计，默认是True。
核密度估计是通过核函数来估计概率密度的方法。
'''
import seaborn as sns

sns.distplot(x, kde=False)
plt.show()
# 图三显示用核函数估计概率密度
sns.distplot(x, kde=True)
plt.show()