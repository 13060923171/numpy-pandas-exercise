import numpy as np
a = np.arange(8)

print(a)
#改变数组的形状
b = a.reshape(1,8)
b1 = a.reshape(2,-1)
print(b1.shape)
#C数组横着写
b2 = a.reshape(2,-1,order='C')
#F数组竖着写
b3 = a.reshape(2,-1,order='F')
print(b2)
print(b3)

print("++"*+30)
a = np.arange(9)
#resize是强行转换，多的就删除，少了就填0
b4 = np.resize(a,(3,3))
print(b4)
print(b4.shape)

