# 数据准备，显示各学历人数的比例
nums = [20, 42, 18, 7, 6]
labels = ['High-school', 'Bachelor', 'Master', 'Ph.d', 'Other']

# pie(x, labels=None)函数,x代表绘制饼图的数据，labels是缺省值，可以为饼图添加标签
import matplotlib.pyplot as plt

plt.pie(x=nums, labels=labels, autopct='%1.1f%%')
plt.show()
# autopct:设置圆内的文本 # '1.1f%'指图片上显示的数字格式，表示小数点前后位数# 另外两个%%是format格式的符号plt.show()