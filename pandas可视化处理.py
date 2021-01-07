import pandas as pd
#导入pandas可视化库
from pandasgui import show

df = pd.read_excel('mydata.xlsx')
show(df,settings={'block':True})