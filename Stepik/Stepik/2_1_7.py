"""У нас есть картинка на странице, значение x спрятано в её атрибуте
Берем x подставляем в формулу, жмем всякие галки и whoola"""
import math
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    textbox = browser.find_element(By.ID, "answer")
    textbox.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()