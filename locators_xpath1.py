from selenium import webdriver
from selenium.webdriver.common.by import By


import time

def locators_define_and_assert():
    
 driver = webdriver.Chrome()
 driver.implicitly_wait(5)
 driver.get("https://cs101.in/ecom/login.html")

 user_name_loc = "//input [@id='auth-user']"
 pwd_loc = "//input [@id='auth-pass']"
 login_loc = "//button[@id='auth-button']"

 locator_username = driver.find_element(By.XPATH,user_name_loc)
 locator_pwd = driver.find_element(By.XPATH,pwd_loc)
 locator_login = driver.find_element(By.XPATH,login_loc)

 locator_username.send_keys("admin")
 locator_pwd.send_keys("admin")
 locator_login.click()


#Assert

 assert driver.title == "NEO"
 assert driver.current_url == "https://cs101.in/ecom/index.html"
 driver.quit()

locators_define_and_assert()
