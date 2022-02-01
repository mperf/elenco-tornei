from openpyxl import Workbook
import glob
import os
from sys import stdin
 



schools=['Caramuel','Castoldi','Roncalli']



for i in range(3):
    cartella = os.path.dirname(os.path.realpath(__file__))
    myFilesPaths = glob.glob(cartella + '/Elenchi '+schools[i]+'/*.txt')
    print(len(myFilesPaths))
    os.makedirs("results-"+str(schools[i]))
    for j in range(len(myFilesPaths)):

      with open(myFilesPaths[j]) as f:
        lines = f.readlines()
        workbook = Workbook()
        sheet = workbook.active
        sheet.column_dimensions['A'].width = 30
        sheet.column_dimensions['B'].width = 15
        sheet.column_dimensions['C'].width = 20
        sheet.column_dimensions['D'].width = 15
        index=2
        
        sheet["A1"] = "ALUNNI "+str(myFilesPaths[j].split(" ")[2].split('.')[0])
        sheet["B1"] = "BASKET 3 vs 3"
        sheet["C1"] = "PALLAVOLO MISTA"
        sheet["D1"] = "CALCETTO"
        for line in lines:
          value='A'+str(index)
          sheet[value]=line
          index+=1
      
        workbook.save(filename= "results-"+str(schools[i])+"/"+myFilesPaths[j][-8:]+".xlsx")

        