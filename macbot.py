import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


def getNamesList():
    classe = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/form/table/thead/tr[2]/td[2]/p[2]/span").text
    f = open("Nomi" + classe + ".txt", 'w')
    n_alunni = driver.find_elements(By.XPATH, "/html/body/div[4]/div[1]/form/table/tbody/*")
    for i in range(len(n_alunni)-2):
        print(driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/form/table/tbody/tr[" + str(i+2) + "]/td[4]").get_attribute("aria-label").split("Giustifica ")[1])
        f.write(driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/form/table/tbody/tr[" + str(i+2) + "]/td[4]").get_attribute("aria-label").split("Giustifica ")[1] + "\n")

cartella = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(executable_path=cartella + '\chromedriver')
while(True):
    time.sleep(2)
    print("Procedere? (Y/n)")
    ans = input()
    if(ans=='Y' or ans=='y'):
        print("...\nATTENDERE\n...")
        driver.get(cartella + "\index.html")
        getNamesList()
    else:
        print("Terminare? (Y/n)")
        ans = input()
        if(ans=='Y' or ans=='y'):
            break