import math
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    browser.execute_script("window.scrollBy(0, 200);")
    browser.find_element(By.ID, "answer").send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()