from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    robot_check = browser.find_element_by_id('robotCheckbox')
    robot_check.click()

    robot_radio = browser.find_element_by_id('robotsRule')
    robot_radio.click()

    btn = browser.find_element_by_tag_name('button')
    btn.click()

    time.sleep(5)

finally:
    browser.quit()
