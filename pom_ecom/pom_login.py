from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPOM:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://vallarasus.github.io/e-com/login.html")
        self.title = self.driver.title

    def login(self, user, password):

        user_locator = "//input[@data-testid='auth-user']"
        password_locator = "//input[@data-testid='auth-pass']"
        login_button_locator = "//button[@id='auth-button']"

        user_el = self.driver.find_element(By.XPATH, user_locator)
        pass_el = self.driver.find_element(By.XPATH, password_locator)
        login_el = self.driver.find_element(By.XPATH, login_button_locator)

        user_el.send_keys(user)
        pass_el.send_keys(password)

        login_el.click()

        self.title = self.driver.title


