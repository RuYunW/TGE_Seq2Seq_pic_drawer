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
l1 = plt.plot(x, y1, 'o:', label="method1")
plt.plot(x, y2, 'v-', label="method2")
plt.plot(x, y3, '^--', label="method3")
plt.plot(x, y4, 'x-.', label="method4")
plt.plot(x, y5, 's-', label="method5", linewidth=3)
plt.legend()
plt.show()
