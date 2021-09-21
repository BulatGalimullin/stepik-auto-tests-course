from selenium import webdriver
import time
import os
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(a):
    return str(math.log(abs(12*math.sin(a)), math.e))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()
    time.sleep(4)
# переключаемся на новое окно
    wind2 = browser.window_handles[1] # находим
    browser.switch_to.window(wind2)

    x = browser.find_element_by_id("input_value")
    x_val = float(x.text)
    y = calc(x_val)

    inp = browser.find_element_by_id('answer')
    inp.send_keys(y)

    browser.find_element_by_tag_name('button').click()

    time.sleep(10)

finally:
    browser.quit()