import matplotlib.pyplot as plt
import numpy as np
fig,axe=plt.subplots()
np.random.seed(100)
x=np.arange(0, 10, 1)
y1=np.random.rand(10)
axe.plot(x, y1, '--o')
plt.show()