# Explicit Wait
# how a fast a page renders

# wait for the page to load 
# implicit wait - fixed amount of time to wait
# keep wait time, increase time a test takes to complete

# Explicit Wait 

# WebDriverWait
# Different conditions to wait on

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def test_explicit_wait():

    # Arrange
    url = "https://vallarasu.in/test/wait"
    driver = webdriver.Chrome()
    driver.get(url)

    el_locator = "//a[contains(text(),'Certification')]"
    el2_locator = "//a[contains(text(),'Boring Stuff')]"
    el3_locator = "//a[contains(text(),'Python Official')]"

   
    # Act
    wait = WebDriverWait(driver, timeout=60)
    #el = wait.until(EC.visibility_of_element_located((By.XPATH, el_locator)))

    #el2 = wait.until(EC.element_to_be_clickable((By.XPATH, el2_locator)))

    #el3 = wait.until(EC.presence_of_element_located((By.XPATH, el3_locator)))

    # el4 = wait.until(EC.text_to_be_present_in_element((By.XPATH, el_locator), "freeCodeCamp Certification"))    

    # el5 = wait.until(EC.url_contains("wait"))

    # el6 = wait.until(EC.url_to_be("https://vallarasu.in/test/wait"))

    # el7 = wait.until(EC.title_contains("Wait"))

    # el8 = wait.until(EC.title_is("Wait Page"))

    # el9 = wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='test-iframe']")))  

    # el10 = wait.until(EC.alert_is_present())    

    wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loader']")))  


    #<div class='loader'> Loading </div> 

    
    # Assert
    # assert el.text == "freeCodeCamp Certification"
    # el.click()
    # time.sleep(3)
    
    # assert el2.text == "Automate the Boring Stuff with Python"
    # el2.click()
    # time.sleep(3)

    # assert el3.text == "Python Official Tutorial" 
    # el3.click()
    # time.sleep(3)

    driver.find_element(By.XPATH,el_locator).click()
    time.sleep(3)

    driver.quit()

test_explicit_wait()