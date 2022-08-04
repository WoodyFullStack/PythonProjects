from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://selenium-python.readthedocs.io/navigating.html")
assert "Navigating" in driver.title
# elem = driver.find_element(By.NAME, "q")
# print(elem.click())
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.ENTER)
# assert "No results found." not in driver.page_source
driver.close()
for cookie in driver.get_cookies():
    print(cookie)
