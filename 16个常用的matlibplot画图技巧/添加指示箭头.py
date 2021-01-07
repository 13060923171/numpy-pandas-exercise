import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['axes.unicode_minus'] = True
fig=plt.figure()
fig,axe=plt.subplots()
t=np.arange(0.0,2.0,0.01)
s=np.sin(2*np.pi*t)
axe.plot(t,s,linestyle='-',label='line1')
axe.annotate('我是正弦函数',xy=(1.25,1),xytext=(1.9,1),
                  arrowprops=dict(facecolor='red',shrink=0.2),
                 horizontalalignment='center',verticalalignment='center')
plt.show()