"""This module does blah blah."""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://netmonet.co/")
# assert "abra-cadabra" in driver.title
img_elem = driver.find_element(By.XPATH, '//img[@src="https://storage.yandexcloud.net/landing-assets/stats/logos'
                                         '/logo_4hands.svg"]')
print(img_elem.get_attribute('style'))
assert "opacity: 1" in img_elem.get_attribute("style")
btn_elem = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
btn_elem.click()
print(img_elem.get_attribute('style'))
assert "opacity: 0.1" in img_elem.get_attribute("style")


"""print(elem.click())
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.ENTER)
assert "No results found." not in driver.page_source
driver.close()
for cookie in driver.get_cookies():
print(cookie)
"""