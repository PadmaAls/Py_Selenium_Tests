from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")

time.sleep(5)
driver.maximize_window()

driver.find_element(By.ID,"docsearch-1").click()
time.sleep(3)
element = driver.find_element(By.ID,"docsearch-input")
element.send_keys("java")
time.sleep(3)
innerele = driver.find_element(By.ID,"docsearch-item-3")

innerele.click()

time.sleep(5)
driver.quit()







