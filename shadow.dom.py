from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time


def shadow_dom_element():
    
    # Arrange
    driver = webdriver.Chrome()
    driver.get("https://vallarasu.in/test/shadow-dom.html")

    #host
    host_locator = "//div[@id='dob-container']"
    day_locator = "dob_day"
    month_loc = "dob_month"
    year_loc = "dob_year"

    # 1. find host
    host = driver.find_element(By.XPATH, host_locator)

    # 2. navigate to shadow_root
    shadow_root = host.shadow_root

    # 3. locate element within shadow root
    # NO XPATH
    day = shadow_root.find_element(By.ID, day_locator)
    day_select = Select(day)
    month = shadow_root.find_element(By.ID, month_loc)
    month_select = Select(month)
    year = shadow_root.find_element(By.ID, year_loc)
    year_select = Select(year)  

    time.sleep(5)

    day_select.select_by_index(2)
    #month_select.select_by_value("5")
    #year_select.select_by_visible_text("2023")
    month_select.select_by_index(5)
    year_select.select_by_index(7)
    
    time.sleep(5)
    # Act
    driver.quit()


shadow_dom_element()