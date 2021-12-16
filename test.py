from openpyxl import Workbook
import glob
import os
from sys import stdin
 



schools=['Caramuel','Castoldi','Roncalli']

workbook = Workbook()
sheet = workbook.active

for i in range(3):
    cartella = os.path.dirname(os.path.realpath(__file__))
    myFilesPaths = glob.glob(cartella + '\Elenchi '+schools[i]+'\*.txt')
    for j in range(len(myFilesPaths)):
      f=open(myFilesPaths[j], 'r')
      index=2
      sheet["A1"] = "ALUNNI"
      sheet["C1"] = "BASKET 3 vs 3"
      sheet["D1"] = "PALLAVOLO MISTA"
      sheet["E1"] = "CALCETTO"
      for line in stdin:
        print(line, end='')
      for line in f:
        try:
          value='A'+str(index)
          sheet[value]=line
        except EOFError:
          break
        index+=1
      workbook.save(filename= myFilesPaths[j][-10:]+".xlsx")

'''
workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "ALUNNI"
sheet["C1"] = "BASKET 3 vs 3"
sheet["D1"] = "PALLAVOLO MISTA"
sheet["E1"] = "CALCETTO"

f = open(".txt", "r")
for x in f:
  print(x)



for i in range(35):
    value='A'+str(i+2)
    print(value)
    sheet[value]=
workbook.save(filename="hello_world.xlsx")
'''