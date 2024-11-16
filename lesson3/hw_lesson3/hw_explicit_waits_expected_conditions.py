# Test 3. Using explicit waits and expected conditions

from selenium.webdriver.support import expected_conditions as EC
import conftest

def test_ui(driver):
    driver.get("https://victoretc.github.io/selenium_waits/")

    locatortag = "/html/body/h1"
    tag_element = driver.find_element("xpath", locatortag)
    assert tag_element.text == "Практика с ожиданиями в Selenium"

    visible_after_button = wait.until(EC.element_to_be_clickable(("css selector", "#startTest")))
    visible_after_button.click()

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