import matplotlib.pyplot as plt
import numpy as np

fig, axe = plt.subplots()
labels = 'Taxi', 'Metro', 'Walk', 'Bus','Bicycle','Drive'
sizes = [10, 30, 5, 25, 5, 25]
explode = (0.1, 0.1, 0.5, 0.1, 0.1, 0.1)   #控制分隔距离
axe.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
axe.axis('equal')
plt.show()