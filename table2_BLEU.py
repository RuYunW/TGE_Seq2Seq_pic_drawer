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
        _.append(float(sheet1.cell_value(i+1, j+2))/100)
    data.append(_)

plt.title("")
plt.xlabel("Datasets")
plt.ylabel("BLEU-4 Score (%)")

plt.bar(x, [data[1][0], data[3][0], data[5][0]], width=0.1, label="NMT", color="#352A86")  #NMT ACC
plt.bar(x+0.1, [data[1][1], data[3][1], data[5][1]], width=0.1, label="LPN", color="#0262E0")
plt.bar(x+0.2, [data[1][2], data[3][2], data[5][2]], width=0.1, label="SEQ2TREE", color="#1389D2")
plt.bar(x+0.3, [data[1][3], data[3][3], data[5][3]], width=0.1, label="SNM", color="#069CCF")
plt.bar(x+0.4, [data[1][4], data[3][4], data[5][4]], width=0.1, label="ASN", color="#1CB2AE")
plt.bar(x+0.5, [data[1][5], data[3][5], data[5][5]], width=0.1, label="GB-CNN", color="#25DC94")
plt.bar(x+0.6, [data[1][6], data[3][6], data[5][6]], width=0.1, label="TGE-Seq2Seq", color="#BCEE5E")

plt.xticks([index + 0.2 for index in x], x1)
plt.grid(linestyle = '--',linewidth =1, color= 'gray',alpha = 0.4)
plt.legend(framealpha=0.5)
plt.ylim(0, 0.31)
plt.savefig("./figure/resultBLEU.png")
plt.show()
