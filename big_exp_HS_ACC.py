from matplotlib import pyplot as plt
import numpy as np
import xlrd

workbook = xlrd.open_workbook("tables.xlsx")
sheet1 = workbook.sheet_by_index(1)

x1 = ['HS-50', 'HS-100', 'HS-200', 'HS-200+']
x = [1, 2, 3, 4]
x = np.array(x)
data = []
_ = []
for i in range(36):
    for j in range(7):
        _.append(sheet1.cell_value(i+1, j+2))
    data.append(_)
    _ = []

plt.xlabel("Datasets")
plt.ylabel("Accuracy Score (%)")
plt.plot(x, [data[0][0], data[3][0], data[6][0], data[9][0]], '*--', label='NMT', linewidth=2, color="#352A86")
plt.plot(x, [data[0][1], data[3][1], data[6][1], data[9][1]], 'v--', label='LPN', linewidth=2, color="#0262E0")
plt.plot(x, [data[0][2], data[3][2], data[6][2], data[9][2]], '^--', label='SEQ2TREE', linewidth=2, color="#1389D2")
plt.plot(x, [data[0][3], data[3][3], data[6][3], data[9][3]], 's--', label='SNM', linewidth=2, color="#06A9C1")
plt.plot(x, [data[0][4], data[3][4], data[6][4], data[9][4]], 'D--', label='ASN', linewidth=2, color="#4DBC91")
plt.plot(x, [data[0][5], data[3][5], data[6][5], data[9][5]], 'x--', label='GB-CNN', linewidth=2, color="#F0B949")
plt.plot(x, [data[0][6], data[3][6], data[6][6], data[9][6]], 'o-', label='TGE-Seq2Seq', linewidth=3, color="#D35230")

plt.xticks([index for index in x], x1)

plt.grid(linestyle = '--',linewidth =1, color= 'gray',alpha = 0.4)
plt.legend(framealpha=0.5)
plt.savefig('./figure/bigLineHS_ACC.png')
plt.show()
