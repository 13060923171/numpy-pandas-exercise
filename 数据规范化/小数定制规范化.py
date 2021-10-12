from sklearn import preprocessing
import numpy as np
#初始化数据，每一行表示一个样本，每一列表示为一个特征
x = np.array([
    [0.,-3.,1.],
    [3.,1.,2.],
    [0.,1.,-1.]
])
#小数定标规范化
j = np.ceil(np.log10(np.max(abs(x))))
scaled_X = x/(10**j)
print(scaled_X)