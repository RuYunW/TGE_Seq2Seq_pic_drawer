from matplotlib import pyplot as plt
import numpy as np
import xlrd

workbook = xlrd.open_workbook("tables.xlsx")
sheet1 = workbook.sheet_by_index(1)

x1 = ['MTG-50', 'MTG-100', 'MTG-200', 'MTG-200+']
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
plt.plot(x, [data[12][0], data[15][0], data[18][0], data[21][0]], '*--', label='NMT', linewidth=2, color="#352A86")
plt.plot(x, [data[12][1], data[15][1], data[18][1], data[21][1]], 'v--', label='LPN', linewidth=2, color="#0262E0")
plt.plot(x, [data[12][2], data[15][2], data[18][2], data[21][2]], '^--', label='SEQ2TREE', linewidth=2, color="#1389D2")
plt.plot(x, [data[12][3], data[15][3], data[18][3], data[21][3]], 's--', label='SNM', linewidth=2, color="#06A9C1")
plt.plot(x, [data[12][4], data[15][4], data[18][4], data[21][4]], 'D--', label='ASN', linewidth=2, color="#4DBC91")
plt.plot(x, [data[12][5], data[15][5], data[18][5], data[21][5]], 'x--', label='GB-CNN', linewidth=2, color="#F0B949")
plt.plot(x, [data[12][6], data[15][6], data[18][6], data[21][6]], 'o-', label='TGE-Seq2Seq', linewidth=3, color="#D35230")

plt.xticks([index for index in x], x1)

plt.grid(linestyle = '--',linewidth =1, color= 'gray',alpha = 0.4)
plt.legend(framealpha=0.5)
plt.savefig('./figure/bigLineMTG_ACC.png')
plt.show()

