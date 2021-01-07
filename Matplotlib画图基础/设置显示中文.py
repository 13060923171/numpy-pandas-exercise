from matplotlib import pyplot as plt
import matplotlib
import random
from matplotlib import font_manager

x = range(0,120)
y = [random.randint(10,30)for i in range(120)]
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y)

my_font = font_manager.FontProperties(fname='C:\\Users\\96075\\files\\fonts\\simsun.ttf',size=18)
plt.xlabel('时间',fontproperties=my_font,rotation=45)
plt.ylabel('次数',fontproperties=my_font)
#设置标题
plt.title('每分钟跳动次数',fontproperties=my_font,color = 'red')
plt.show()
