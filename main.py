import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(browser):
    browser.get("https://example.com")
    username_input = browser.find_element_by_id("username")
    username_input.send_keys("your_username")
    password_input = browser.find_element_by_id("password")
    password_input.send_keys("your_password")
    password_input.send_keys(Keys.RETURN)
    assert "Welcome" in browser.page_source
