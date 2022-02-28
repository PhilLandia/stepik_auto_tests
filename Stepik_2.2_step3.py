from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time


link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_element = int(browser.find_element_by_id('num1').text)
    second_element = int(browser.find_element_by_id('num2').text)
    y = first_element + second_element

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))# ищем элемент с текстом "Python"
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
finally:
    time.sleep(7)
    browser.quit()
