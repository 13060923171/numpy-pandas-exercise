import numpy as np
a = np.array([1,1,1])
b = np.array([2,2,2])
#合并两个一维数列,上下合并
print(np.vstack((a,b)))
#合并两个一维数列,左右合并
print(np.hstack((a,b)))
#在纵向加了个维度，把一行，变成多行一列
print(a[:,np.newaxis])
#在横向加了个维度，把一维数组，变成一行多列的数组
print(a[np.newaxis,:])
#可以合并多个数组，并且定义他的横纵向
print(np.concatenate((a,b,a,b),axis=0))