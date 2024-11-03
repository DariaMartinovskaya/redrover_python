from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://195.133.27.184/")
element = browser.find_element(By.XPATH, "/html/body/main/div[1]/div/section[1]/div/a[1]")
element.click()

time.sleep(4)

assert browser.current_url == "http://195.133.27.184/list/", "Wrong URL"

#assert element.is_displayed(), "Element is not visible"