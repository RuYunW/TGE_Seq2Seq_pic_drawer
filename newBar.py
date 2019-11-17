from matplotlib import pyplot as plt
import math
import numpy as np
import random

x = np.arange(1, 17)
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

for i in x:
    y1.append(5-math.sqrt(i))
    # y2.append(random.randint(1, 10) * i)
    # y3.append(random.randint(1, 10) * i)
    # y4.append(random.randint(1, 10) * i)
    # y5.append(random.randint(1, 10) * i)


plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.bar(x[0], y1[0], label="method1", width=0.9, color="#352A86")
plt.bar(x[1], y1[1], label="method2", width=0.9, color="#3143B9")
plt.bar(x[2], y1[2], label="method3", width=0.9, color="#0262E0")
plt.bar(x[3], y1[3], label="method4", width=0.9, color="#0C74DC")
plt.bar(x[4], y1[4], label="method5", width=0.9, color="#1389D2")
plt.bar(x[5], y1[5], label="method6", width=0.9, color="#069CCF")
plt.bar(x[6], y1[6], label="method7", width=0.9, color="#06A9C1")
plt.bar(x[7], y1[7], label="method8", width=0.9, color="#1CB2AE")
plt.bar(x[8], y1[8], label="method9", width=0.9, color="#4DBC91")
plt.bar(x[9], y1[9], label="method10", width=0.9, color="#7CBF7B")
plt.bar(x[10], y1[10], label="method11", width=0.9, color="#A5BE6A")
plt.bar(x[11], y1[11], label="method12", width=0.9, color="#C8BB5C")
plt.bar(x[12], y1[12], label="method13", width=0.9, color="#F0B949")
plt.bar(x[13], y1[13], label="method14", width=0.9, color="#FDC832")
plt.bar(x[14], y1[14], label="method15", width=0.9, color="#F5DD21")
plt.bar(x[15], y1[15], label="method16", width=0.9, color="#F8FA0D")
# plt.legend()

plt.grid(linestyle = '--',linewidth =1, color= 'gray',alpha = 0.4)
plt.legend()
plt.show()