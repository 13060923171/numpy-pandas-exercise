import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
fig=plt.figure()
fig,axe=plt.subplots()
axe.text(0.5,0.5,'我是文本框',bbox={'facecolor':'cyan','alpha':0.5,'pad':0.7})  #添加文本框
plt.show()