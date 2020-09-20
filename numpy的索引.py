import numpy as np
a = np.arange(3,15).reshape((3,4))
print(a)
#在一维数组中通过索引，找出这个数组在第4位的数值
#在二维数值中，这样写，就是输出数组的第4行内容
print(a[2])
#这样就是输出第3行，第4位的数值
print(a[2][3])
#把二维数组转化成一维数组
print(a.flatten())
for i in a.flat:
    print(i)