from selenium import webdriver
from selenium.webdriver.common.by import By


import time

def locators_define_and_assert():
    
 driver = webdriver.Chrome()
 driver.implicitly_wait(5)
 driver.get("https://practicetestautomation.com/practice-test-login/")
 
 user_name_loc = "//input[@id='username']"
 pwd_loc = "//input[@id='password']"
 login_loc = "//button[@id='submit']"
 
 locator_username = driver.find_element(By.XPATH,user_name_loc)
 locator_pwd = driver.find_element(By.XPATH,pwd_loc)
 locator_login = driver.find_element(By.XPATH,login_loc)
 
 locator_username.send_keys("student")
 locator_pwd.send_keys("Password123")
 locator_login.click()


#Assert

 
 assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"
 driver.quit()

locators_define_and_assert()
