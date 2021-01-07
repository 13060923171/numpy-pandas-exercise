import matplotlib.pyplot as plt
import random
x = range(2,26,2)#x轴的位置
y = [random.randint(15,30) for i in x]
plt.figure(figsize=(20,8),dpi=80)
#设置x轴的刻度
#plt.xticks(X)
#plt.xticks(range(1,25))
#设置y轴的刻度
#plt.yticks(y)
#plt.yticks(range(min(y)),max(y)+1)
#构造x轴刻度标签,for循环读取x轴刻度并控制产生刻度标签的个数，并以相应的格式显示:{}中，放置format(i)括号中的i,也就是取得x
x_ticks_label = ['{}:00'.format(i) for i in x]
#rotation = 45 让字旋转45度
plt.xticks(x,x_ticks_label,rotation=45)
#设置y轴的刻度标签
y_ticks_label = ['{}°C'.format(i) for i in range(min(y),max(y)+1)]
plt.yticks(range(min(y),max(y)+1),y_ticks_label)
#绘图
plt.plot(x,y)
plt.show()