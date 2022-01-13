from datetime import datetime
import xlsxwriter
import time
import os

from ScrapingLocation import *
    
def createExcel(driver):    
    
    name = (str(datetime.today()))[0:-7]

    path = os.getcwd()+name
    file = xlsxwriter.Workbook(path+'.xlsx')
    page = file.add_worksheet()

    time.sleep(2)
    locations = open("LOCATIONS.txt", "r")

    row = 0

    for line in locations:
    
        scrapingLocation(driver, line,page,row)
        row+=9

    file.close()
