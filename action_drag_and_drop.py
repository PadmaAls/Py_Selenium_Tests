from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


import time


def test_drag_drop_call():

    # Arrange
    driver = webdriver.Chrome()
    driver.get("https://vallarasu.in/test/drag-drop")

    source_selector = "//span[text() = 'Christina Aguilera']//ancestor::li"
                      
    target_selector = "//ul[@id='selected-items']"

    source_el = driver.find_element(By.XPATH, source_selector)
    target_el = driver.find_element(By.XPATH, target_selector)

    time.sleep(3)

    # Act
    action = ActionChains(driver)
    action.drag_and_drop(source_el,target_el).perform()
    # action.click_and_hold(source_el).move_to_element(target_el).release().perform()

    time.sleep(5)
    driver.quit()

    # Assert


test_drag_drop_call()
