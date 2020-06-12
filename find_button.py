import time
from selenium import webdriver

from selenium.webdriver.common.by import By

try:
	browser = webdriver.Chrome()
	browser.get("https://www.tut.by")
	button = browser.find_element(By.ID, "search")
	button.click()
finally:
	time.sleep(5)
	browser.quit()