# # 生成20个[0,100]的随机整数
# In [30]: a = np.random.randint(1,100,20)
# In [31]: a
# Out[31]:
# array([48, 22, 46, 84, 13, 52, 36, 35, 27, 99, 31, 37, 15, 31,  5, 46, 98,99, 60, 43])
#
# # cut分箱
# In [33]: pd.cut(a, [0,60,75,90,100], labels = ['D', 'C', 'B', 'A'])
# Out[33]:
# [D, D, D, B, D, ..., D, A, A, D, D]
# Length: 20
# Categories (4, object): [D < C < B < A]