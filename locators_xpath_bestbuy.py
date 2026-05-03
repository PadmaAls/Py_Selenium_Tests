from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time

def locators_xpath_find_bestbuy():
    
 driver = webdriver.Chrome()
 driver.implicitly_wait(5)
 driver.get("https://www.bestbuy.com/site/misc/deal-of-the-day/pcmcat248000050016.c?id=pcmcat248000050016")

 driver.maximize_window()

 email_loc = "//form[@id='marketingCommunicationId-e9f43e57-bd5b-4a1a-8483-0a93a74b409a']//input[@id='input-e9f43e57-bd5b-4a1a-8483-0a93a74b409a']"

 email_el = driver.find_element(By.XPATH,email_loc)


 
 signup_loc = "//form[@id='marketingCommunicationId-e9f43e57-bd5b-4a1a-8483-0a93a74b409a']//input[@title='Sign up']"

 signup_el = driver.find_element(By.XPATH,signup_loc)
 print(signup_el.get_property("title"))
 time.sleep(2)
 #signup_el.send_keys(Keys.ENTER)
 email_el.send_keys("testgmailid@gmail.com")
 time.sleep(1)
 signup_el.click()
  
 time.sleep(3)
  
 driver.quit()

locators_xpath_find_bestbuy()
