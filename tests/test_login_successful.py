import pytest
from selenium.webdriver import Chrome, Keys, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture
def browser():
    driver = Chrome()
    yield driver
    WebDriverWait(driver, 3)
    driver.quit()


def test_successful_login(browser):
    browser.get("https://www.saucedemo.com/")

    username_name = browser.find_element(By.NAME, "user-name")
    password_input = browser.find_element(By.NAME, "password")
    login_button = browser.find_element(By.NAME, "login-button")

    username_name.send_keys("standard_user")
    password_input.send_keys("secret_sauce")

    login_button.click()

