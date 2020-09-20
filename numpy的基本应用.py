import numpy as np
a = np.arange(2,14).reshape((3,4))
print(a)

#计算矩阵最小和最大位数以及平均数,中位数，分别为0和11，因为这个矩阵一
# 个有12位数字，计算机是从0开始的，所以，最小就是0，最大就是11，平均数为7.5
print(np.argmin(a))
print(np.argmax(a))
print(np.mean(a))
print(np.average(a))
print(np.median(a))
#累加函数,前一个数和后一个数相加
print(np.cumsum(a))
#累差
print(np.diff(a))
#排序，从小到大,是逐行排序
print(np.sort(a))
#把矩阵行变成列，列变成行，这个应用范围比较广
print(np.transpose(a))
print(a.T)
#就是说在这个矩阵内，我定义最小值为5，最大值为9，如果不在这个范围内，那么小于5的全部变成5，大于9的全部变成9，符合这个值的保持不变
print(np.clip(a,5,9))

#根据axis来对这个矩阵进行，行或者列的求平均值
print(np.mean(a,axis=1))