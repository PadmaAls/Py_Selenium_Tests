from selenium import webdriver
from selenium.webdriver.common.by import By

class SigninPOM:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://accounts.zoho.com/signin")
        self.title = self.driver.title

    def login(self, user, password):

        
        login_id_locator = "//input[@id='login_id']"
        
        login_button_locator = "//button[@id='nextbtn']"

        password_loc = "//input[@id = 'password']"

        

       

        login_el = self.driver.find_element(By.XPATH, login_id_locator)
        
        login_button_el = self.driver.find_element(By.XPATH, login_button_locator)

        password_el = self.driver.find_element(By.XPATH, password_loc)

        signin_button_el = self.driver.find_element(By.XPATH, login_button_locator)

        login_el.clear()
        login_el.send_keys(user)
        

        login_button_el.click()

        password_el.send_keys(password)

        signin_button_el.click()

        self.url = self.driver.current_url

        




