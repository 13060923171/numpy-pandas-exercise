import matplotlib.pyplot as plt
import numpy as np

fig,axe=plt.subplots()
data_m=(40, 60, 120, 180, 20, 200)
index = np.arange(6)
width=0.4
axe.barh(index, data_m, width,align='center',alpha=0.8, label='men')
plt.show()