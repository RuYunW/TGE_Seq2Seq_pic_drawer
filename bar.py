from matplotlib import pyplot as plt

import numpy as np
import random

x = np.arange(1, 11)
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

for i in x:
    y1.append(random.randint(1, 10) * i)
    y2.append(random.randint(1, 10) * i)
    y3.append(random.randint(1, 10) * i)
    y4.append(random.randint(1, 10) * i)
    y5.append(random.randint(1, 10) * i)


plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.bar(x, y1, label="method1", width=0.2)
plt.bar(x+0.2, y2, label="method2", width=0.2)
plt.bar(x+0.4, y3, label="method3", width=0.2)
plt.bar(x+0.6, y4, label="method4", width=0.2)
# plt.bar(x+0.8, y5, label="method5", width=0.2)
plt.legend()
plt.show()