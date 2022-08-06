"""This module does blah blah."""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://netmonet.co/")
VC_SRC = "https://storage.yandexcloud.net/landing-assets/stats/logos/logo_vc.svg"
img_elem = driver.find_element(By.XPATH, f'//img[@src="{VC_SRC}"]')
btn_elem = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')[1]

def test_opacity():
    # assert "abra-cadabra" in driver.title

    assert "opacity: 1" in img_elem.get_attribute("style")
def test_2():
    btn_elem.click()
    assert "opacity: 0.1" in img_elem.get_attribute("style")


def test_close_chrome():
    driver.close()


"""
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.ENTER)
assert "No results found." not in driver.page_source
for cookie in driver.get_cookies():
print(cookie)
"""