import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
import seaborn as sns

#初始化参数
sns.set()
# uniform_data = np.random.rand(3,3)
# # #设置热力图区间
# # heatmap = sns.heatmap(uniform_data,vmin=0.2,vmax=0.5)
# heatmap = sns.heatmap(uniform_data,center=0)
# plt.show()

flights = sns.load_dataset('flights')
#取出这三个属性图画热力图，坐标点的位置是passengers
flights = flights.pivot('month','year','passengers')
ax = sns.heatmap(flights)
plt.show()

# #将实际的数值绘制到上面
# flights = sns.load_dataset('flights')
# #取出这三个属性画热力图，坐标点的位置是passengers
# flights = flights.pivot('month','year','passengers')
# ax = sns.heatmap(flights,linewidths=0.5,cmap='YlGnBu',cbar=False)
# plt.show()