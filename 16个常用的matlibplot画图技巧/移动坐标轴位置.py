import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
fig,axe=plt.subplots()
axe.spines['right'].set_color('none')
axe.spines['top'].set_color('none')
axe.spines['bottom'].set_position(('data',1))
axe.spines['left'].set_position(('data',1))
plt.show()