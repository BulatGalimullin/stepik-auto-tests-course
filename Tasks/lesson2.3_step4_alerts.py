from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()

    alert = browser.switch_to.alert
    alert.accept()


    time.sleep(10)

finally:
    browser.quit()