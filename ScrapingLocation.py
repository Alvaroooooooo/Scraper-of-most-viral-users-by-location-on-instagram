import time
from WriteExcel import *


def scrapingLocation(driver, line, page, row):
    
    time.sleep(2)
    
    driver.get(line)

    time.sleep(2)

    a = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[1]/div[1]/a').get_attribute('href')
    b = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[1]/div[2]/a').get_attribute('href')
    c = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[1]/div[3]/a').get_attribute('href')
    d = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/div[1]/a').get_attribute('href')
    e = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/div[2]/a').get_attribute('href')
    f = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/div[3]/a').get_attribute('href')
    g = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[3]/div[1]/a').get_attribute('href')
    h = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[3]/div[2]/a').get_attribute('href')
    i = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[3]/div[3]/a').get_attribute('href')

    writeExcel(driver, line, a,b,c,d,e,f,g,h,i, row, page)

    