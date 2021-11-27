import numpy as np

#最简单的创建array
arr = np.array([1,2,3,4,5,6])
#调入参数生成array
list1 = [1,2,3,4,5,6]
arr1 = np.array(list1)
#数组转列表
list2 = list(arr1)
print(arr)
print(type(arr))

#演示多维数组
#0维数组
arr2 = np.array(43)
print(arr2)
#1维数组
arr3 = np.array([1,2,3,4,5,6])
print(arr3)
#2维数组
arr4 = np.array([[1,2,3,4,5,6],[11,12,13,14,15,16]])
print(arr4)

#3维数组
arr5 = np.array([[[1,2,3,4,5,6],[11,12,13,14,15,16]],[[1,2,3,4,5,6],[11,12,13,14,15,16]]])
print(arr5)

#怎么查看是几维数组
print(arr5.ndim)

#去创建更高的维度数组
arr6 = np.array([1,2,3,4,5],ndmin=5)
print(arr6)
print(arr6.ndim)

#创建数组指定数据类型
arr7 = np.array([1,2,3,4,5],dtype=np.float)
print(arr7)