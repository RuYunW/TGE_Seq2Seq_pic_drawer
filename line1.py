from matplotlib import pyplot as plt
import numpy as np

list_name = ["HS-50", "HS-100", "HS-200", "HS-200+"]

x = [1, 2, 3, 4]

y1 = [] # NMT


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
