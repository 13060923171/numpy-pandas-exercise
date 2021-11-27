import numpy as np

a = np.array([[1,2,3,4],[4,5,6,7],[8,9,10,11]])
print(a)

#行转列
print(a.transpose())
print(a.T)

a = np.array([[1,2],[3,4],[5,6]])
print(a.shape)
#行转列
print(np.swapaxes(a,0,1))