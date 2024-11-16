from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait

def test_ui(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    add_element_button = ("xpath", "/html/body/div[2]/div/div/button")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(add_element_button)).click()

    delete_button = ("xpath", "/html/body/div[2]/div/div/div/button")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(delete_button)).click()

def test_authorization(driver):
    driver.get("https://the-internet.herokuapp.com/basic_auth")

    username_field = ("xpath", "")

    visible__sign_in_pop_up = wait.until(EC.element_to_be_clicable(("xpath", "#startTest")))





