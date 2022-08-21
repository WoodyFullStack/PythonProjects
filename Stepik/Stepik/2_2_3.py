
import math
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    sum = int(x)+int(y)

    select = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
    select.select_by_value(str(sum))

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()