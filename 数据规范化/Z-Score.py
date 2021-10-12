from sklearn import preprocessing
import numpy as np

#初始化数据，每一行表示一个样本，每一列表示为一个特征
x = np.array([
    [0.,-3.,1.],
    [3.,1.,2.],
    [0.,1.,-1.]
])
scaled_x = preprocessing.scale(x)
print(scaled_x)