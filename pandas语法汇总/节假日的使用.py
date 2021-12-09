import pandas as pd
#导入节假日的相关库
from pandas._libs.tslibs.offsets import CustomBusinessDay
from pandas.tseries.holiday import AbstractHolidayCalendar,nearest_workday,Holiday
# import pandas._libs.tslibs.off
#加载时间序列
df = pd.read_csv('./data/aapl_no_dates.csv')
print(df)

rng = pd.date_range(start='5/1/2017',end='5/21/2017',freq='B')


#定义节假日
class myCalendar(AbstractHolidayCalendar):
    rules = [Holiday('五一',month=5,day=1),]

wuyi = CustomBusinessDay(calendar=myCalendar())

rng1 = pd.date_range(start='5/1/2017',end='5/21/2017',freq=wuyi)
print(rng1)

#埃及的工作日 星期天到星期四
egypt_weekdays = "Sun Mon Tue Wed Thu"
b2 = CustomBusinessDay(weekmask=egypt_weekdays)
rng2 = pd.date_range(start='5/1/2017',end='5/21/2017',freq=b2)
print(rng2)

from datetime import datetime
dt = datetime(2017,7,10)
#b2可以作为时间参数
dt1 = dt +4*b2
print(dt1)

