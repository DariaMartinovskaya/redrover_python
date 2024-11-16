# Test 2. Using implicit waits

from selenium import webdriver
import pytest

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_ui(driver):
    driver.get("https://victoretc.github.io/selenium_waits/")

    locatortag = "/html/body/h1"
    tag_element = driver.find_element("xpath", locatortag)
    assert tag_element.text == "Практика с ожиданиями в Selenium"

    button1 = "#startTest"
    driver.find_element("css selector", button1).click()

    username_loc = "#login"
    password_loc = "#password"
    username = "standard_user"
    password = "secret_sauce"
    driver.find_element("css selector", username_loc).send_keys(username)
    driver.find_element("css selector", password_loc).send_keys(password)

    checkbox = "#agree"
    driver.find_element("css selector", checkbox).click()

    login_button = "#register"
    driver.find_element("css selector", login_button).click()

    loader = "#loader"
    loader_element = driver.find_element("css selector", loader)
    assert loader_element.is_displayed()

    success_tag = "#successMessage"
    success_tag_element = driver.find_element("css selector", success_tag)
    assert success_tag_element.text == "Вы успешно зарегистрированы!"