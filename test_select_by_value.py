


#https://vallarasu.in/test/select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


import time

def test_select_by_value_func():

 driver = webdriver.Chrome()
 driver.implicitly_wait(5)
 driver.get("https://vallarasu.in/test/select")


 day_dob = "//select[@id='dob_day']"
 mon_dob = "//select[@id='dob_month']"
 year_dob = "//select[@id='dob_year']"

 day_dob_locator = driver.find_element(By.XPATH,day_dob)
 mon_dob_locator = driver.find_element(By.XPATH,mon_dob)
 year_dob_locator = driver.find_element(By.XPATH,year_dob)


 day_select = Select(day_dob_locator)
 size_of_days = len(day_select.options)

 month_select = Select(mon_dob_locator)
 size_of_months = len(month_select.options)

 day_select.select_by_visible_text("02")
 month_select.select_by_visible_text("03")

 assert size_of_days == 31
 assert size_of_months == 12



test_select_by_value_func()

















