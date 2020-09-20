import numpy as np
a = np.arange(12).reshape((3,4))
print(a)
#对numpy进行分割，
print(np.split(a,3,axis=0))
#纵向分割
print(np.vsplit(a,3))
#横向分割
print(np.hsplit(a,2))