import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = Chrome()
    yield driver
    driver.quit()


def test_successful_login(browser):
    browser.get("https://www.saucedemo.com/")

    username_name = browser.find_element(By.NAME, "user-name")
    password_input = browser.find_element(By.NAME, "password")
    login_button = browser.find_element(By.NAME, "login-button")

    username_name.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    time.sleep(4)
    login_button.click()

    assert "https://www.saucedemo.com/inventory.html" in browser.current_url


if __name__ == "__main__":
    pytest.main()
