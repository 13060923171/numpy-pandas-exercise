import matplotlib.pyplot as plt

x = range(1,8)
y = [17,17,18,15,11,11,13]
#传入x和y,通过plot画折线图,改变颜色
plt.plot(x,y,color= 'red',alpha = 0.5,linestyle='--',linewidth=3,marker='v')
plt.show()

'''基础属性设置
 color='red' : 折线的颜色
 alpha=0.5 : 折线的透明度(0-1)
 linestyle='--' : 折线的样式
 linewidth=3 : 折线的宽度
 '''
'''线的样式
 - 实线(solid)
 -- 短线(dashed)
 -. 短点相间线(dashdot)
 ：虚点线(dotted)
'''


'''折点样式
‘o’ 圆圈 
 ‘.’ 点
 ‘D’ 菱形 
 ‘s’ 正方形
 ‘h’ 六边形1 
 ‘*’ 星号
 ‘H’ 六边形2 
 ‘d’ 小菱形
 ‘_’ 水平线
 ‘v’ 一角朝下的三角形
 ‘8’ 八边形
 ‘<’ 一角朝左的三角形
 ‘p’ 五边形
 ‘>’ 一角朝右的三角形
 ‘,’ 像素 
 ‘^’ 一角朝上的三角形
 ‘+’ 加号 
 ‘| ‘ 竖线
 ‘None’,’’,’ ‘ 无 
 ‘x’ X
 '''