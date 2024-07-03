import time
import pytest
from selenium import webdriver
from selenium.webdriver import Chrome, Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver_path = ""  # TODO: put path to webdriver
    driver = Chrome(service=Service(driver_path))
    yield driver
    driver.quit()


def test_successful_login(browser):
    browser.get("https://www.saucedemo.com/")

    username_name = browser.find_element_by_id("standard_user")
    password_input = browser.find_element_by_id("secret_sauce")
    login_button = browser.find_element_by_id("login-button")

    username_name.send_keys("admin")
    password_input.send_keys("password")

    login_button.click("login-button")

    assert browser.current_url == "https://www.saucedemo.com/"
