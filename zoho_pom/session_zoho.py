from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SessionPOM:

    def __init__(self, driver):
        self.driver = driver
        
        self.title = self.driver.title

    def loginsession(self):

      session_loc = "//span[text() = 'Sessions ']"
      active_session_loc = "//span[@id ='useractivesessions']"
      view_more_session_loc = "//div[text() = 'View 3 more sessions']"

      session_el = self.driver.find_element(By.XPATH, session_loc)
        
      active_session_el = self.driver.find_element(By.XPATH, active_session_loc)

      view_more_session_el = self.driver.find_element(By.XPATH, view_more_session_loc)

      session_el.click()
      time.sleep(5)
      active_session_el.click()
      time.sleep(5)
      view_more_session_el.click()
      time.sleep(5)
        

      self.url = self.driver.current_url

        




