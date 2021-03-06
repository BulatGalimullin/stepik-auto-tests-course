import unittest
from selenium import webdriver
import time

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input[class = 'form-control first'][required]")
        input1.send_keys('hello')
        input2 = browser.find_element_by_css_selector("input[class = 'form-control second'][required]")
        input2.send_keys('h3i')
        input3 = browser.find_element_by_css_selector("input[class = 'form-control third'][required]")
        input3.send_keys('hi')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text messages do not match each other")

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input[class = 'form-control first'][required]")
        input1.send_keys('hello')
        input2 = browser.find_element_by_css_selector("input[class = 'form-control second'][required]")
        input2.send_keys('h3i')
        input3 = browser.find_element_by_css_selector("input[class = 'form-control third'][required]")
        input3.send_keys('hi')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text messages do not match each other")

        # закрываем браузер после всех манипуляций
        browser.quit()




if __name__ == "__main__":
    unittest.main()