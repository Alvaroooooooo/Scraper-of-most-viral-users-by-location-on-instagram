import time

def writeExcel(driver, line, a,b,c,d,e,f,g,h,i, row, page):

    time.sleep(2)

    col = 0

    for i in (a,b,c,d,e,f,g,h,i):
        
        time.sleep(2)
        driver.get(i)
        time.sleep(2)
        user = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').text

        try:
            likes = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/a/span').text
        except:
            
            likes = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/span/span').text
        

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').click()
        time.sleep(2)
        followers = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text
        followings = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text

        page.write(row, col, user)
        page.write(row, col+1, likes)
        page.write(row, col+2, followers)
        page.write(row, col+3, followings)
        row += 1