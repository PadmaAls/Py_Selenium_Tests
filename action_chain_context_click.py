from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


import time

def action_chain_cont_click():
    
 driver = webdriver.Chrome()
 driver.implicitly_wait(5)
 driver.get("https://vallarasu.in/test/action-chain")

 #arrange

 content_loc = "//button[@class='context-menu-one']"

 content_el = driver.find_element(By.XPATH,content_loc)

 copy_loc = "//span[text()='Copy']"


 
 #act
 action = ActionChains(driver)
 action.context_click(content_el).perform()

 time.sleep(3)
 copy_el = driver.find_element(By.XPATH,copy_loc)

 copy_el.click()

 alert = driver.switch_to.alert
 

 actual = alert.text
 expected = "clicked: copy"
  
 time.sleep(3)

 #assert

 if (actual == expected):
    print("Clicked Copy successfully")
  
 driver.quit()

action_chain_cont_click()
