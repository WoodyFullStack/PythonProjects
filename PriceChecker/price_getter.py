"""
This module does next things
1. Opening txt file with URL links to the items to check their prices
2. Use Selenium Webdriver to get all these prices
2.1 Maybe should use Beautifulsoup for that
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = 'driver/chromedriver.exe'
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(DRIVER_PATH, options=options)
price_locator = '//div[@class="product-buy__price"]'
desc_locator = '//h1[@class="product-card-top__title"]'


def get_list_of_items(filepath):
    """Just get a list of URLs of the items """
    file = open(filepath, 'r', encoding='UTF-8')
    items = file.read().split(',')
    file.close()
    return items


def get_desc_and_prices():
    """
    Get prices from URLs
    Do it silently by using --headless argument
    Use selenium because DNS-shop site doesn't response properly to parse html by beautifullsoup
    :return: list of items in format {url:[item_description, item_price]}
    """
    list_of_items = {}
    for item in get_list_of_items('cart.txt'):
        driver.get(item)
        driver.implicitly_wait(10)
        price = driver.find_element(By.XPATH, price_locator)
        desc = driver.find_element(By.XPATH, desc_locator)
        list_of_items[item] = [desc.text, price.text[0:-2]]
    driver.implicitly_wait(2)
    driver.close()
    return list_of_items