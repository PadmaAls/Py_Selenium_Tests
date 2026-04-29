#https://vallarasu.in/test/form

from selenium import webdriver
from selenium.webdriver.common.by import By


import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://vallarasu.in/test/form")

user_name_loc = "//input[@id='name-input']"
email_loc = "//input[@id='email-input']"
phone_loc = "//input[@id='phone-input']"
location_loc = "//input[@id='location-input']"
grad_loc = "//input[@id='graduation-input']"
year_of_study_loc = "//select[@id='graduation-select']"
male_fem = "//input[@id='female-radio']"
reg_now = "//button[@id='register-button']"

locator_username = driver.find_element(By.XPATH,user_name_loc)
locator_email_loc = driver.find_element(By.XPATH,email_loc)
locator_phone_loc = driver.find_element(By.XPATH,phone_loc)
locator_location_loc = driver.find_element(By.XPATH,location_loc)
locator_grad_loc = driver.find_element(By.XPATH,grad_loc)
locator_yos = driver.find_element(By.XPATH,year_of_study_loc)
locator_male_fem = driver.find_element(By.XPATH,male_fem)
locator_reg_now = driver.find_element(By.XPATH,reg_now)

locator_username.send_keys("Padma Sri")
locator_email_loc.send_keys("Padma123@test.com")
locator_phone_loc.send_keys("123 456 4567")
locator_location_loc.send_keys("Chicago")
locator_grad_loc.send_keys("BE CSE")
time.sleep(5)
locator_yos.send_keys("2026")
time.sleep(5)
locator_male_fem.click()
time.sleep(5)
locator_reg_now.click()
time.sleep(5)

driver.quit()



#//input[@id='female-radio']

#//input[@id="graduation-select"]

#//*[@id="register-button"]










