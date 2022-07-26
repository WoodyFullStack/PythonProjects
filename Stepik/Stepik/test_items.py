from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button_exists(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    assert browser.find_elements(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']") != [], 'Элемент не найден'