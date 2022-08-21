"""У нас есть span c id="input_value" на странице, это наше значение для x
Берем x подставляем в формулу, жмем всякие галки и whoola"""
import math
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
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