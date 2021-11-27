import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
#把二维改为一维,flatten不会改变原来的数组
print(a.flatten())

#把二维改为一维，ravel会改变原来的数组
c = a.ravel()
print(c)


