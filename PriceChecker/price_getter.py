"""
This module does next things
1. Opening txt file with URL links to the items to check their prices
2. Use Selenium Webdriver to get all these prices
2.1 Maybe should use Beautifulsoup for that
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from file_processor import get_list_of_items

DRIVER_PATH = 'driver/chromedriver.exe'
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
PRICE_LOCATOR = '//div[@class="product-buy__price-wrap product-buy__price-wrap_interactive"]/div[1]'
DESC_LOCATOR = '//h1[@class="product-card-top__title"]'


def dns_get_desc_and_prices(user_id):
    """
    Get prices from URLs
    Do it silently by using --headless argument
    Use selenium because DNS-shop site doesn't response properly to parse html by beautifullsoup
    :return: list of items in format {url:[item_description, item_price]}
    """
    list_of_items = {}
    driver = webdriver.Chrome(DRIVER_PATH, options=options)
    for item in get_list_of_items(user_id):
        driver.get(item)
        driver.implicitly_wait(30)
        #when DOM is fully loaded - price still doesn't show sometimes, dunno how to fix it more clever
        while True:
            price = driver.find_element(By.XPATH, PRICE_LOCATOR)
            time.sleep(1)
            if price != '':
                break
        desc = driver.find_element(By.XPATH, DESC_LOCATOR)
        list_of_items[item] = [desc.text, price.text.split('₽')[0]]
    driver.implicitly_wait(2)
    driver.close()
    return list_of_items
