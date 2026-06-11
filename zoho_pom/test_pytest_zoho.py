from selenium import webdriver
import pytest
import time

from signin_zoho import SigninPOM
from session_zoho import SessionPOM

@pytest.fixture
def loginname():
    return "padmasrinivasan1983@gmail.com","HelloChennai341@"

@pytest.fixture(scope="session")
def chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver

def test_login_works(loginname, chrome):
    
    # Arrange
    # instance of pom
    signin_page = SigninPOM(chrome)

    # Act
   

    user, password = loginname
    signin_page.login(user, password)
    time.sleep(5)

    # Assert
    assert signin_page.url != "https://crm.zoho.com/crm/org927059263/tab/Home/begin"

def see_active_sessions(chrome):
    session_page = SessionPOM(chrome)
    session_page.loginsession()
    time.sleep(5)

    assert session_page.url == "https://accounts.zoho.com/home#sessions/useractivesessions"