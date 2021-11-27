import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[10,20],[30,40]])
print(a*b)
print(a+b)
a1 = np.matrix("1 2; 3 4")
b1 = np.matrix("10 20; 30 40")
print(a1)
print(type(a1))
print(a1+b1)
#matrix的乘法不同于array的乘法，matrix的乘法是点乘法
print(a1*b1)

print('*'*100)

a = np.matrix('1 2;3 4')
print(a)
#线性代数，反向矩阵
b = np.linalg.inv(a)
print(b)
#矩阵
print(a * b)

print("+"*50)

a = np.array([[1,2],[3,4]])
b = np.linalg.matrix_power(a,2)
print(b)

print(a.dot(a))

b = np.linalg.matrix_power(a,-1)
print(b)

print(a.dot(b))
print("-"*50)

#解方程
c = np.array([[3,1],[1,2]])
d = np.array([9,8])
e = np.linalg.solve(c,d)
print(e)


print('*'*100)
#求面积
a = np.array([[0,4],[4,0]])
print(np.linalg.det(a))

a = np.array([[0,0,4],[0,4,0],[4,0,0]])
print(np.linalg.det(a))