from matplotlib import pyplot as plt
import numpy as np
import xlrd

workbook = xlrd.open_workbook("tables.xlsx")
sheet1 = workbook.sheet_by_index(7)

x1 = ['...', '[10,20]', '[20,30]', '[30,40]', '[0,50]', '[50,100]', '[100,150]', '[150,200]','[200,500]','[500+]']
x_1 = [10, 20, 30, 40]
x_2 = [48.5, 58.5, 68.5]
x_3 = [51.5, 61.5, 71.5, 80, 90, 100]
x_0 = [15, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x_1 = np.array(x_1)
x_2 = np.array(x_2)
x_3 = np.array(x_3)

data = []

for i in range(16):
    data.append(float(sheet1.cell_value(i+1, 7))/100)

print(data)

data = np.array(data)
plt.title("")
plt.xlabel("Description Length")
plt.ylabel("BLEU Score (%)")

plt.bar(x_1-5, data[0:4], width=3, label="HS", color='#db3934' )  #NMT ACC
plt.bar(x_2-5, data[5:8], width=3, label="MTG", color='#ffc758' )
plt.bar(x_3-5, data[9:15], width=3, label="E-JDT", color='#094b63')

plt.xticks([index-5 for index in x_0], x1)
plt.xticks(rotation=45)    # 设置x轴标签旋转角度
plt.grid(linestyle='--', linewidth=1, color='gray', alpha=0.4)
plt.legend(framealpha=0.5)
# plt.ylim(0, 1)
plt.xlim(8, )
plt.savefig("./figure/des_length_BLEU.png")
plt.show()
