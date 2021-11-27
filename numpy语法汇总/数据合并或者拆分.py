import numpy as np

arr1 = np.array([[2,4],[6,8]])

arr2 = np.array([[3,5],[7,9]])

#合并,axis =0  表示列，1表示行，None表示全部改为一维
res = np.concatenate((arr1,arr2),axis=0)
print(res)

print("+"*+50)

in_arr1 = np.array([1,2,3])
in_arr2 = np.array([4,5,6])

#平行相加
out_arr = np.vstack((in_arr1,in_arr2))
print(out_arr)
#垂直相加
out_arr1 = np.hstack((in_arr1,in_arr2))
print(out_arr1)
print('-'*100)
a = np.arange(9).reshape(3,3)
#纵向切
b = np.hsplit(a,3)
print(b)
#横向切
b1 = np.vsplit(a,3)
print(b1)
print('-'*100)

arr1 = np.array([[1,2],[3,4]])
b = np.insert(arr1,1,23,axis=1)
b = np.insert(arr1,1,[9,9],axis=1)
print(b)

c = np.append(arr1,[[3399,2]],axis=0)
print(c)
print('-'*100)
arr3 = np.array([[1,2],[3,4]])
e = np.delete(arr3,1,axis=1)
print(e)

