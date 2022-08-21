import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    path = 'G:/Projects/PythonProjects/Stepik/1.txt'
    # Код, который заполняет обязательные поля
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Alina")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Malina")
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys("ai@mail.com")
    textfile = browser.find_element(By.NAME, "file").send_keys(path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()