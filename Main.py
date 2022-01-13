from selenium import webdriver
import pathlib

from LogIn import *
from CreateExcel import *

path=str(pathlib.Path(__file__).parent.absolute())

try:
    driver = webdriver.Chrome(path+'/chromedriver')
except:
    driver = webdriver.Chrome(path+'/chromedriver.exe')

logIn(driver)
createExcel(driver)

driver.quit()

print("")
print("")
print("")
print("[PROCESO FINALIZADO CON EXITO]")
print("")
print("")
print("")
