import pandas as pd
import sqlalchemy
#连接数据库
engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/demo1')
#读取数据表
df = pd.read_sql_table('customers',engine)
print(df)

#怎么使用数据库语句去调用python代码
query = '''
select cust_name from customers WHERE cust_name = 'Wascals'
'''
df2 = pd.read_sql_query(query,engine)
print(df2)

#怎么保存数据到数据库里面
df.to_sql(name='customers',con=engine,if_exists='append',index=False)