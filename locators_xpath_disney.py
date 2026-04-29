from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time

def locators_xpath_find_disney():
    
 driver = webdriver.Chrome()
 driver.implicitly_wait(5)
 driver.get("https://disneyworld.disney.go.com/")



 resorts_loc = "//a[@href='/resorts/' and @class='button button--primary button--large hero-button astro-lvkotgoy' and @data-analytics-link-id='WDW_Module_0_Hero_fastHeroStandard_0_ExploreResortHotels_link']"

 resorts_el = driver.find_element(By.XPATH,resorts_loc)
 resorts_el.click()

 time.sleep(3)
 driver.back()

 gettickets_loc = "//a[@href='/admission/tickets/' and @class='button button--primary button--large hero-button astro-lvkotgoy' and @data-analytics-link-id='WDW_Module_0_Hero_fastHeroStandard_0_GetTickets_link']"

 gettickets_el = driver.find_element(By.XPATH,gettickets_loc)
 gettickets_el.click()
 time.sleep(2)

 driver.back()

 driver.maximize_window()
 time.sleep(3)
 search_loc = "//input[@aria-label='Search or ask a question' and @type = 'search']"

 search_loc_el = driver.find_element(By.XPATH,search_loc)
 search_loc_el.send_keys("test"+ Keys.ENTER)
 
 time.sleep(3)



 
 driver.quit()

locators_xpath_find_disney()
