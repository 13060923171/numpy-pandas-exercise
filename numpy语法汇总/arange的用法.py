import numpy as np
#最基础的用法
print(np.arange(1,10,3))

#指定数据类型
x = np.arange(5,dtype=np.float)
print(x.dtype)
#查看占用大小
print(x.itemsize)

#np和其他函数的使用
y = np.arange(-1,1.1,0.5)
print(y)
print(np.abs(y))