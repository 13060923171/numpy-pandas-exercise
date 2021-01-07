from matplotlib import pyplot as plt
import random

x = range(2, 20, 2)  # x轴的位置
y = [random.randint(15, 30) for i in x]
# 设置图片的大小
'''
figsize:指定figure的宽和高，单位为英寸；
dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80 1英寸等于2.5cm,A4纸是 21*30cm的纸张
'''
# 设置画布对象
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)  # 传入x和y, 通过plot画图
# 保存(注意：要放在show的上面，plt.show()会释放figure资源，如果在显示图像之后保存图片将只能保存空图片。)
plt.savefig('t1.png')
# ./表示放在当前python文件的目录
plt.show()
# 图片的格式也可以保存为svg这种矢量图格式，这种矢量图放在网页中放大后不会有锯齿
# plt.savefig('./t1.svg')