import matplotlib.pyplot as plt
import numpy as np

fig,axe=plt.subplots()
data_m=(40, 60, 120, 180, 20, 200)
data_f=(30, 100, 150, 30, 20, 50)
index = np.arange(6)
width=0.4
#bar charts
axe.bar(index, data_m, width, color='c', label='men')
axe.bar(index, data_f, width, color='b', bottom=data_m, label='women')
axe.set_xticks([])
axe.legend()
#table
data=(data_m,data_f)
rows=('male','female')
columns=('Taxi','Metro','Walk','Bus','Bicycle','Driving')
axe.table(cellText=data, rowLabels=rows, colLabels=columns)
plt.show()