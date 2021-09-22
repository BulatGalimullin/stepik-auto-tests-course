from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath(
        "/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath(
        '/html/body/div/form/div[1]/div[2]/input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath(
        "/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("Smolensk")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)
    browser.quit()


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath(
        "/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath(
        '/html/body/div/form/div[1]/div[2]/input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath(
        "/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("dsfsf@sasdasd.net")
    input4 = browser.find_element_by_xpath(
        "/html/body/div/form/div[2]/div[1]/input")
    input4.send_keys("+324324")
    input5 = browser.find_element_by_xpath(
        "/html/body/div/form/div[2]/div[2]/input")
    input5.send_keys("Kotikov 12")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(1)
    browser.quit()

try:

    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input4 = browser.find_element_by_xpath(
        "/html/body/div/form/div[2]/div[1]/input")
    input4.send_keys("+324324")
    input5 = browser.find_element_by_xpath(
        "/html/body/div/form/div[2]/div[2]/input")
    input5.send_keys("Kotikov 12")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(1)
    browser.quit()