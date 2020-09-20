import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#怎么生成数据可视化，
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data = pd.DataFrame(np.random.rand(1000,4),
                    index=np.arange(1000),columns=list('abcd'))
#累加
# data = data.cumsum()
#生成折线图，因为是有4列数据，所以生成4条折线图
# data.plot()
# plt.show()
ax = data.plot.scatter(x='a',y='b',color='DarkBlue',label="Class 1")
data.plot.scatter(x="a",y="c",color="Darkgreen",label="Class 2",ax=ax)
plt.show()