from matplotlib import pyplot as plt
import numpy as np
import xlrd

workbook = xlrd.open_workbook("tables.xlsx")
sheet1 = workbook.sheet_by_index(1)

x1 = ['EJDT-50', 'EJDT-100', 'EJDT-200', 'EJDT-200+']
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
plt.plot(x, [data[24][0], data[27][0], data[30][0], data[33][0]], '*--', label='NMT', linewidth=2, color="#352A86")
plt.plot(x, [data[24][1], data[27][1], data[30][1], data[33][1]], 'v--', label='LPN', linewidth=2, color="#0262E0")
plt.plot(x, [data[24][2], data[27][2], data[30][2], data[33][2]], '^--', label='SEQ2TREE', linewidth=2, color="#1389D2")
plt.plot(x, [data[24][3], data[27][3], data[30][3], data[33][3]], 's--', label='SNM', linewidth=2, color="#06A9C1")
plt.plot(x, [data[24][4], data[27][4], data[30][4], data[33][4]], 'D--', label='ASN', linewidth=2, color="#4DBC91")
plt.plot(x, [data[24][5], data[27][5], data[30][5], data[33][5]], 'x--', label='GB-CNN', linewidth=2, color="#F0B949")
plt.plot(x, [data[24][6], data[27][6], data[30][6], data[33][6]], 'o-', label='TGE-Seq2Seq', linewidth=3, color="#D35230")

plt.xticks([index for index in x], x1)

plt.grid(linestyle = '--',linewidth =1, color= 'gray',alpha = 0.4)
plt.legend(framealpha=0.5, loc='upper right')
plt.savefig('bigLineEJDT_ACC.png')
plt.show()
