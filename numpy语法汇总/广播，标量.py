import numpy as np

a = np.array([10,20,30,40])

print(a+2)

b = np.array([[10,20,30,40],[10,20,30,40]])

print(b+2)

print('--'*30)
a = np.array([10,20,30,40])
b = np.arange(1,5)
print(a)
print(b)
print(a+b)

print('--'*30)
#广播形式要么数组的形状相同可以相加，要么是一维数组，否则其他都不可以
a = np.array([[1,2],[3,4],[5,6]])
b = np.array([10,20])
print(a+b)
print('--'*30)

a = np.array([[1],[2],[3]])
b = np.array([10,20,30])
print(a+b)



