# 方法add_subplot：给figure新增子图

# 这里引进的科学计算库Numpy,把它看作一个[列表]即可，目的是要使用log方法画log对数函数。
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 100)  # 与range（）相同
# 新建figure画布对象，三个坐标轴（子图）建立在同一个画布上
fig = plt.figure(figsize=(20, 10), dpi=80)

# 利用画布对象，在上面放置三个坐标系
# 新建子图1
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x, x)
# 新建子图2
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x, x ** 2)  # x的二次方，如果是x**3是x的三次方
ax2.grid(color='r', linestyle='--', linewidth=1, alpha=0.3)
# 新建子图3
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(x, np.log(x))
plt.show()