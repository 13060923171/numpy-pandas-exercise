import numpy as np

#zeros的用法
#生成0
print(np.zeros(5))
print(np.zeros(5,dtype=int))
#打印多维数组
print(np.zeros([2,3]))

#生成1
print('+++'*30)
print(np.ones(2))
print(np.ones(2,dtype=int))
print(np.ones([2,3]))

#随机生成数据
print('+++'*30)
print(np.empty(4))
print(np.empty(2,dtype=int))
print(np.empty([4,5]))