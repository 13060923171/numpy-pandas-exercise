import pandas as pd
import numpy as np
import datetime
import pytz

invoices = pd.read_csv('./data/invoices.csv')
print(invoices.head())
#查看每一列的数据类型
print(invoices.info())
#category指的是分类的数据类型，一般用于少数的类别
invoices['Type of Meal'] = invoices['Type of Meal'].astype('category')
invoices['Date'] = invoices['Date'].astype('datetime64[ns]')
invoices['Meal Price'] = invoices['Meal Price'].astype('int')
print(invoices.info())

#查看该列存在多少种数据类型，用于处理脏数据
print(invoices['Meal Price'].apply(lambda x:type(x)).value_counts())
#强行转换数据类型的另一种类型，如果遇到报错直接忽略，当errors='coerce'遇到错误的数据，则会把这个错误数据转换为nan
invoices['Meal Price'] = pd.to_numeric(invoices['Meal Price'],errors='ignore')