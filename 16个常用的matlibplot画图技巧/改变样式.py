import matplotlib.pyplot as plt
import numpy as np

fig,axe=plt.subplots()
data_m=(40, 60, 120, 180, 20, 200)
index = np.arange(6)
axe.bar(index, data_m)
plt.style.use('dark_background')
plt.show()