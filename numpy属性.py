import numpy as np
#把一维数组转化成二维数组
# array = np.array([[1,2,3],[4,5,6]])
# #查看它是几维数组
# print('number of dim:',array.ndim)
# #查看它的形状，shape (2, 3)表示他是两行三列的一个二维数组
# print("shape",array.shape)
# #查看它有多少个元素
# print("size:",array.size)

# #定义这个数组的类型
# a = np.array([1,2,3,4],dtype=np.int)
# print(a.dtype)

# #定义一个矩阵全部为0，并且是定义它的行和列
# a = np.zeros((3,3))
# print(a)
# #定义一个矩阵全部为1，并且是定义它的行和列
# b = np.ones((3,3),dtype=np.int16)
# print(b)
# #定义一个矩阵其中它的数值无限接近0，并且是定义它的行和列
# c = np.empty((3,3))
# print(c)
# #定义一个矩阵并且用range生成数列，再对它的shape重新进行定义
# d = np.arange(12).reshape((3,4))
# print(d)
# #生成线段
# f = np.linspace(1,10,5)
# print(f)

# #在两个长度相同的数组，怎么进行加减乘除
# a = np.array([10,20,30,40])
# b = np.arange(4)
# c = a-b
# #cos,tan,都是这样
# d = np.sin(a)
# print(c,d)

#当面对二维矩阵的的时候
a = np.array([[10,20],[30,40]])
b = np.arange(4).reshape(2,2)
#单纯的二维数组相乘
c = a*b
#矩阵之间的乘法
c_dot = np.dot(a,b)
print(c)
# print(c_dot)
#axis =0.代表的是每一列的值，例如np.max(c,axis=0)，这句话的意思就是，我在这个二维数组里面，寻找每一列的最大值
#axis =1,代表的是每一行的值，例如np.sum(c,axis=1),这句话的意思就是，我在这个二维数组里面，求每一行的和
print()
print(np.max(c,axis=0))
print(np.min(c,axis=1))