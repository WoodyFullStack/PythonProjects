"""
This module does next things
1. Opening txt file with URL links to the items to check their prices
2. Use Selenium Webdriver to get all these prices
2.1 Maybe should use Beautifulsoup for that
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_list_of_items(filepath):
    """Just get a list of URLs of the items """
    file = open(filepath, 'r', encoding='UTF-8')
    items = file.read().split(',')
    file.close()
    return items


def get_desc_and_prices():
    """
    Get prices from URLs
    :return: nothing ATM
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    for item in get_list_of_items('cart.txt'):
        driver.get(item)
        driver.implicitly_wait(10)
        price = driver.find_element(By.XPATH, '//div[@class="product-buy__price"]')
        desc = driver.find_element(By.XPATH, '//div[@class="product-card-top__specs"]')
        print(f"Товар {desc.text} стоит {price.text}ублей")
    driver.close()


get_desc_and_prices()
