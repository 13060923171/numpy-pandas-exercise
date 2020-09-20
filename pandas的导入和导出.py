import pandas as pd
import numpy as np
data = pd.read_csv('试验_13.csv')

# #1.怎么合并两个表
# df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
# #这句话的意思就是把这df1,df2,df3的列表给合并在一起，根据axis的值，axis等于0，那么把这个3个列表进行竖向合并，如果axis为1那么就是横向合并
# #ignore_index=True这句话的意思就是把我们的索引值进行一个重新排序，从小到大
# res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
# print(res)

# df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','f','e'])
# #join,['inner','outer']
# #这句话的作用就是把两个不一样的表格合并在一起，如果没有这一行就用nan值来代替，这个就是并
# #如果join的值是inner的话，那么就是只合并它们共同的那一列，可以看出是是交
# res = pd.concat([df1,df2],join='inner',ignore_index=True)
# print(res)

#append
#类似python中列表的添加
# df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
# s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
# res = df1.append(s1,ignore_index=True)
# print(res)

# left = pd.DataFrame({'key':['k0','k1','k2','k3'],
#                      'A':['A0','A1','A2','A3'],
#                      'B':['B0','B1','B2','B3']})
# right = pd.DataFrame({"key":['k0','k1','k2','k3'],
#                       "C":['C0','C1','C2','C3'],
#                       'D':['D0','D1','D2','D3']})
#
# print(left)
# print(right)
# #如何把两个列表里面的数据合并，根据他们的的某一列来进行定位，然后将变个列表存在的数进行合并
# res = pd.merge(left,right,on='key')
# print(res)

# left = pd.DataFrame({'key1':['k0','k0','k1','k2'],
#                     'key2':['k0','k1','k0','k1'],
#                      'A':['A0','A1','A2','A3'],
#                      'B':['B0','B1','B2','B3']})
# right = pd.DataFrame({"key1":['k0','k1','k1','k2'],
#                     'key2':['k0','k0','k0','k0'],
#                       "C":['C0','C1','C2','C3'],
#                       'D':['D0','D1','D2','D3']})
# #当定位两个参数作为定位的时候，找两个参数都有的相同值来进行筛选
# #how = inner,outer,left,right
# #inner,outer操作原理和上面一样，right,left就是根据这两个列表作为参照来进行筛选
# res = pd.merge(left,right,on=['key1','key2'],how='inner')
# print(res)

# df1 = pd.DataFrame({'coll':[0,1],'col_left':['a','b']})
# df2 = pd.DataFrame({'coll':[1,2,2],'col_right':[2,2,2]})
# res = pd.merge(df1,df2,on='coll',how='outer',indicator=True)
# print(res)
#用索引值来进行定位
# left = pd.DataFrame({'key1':['k0','k0','k1','k2'],
#                     'key2':['k0','k1','k0','k1'],
#                      'A':['A0','A1','A2','A3'],
#                      'B':['B0','B1','B2','B3']
#                       },index=['K0','K1','K2','K3'])
# right = pd.DataFrame({"key1":['k0','k1','k1','k2'],
#                     'key2':['k0','k0','k0','k0'],
#                       "C":['C0','C1','C2','C3'],
#                       'D':['D0','D1','D2','D3']},index=['K0','K1','K2','K3'])
#
# res = pd.merge(left,right,left_index=True,right_index=True,how="outer")
# # res = pd.merge(left,right,left_index=True,right_index=True,how="inner")
# print(res)

#当被选取量名相同的时候，采取suffixes这种方式来进行划分
boy = pd.DataFrame({'k':['k0','k1','k2'],'age':[1,2,3]})
girl = pd.DataFrame({'k':['k0','k1','k2'],'age':[4,5,6]})
res = pd.merge(boy,girl,on='k',suffixes=['_boy','_girl'],how='inner')
print(res)