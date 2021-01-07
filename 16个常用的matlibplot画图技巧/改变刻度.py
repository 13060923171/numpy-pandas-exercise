import matplotlib.pyplot as plt
import numpy as np


fig=plt.figure()
fig,axe=plt.subplots()
axe.set_xticks([0,1,2,3,4,5])
axe.set_xticklabels(['Taxi','Metro','Walk','Bus','Bicycle','Driving'])
plt.show()