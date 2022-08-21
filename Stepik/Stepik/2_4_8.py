import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    while True:
        if browser.find_element(By.ID, "price").text == '$100':
            break
        time.sleep(1)
    browser.find_element(By.CLASS_NAME, "btn").click()

    browser.find_element(By.ID, "answer").send_keys(calc(browser.find_element(By.ID, "input_value").text))

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

