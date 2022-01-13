from selenium import webdriver
import pathlib

from LogIn import *
from CreateExcel import *

path=str(pathlib.Path(__file__).parent.absolute())
driver = webdriver.Chrome(path+'/chromedriver')

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
