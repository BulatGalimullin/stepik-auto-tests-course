from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name('firstname')
    name.send_keys("Я")
    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys("устал")
    mail = browser.find_element_by_name('email')
    mail.send_keys("от всего")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'Files', 'fuck.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_id('file').send_keys(file_path)

    browser.find_element_by_tag_name('button').click()

    time.sleep(10)

finally:
    browser.quit()