import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(-10,11,1)
# y = x**2
# plt.plot(x,y)
# plt.show()

x = np.arange(-10,11,1)
y = x**2
plt.plot(x,y)
#调x轴的左右两边
#plt.xlim([-5,5])
#只调一边
#plt.xlim(xmin=-4)
#plt.xlim(xmax=4)
#这里我们只保留x为正的部分
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()