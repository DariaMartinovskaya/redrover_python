# Test 1. Using time.sleep()
import time

def test_ui(driver):
    driver.get("https://victoretc.github.io/selenium_waits/")

    locatortag = "/html/body/h1"
    tag_element = driver.find_element("xpath", locatortag)
    assert tag_element.text == "Практика с ожиданиями в Selenium"

    time.sleep(8)

    button1 = "#startTest"
    driver.find_element("css selector", button1).click()
    time.sleep(2)

    username_loc = "#login"
    password_loc = "#password"
    username = "standard_user"
    password = "secret_sauce"
    time.sleep(1)
    driver.find_element("css selector", username_loc).send_keys(username)
    time.sleep(1)
    driver.find_element("css selector", password_loc).send_keys(password)
    time.sleep(1)

    checkbox = "#agree"
    driver.find_element("css selector", checkbox).click()
    time.sleep(1)

    login_button = "#register"
    driver.find_element("css selector", login_button).click()
    time.sleep(1)

    loader = "#loader"
    loader_element = driver.find_element("css selector", loader)
    time.sleep(1)
    assert loader_element.is_displayed()
    time.sleep(2)

    success_tag = "#successMessage"
    success_tag_element = driver.find_element("css selector", success_tag)
    assert success_tag_element.text == "Вы успешно зарегистрированы!"

