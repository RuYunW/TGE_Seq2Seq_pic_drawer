from matplotlib import pyplot as plt
import numpy as np
import xlrd

workbook = xlrd.open_workbook("tables.xlsx")
sheet1 = workbook.sheet_by_index(6)

list_name = ['Max.in', 'Avg.in', 'Max.out', 'Avg.out']
x = [0.5, 1, 1.5, 2]

x = np.array(x)
data = []
for i in range(6):
    _ = []
    for j in range(3):
        _.append(sheet1.cell_value(i+1, j+1))
    data.append(_)

plt.rcdefaults()
fig, ax = plt.subplots()

ax.set_xlabel('Number')
ax.set_title('')

ax.barh(x, [data[2][0], data[3][0], data[4][0], data[5][0]], height=0.1, align='center', label='HS', color="#0262E0")
ax.barh(x+0.1, [data[2][1], data[3][1], data[4][1], data[5][1]], height=0.1, align='center', label='MTG', color='#069CCF')
ax.barh(x+0.2, [data[2][2], data[3][2], data[4][2], data[5][2]], height=0.1, align='center', label='E-JDT', color='#25DC94')

ax.set_yticks(x+0.1)
ax.set_yticklabels(list_name)
plt.legend()
plt.show()
# plt.title("")
# plt.xlabel("Datasets")
# plt.ylabel("BLEU")
# # plt.bar(x, [data[1][0], data[3][0], data[5][0]], width=0.1, label="NMT", color="#352A86")  #NMT ACC
# # plt.bar(x+0.1, [data[1][1], data[3][1], data[5][1]], width=0.1, label="LPN", color="#0262E0")
# # plt.bar(x+0.2, [data[1][2], data[3][2], data[5][2]], width=0.1, label="SEQ2TREE", color="#1389D2")
# # plt.bar(x+0.3, [data[1][3], data[3][3], data[5][3]], width=0.1, label="SNM", color="#069CCF")
# # plt.bar(x+0.4, [data[1][4], data[3][4], data[5][4]], width=0.1, label="ASN", color="#1CB2AE")
# # plt.bar(x+0.5, [data[1][5], data[3][5], data[5][5]], width=0.1, label="GB-CNN", color="#25DC94")
# # plt.bar(x+0.6, [data[1][6], data[3][6], data[5][6]], width=0.1, label="TGE-Seq2Seq", color="#BCEE5E")
#
# plt.xticks([index + 0.2 for index in x], list_name)
# plt.grid(linestyle = '--',linewidth =1, color= 'gray',alpha = 0.4)
# plt.legend(framealpha=0.5)
# plt.show()