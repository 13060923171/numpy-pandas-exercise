import numpy as np

#生成对角线矩阵
b = np.eye(2)
print(b)
b1 = np.eye(3,dtype=int)
print(b1)

#不完整矩阵
b2 = np.eye(4,5,dtype=int)
print(b2)

#k决定对角线倾斜度
b3 = np.eye(5,5,dtype=int,k=2)
print(b3)


print("="*50)
#线性分割,retstep告诉你怎么切分
a = np.linspace(2.0,3.0,num=15,retstep=True)
print(a)
print("="*50)
import pylab as p
x1 = np.linspace(0,2,10)
y1 = np.linspace(5,9,10)
print(x1)
print(y1)
p.plot(x1,y1,'*')
# p.show()

print("="*50)
#随机生成一维数组
b = np.random.rand(5)
print(b)
#随机生成二维数组
b1 = np.random.randn(3,4)
print(b1)
#随机生成三维数组
b2 = np.random.randn(2,2,2)
print(b2)
