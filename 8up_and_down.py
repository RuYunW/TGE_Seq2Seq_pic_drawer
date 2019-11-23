from matplotlib import pyplot as plt
import numpy as np
import xlrd

workbook = xlrd.open_workbook("tables.xlsx")
sheet1 = workbook.sheet_by_index(8)

x1 = ['[0,10]', '[10,20]', '[20,30]', '[30,40]', '[40,50]', '[50,60]', '[60,70]', '[70,80]', '[80,90]', '[90,100]']

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = np.array(x)
data = []
_ = []
for i in range(10):
    for j in range(7):
        _.append(sheet1.cell_value(i+1, j+1))
    data.append(_)
    _ = []


data = np.array(data)


plt.xlabel("Subdivided Datasets")
plt.ylabel("BLEU Score (%)")
plt.plot(x, data[:, 0], '*--', label='NMT', linewidth=2, color="#352A86")
plt.plot(x, data[:, 1], 'v--', label='LPN', linewidth=2, color="#0262E0")
plt.plot(x, data[:, 2], '^--', label='SEQ2TREE', linewidth=2, color="#1389D2")
plt.plot(x, data[:, 3], 's--', label='SNM', linewidth=2, color="#06A9C1")
plt.plot(x, data[:, 4], 'D--', label='ASN', linewidth=2, color="#4DBC91")
plt.plot(x, data[:, 5], 'x--', label='GB-CNN', linewidth=2, color="#F0B949")
plt.plot(x, data[:, 6], 'o-', label='TGE-Seq2Seq', linewidth=3, color="#D35230")

plt.xticks([index for index in x], x1)
# plt.ylim(5, 20)
plt.grid(linestyle = '--',linewidth =1, color= 'gray',alpha = 0.4)
plt.legend(framealpha=0.5, loc='upper right')
plt.xticks(rotation=45)    # 设置x轴标签旋转角度
plt.savefig('./figure/up_and_down.png')
plt.show()
