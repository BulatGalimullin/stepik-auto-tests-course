from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element_by_id('num1')
    x1_val = x1.text

    x2 = browser.find_element_by_id('num2')
    x2_val = x2.text

    y = int(x1_val) + int(x2_val)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))

    browser.find_element_by_tag_name('button').click()

    time.sleep(10)

finally:
    browser.quit()
