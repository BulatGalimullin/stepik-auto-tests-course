from selenium import webdriver
import time
import math

def calc(a):
    return str(math.log(abs(12*math.sin(a)), math.e))


link = "http://SunInJuly.github.io/execute_script.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value")
    x_val = float(x.text)

    y = calc(x_val)

    browser.execute_script("window.scrollBy(0, 130);")

    inp = browser.find_element_by_id('answer')
    inp.send_keys(y)

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_tag_name('button').click()

    time.sleep(10)

finally:
    browser.quit()