import string
exclude = set(string.punctuation)

def remove_punctuation(x):
    x = ''.join(ch for ch in x if ch not in exclude)
    return x
# # 原df
# Out[26]:
#       a       b
# 0   c,d  edc.rc
# 1     3       3
# 2  d ef       4
#
# # 过滤a列标点
# In [27]: df.a = df.a.apply(remove_punctuation)
# In [28]: df
# Out[28]:
#       a       b
# 0    cd  edc.rc
# 1     3       3
# 2  d ef       4