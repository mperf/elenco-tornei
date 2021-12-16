import time
import os
import glob
from selenium import webdriver
from selenium.webdriver.common.by import By

def getNamesList():
    classe = driver.find_element(By.XPATH, "/html/body/div/table[2]/thead/tr[2]/td[2]/p[2]/span").text
    f = open("Nomi" + classe + ".txt", 'w')
    n_alunni = driver.find_elements(By.XPATH, "/html/body/div/table[2]/tbody/*")
    for i in range(3,len(n_alunni)):
        try:
            print(driver.find_element(By.XPATH, "/html/body/div/table[2]/tbody/tr["+str(i)+"]/td[4]/p[1]/span").text)
            f.write(driver.find_element(By.XPATH, "/html/body/div/table[2]/tbody/tr["+str(i)+"]/td[4]/p[1]/span").text + "\n")
        except:
            print("OPS " + classe)

cartella = os.path.dirname(os.path.realpath(__file__))
myFilesPaths = glob.glob(cartella + '\Castoldi\*.html')
print(myFilesPaths)
driver = webdriver.Chrome(executable_path=cartella + '\chromedriver.exe')
for i in range(len(myFilesPaths)):
    time.sleep(2)
    print("...\nATTENDERE\n...")
    driver.get(myFilesPaths[i])
    getNamesList()

