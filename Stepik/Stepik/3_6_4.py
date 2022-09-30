"""Tests parametrization"""
import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestPage:
    res = ''
    links = ['https://stepik.org/lesson/236895/step/1',
            'https://stepik.org/lesson/236895/step/1',
            'https://stepik.org/lesson/236896/step/1',
            'https://stepik.org/lesson/236897/step/1',
            'https://stepik.org/lesson/236898/step/1',
            'https://stepik.org/lesson/236899/step/1',
            'https://stepik.org/lesson/236903/step/1',
            'https://stepik.org/lesson/236904/step/1',
            'https://stepik.org/lesson/236905/step/1']

    @pytest.mark.parametrize('links', links)
    #параметризируем тест - добавляя в него набор внешних данных. Тест запуститься для каждого элемента в list.
    def test_guest_should_see_login_link(self, browser, links):
        browser.get(links)
        browser.implicitly_wait(10)
        page = browser.find_element(By.XPATH, "//textarea")
        page.send_keys(math.log(int(time.time())))
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        browser.implicitly_wait(10)
        text = browser.find_element(By.XPATH, "//p[@class = 'smart-hints__hint']").text
        if text != "Correct!":
            self.res = self.res + text
            print(self.res)