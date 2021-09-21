from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(a):
    return str(math.log(abs(12*math.sin(a)), math.e))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет видно текста 100$
    WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    browser.find_element_by_id('book').click()

    x = browser.find_element_by_id("input_value")
    x_val = float(x.text)
    y = calc(x_val)

    inp = browser.find_element_by_id('answer')
    inp.send_keys(y)

    browser.find_element_by_id('solve').click()

    time.sleep(10)


finally:
    browser.quit()