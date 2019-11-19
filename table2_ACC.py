from matplotlib import pyplot as plt
import numpy as np
import xlrd

workbook = xlrd.open_workbook("tables.xlsx")
sheet1 = workbook.sheet_by_index(2)

x1 = ['HS', 'MTG', 'E-JDT']
x = [1, 2, 3]

x = np.array(x)
data = []
for i in range(6):
    _ = []
    for j in range(7):
        _.append(float(sheet1.cell_value(i+1, j+2)/100))
    data.append(_)

plt.title("")
plt.xlabel("Datasets")
plt.ylabel("Accuracy")
plt.bar(x, [data[0][0], data[2][0], data[4][0]], width=0.1, label="NMT", color="#352A86")  #NMT ACC
plt.bar(x+0.1, [data[0][1], data[2][1], data[4][1]], width=0.1, label="LPN", color="#0262E0")
plt.bar(x+0.2, [data[0][2], data[2][2], data[4][2]], width=0.1, label="SEQ2TREE", color="#1389D2")
plt.bar(x+0.3, [data[0][3], data[2][3], data[4][3]], width=0.1, label="SNM", color="#069CCF")
plt.bar(x+0.4, [data[0][4], data[2][4], data[4][4]], width=0.1, label="ASN", color="#1CB2AE")
plt.bar(x+0.5, [data[0][5], data[2][5], data[4][5]], width=0.1, label="GB-CNN", color="#25DC94")
plt.bar(x+0.6, [data[0][6], data[2][6], data[4][6]], width=0.1, label="TGE-Seq2Seq", color="#BCEE5E")

plt.xticks([index + 0.2 for index in x], x1)
plt.grid(linestyle = '--',linewidth =1, color= 'gray',alpha = 0.4)
plt.legend()
plt.savefig("./figure/resultACC.png")
plt.show()
