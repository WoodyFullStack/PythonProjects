"""
This module does next things
1. Opening txt file with URL links to the items to check their prices
2. Use Selenium Webdriver to get all these prices
2.1 Maybe should use Beautifulsoup for that
"""

import selenium.webdriver
from selenium.webdriver.common.by import By


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
    for item in get_list_of_items('cart.txt'):
        driver = selenium.webdriver.Chrome()
        driver.get(item)
        driver.implicitly_wait(10)
        price = driver.find_elements(By.CSS_SELECTOR,
                                     '#pc-8sSL > div.product-card-top.product-card-top_full > '
                                     'div.product-card-top__buy > div.product-buy.product-buy_one-line > div > '
                                     'div.product-buy__price')
        print(price)


get_desc_and_prices()
