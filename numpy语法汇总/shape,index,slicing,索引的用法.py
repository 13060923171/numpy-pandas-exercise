import numpy as np

arr1 = np.array([[1,2,3,4],[2,4,6,8]])
print(arr1)
#查看形状
print(arr1.shape)

print("="*50)
list1 = [1,2,3,4,5,6,7,8]
list2 = [9,10,11,12,12,13,14,15]
a1 = np.array(list1)
a2 = np.array(list2)
print(a1*a2)

a = np.arange(10,1,-2)
print(a)

print("="*50)
a = np.array([[1,2,3],[4,2,3]])
#逻辑索引
print(a[a<2]*3)
