from matplotlib import pyplot as plt
import numpy as np
import xlrd

workbook = xlrd.open_workbook("tables.xlsx")
sheet1 = workbook.sheet_by_index(7)

x1 = ['[0,10]','[10,20]', '[20,30]', '[30,40]', '[0,50]', '[50,100]', '[100,150]', '[150,200]']
x_1 = [10, 20, 30, 40]
x_2 = [55, 75, 65]
x_3 = [45, 65, 85, 95, 105]

# x_1 = np.array(x_1)
# x_2 = np.array(x_2)
# x_3 = np.array(x_3)

data = []

for i in range(15):
    data.append(float(sheet1.cell_value(i+1, 7))/100)

print(data)

data = np.array(data)
plt.title("")
plt.xlabel("Datasets")
plt.ylabel("BLEU")

plt.bar(x_1, data[0:4], width=5, label="HS", )  #NMT ACC
plt.bar(x_2, data[5:8], width=5, label="MTG", )
plt.bar(x_3, data[9:14], width=5, label="E-JDT",)

plt.xticks([index for index in x_1+x_2], x1)
plt.xticks(rotation=-45)    # 设置x轴标签旋转角度
plt.grid(linestyle = '--',linewidth =1, color= 'gray',alpha = 0.4)
plt.legend(framealpha=0.5)
# plt.ylim(0, 1)
# plt.xlim(10, )
plt.savefig("./figure/resultBLEU.png")
plt.show()
