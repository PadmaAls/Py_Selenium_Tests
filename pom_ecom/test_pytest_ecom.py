from selenium import webdriver
import pytest

from pom_login import LoginPOM

@pytest.fixture
def credentials():
    return "admin", "admin"

@pytest.fixture(scope="session")
def chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver

def test_login_works(credentials, chrome):
    
    # Arrange
    # instance of pom
    login_page = LoginPOM(chrome)

    # Act
    # unpack credentials
    user, password = credentials
    login_page.login(user, password)

    # Assert
    assert login_page.title == "NEO"