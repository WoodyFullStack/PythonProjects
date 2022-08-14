import requests
import selenium.webdriver
from selenium.webdriver.common.by import By


def get_list_of_items(filepath):
    file = open(filepath, 'r')
    items = file.read().split(',')
    file.close()
    return items


def get_desc_and_prices():
    for item in get_list_of_items('cart.txt'):
        driver = selenium.webdriver.Chrome()
        driver.get(item)
        driver.implicitly_wait(10)
        price = driver.find_elements(By.CSS_SELECTOR,
                                     '#pc-8sSL > div.product-card-top.product-card-top_full > '
                                     'div.product-card-top__buy > '
                                     'div.product-buy.product-buy_one-line > div > div.product-buy__price')
        print(price)


get_desc_and_prices()
