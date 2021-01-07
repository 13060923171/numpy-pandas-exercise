from matplotlib import pyplot as plt
import matplotlib
import random
from matplotlib import font_manager

y1 = [random.randint(1,15) for i in range(10)]
y2 = [random.randint(1,15) for i in range(10)]
y3 = [random.randint(1,15) for i in range(10)]

x = range(11,21)
#设置图形
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y1,color='red',label='自己')
plt.plot(x,y2,color='blue',label='老妈')
plt.plot(x,y3,color='green',label='老爸')

#设置x轴刻度
xtick_labels = ['{}岁'.format(i) for i in x]
my_font = font_manager.FontProperties(fname='C:\\Users\\96075\\files\\fonts\\simsun.ttf',size=18)
plt.xticks(x,xtick_labels,fontproperties=my_font,rotation=45)
#绘制网络（网格也是可以设置线的样式）
#alpha=0.4 设置透明度
plt.grid(alpha=0.4)
#添加图例（注意：只有在这里需要添加prop参数是显示中文，其他的都用fontproperties）
#设置位置loc:upper left, lower left, center left, upper center
plt.legend(prop= my_font,loc='upper right')
#展示
plt.show()