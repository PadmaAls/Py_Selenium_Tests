#https://vallarasu.in/test/iframe

from selenium import webdriver
from selenium.webdriver.common.by import By



import time

def test_iframe_func():

 driver = webdriver.Chrome()
 driver.implicitly_wait(5)
 driver.get("https://vallarasu.in/test/iframe")


 #//input[data-testid='name-input']
 iframe1 = driver.find_element(By.XPATH,"//iframe[@data-test-id='iframe-form-container']")
 

 driver.switch_to.frame(iframe1)

 name_el = driver.find_element(By.XPATH,"//input[@data-testid='name-input']")

 
 name_el.send_keys("Padma Sri")

 time.sleep(2)

 driver.switch_to.default_content()

 assert driver.title == "iFrame Form Fields Automation Testing"

 
 driver.quit()

test_iframe_func()