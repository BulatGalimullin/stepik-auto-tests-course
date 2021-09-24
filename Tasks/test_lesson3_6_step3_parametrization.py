import pytest
from selenium import webdriver
import time
import math
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'Files', '3_6_links.txt')  # добавляем к этому пути имя файла

# открываем файл
f = open(file_path, 'r')
links = [line.strip() for line in f]


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestSendFeedback():
    output_text = ""

    @pytest.mark.parametrize("link", links)
    def test_feed(self, browser, link):
        browser.get(link)

        textare = browser.find_element_by_css_selector('[class="ember-text-area ember-view textarea string-quiz__textarea"]')
        textare.send_keys(str(math.log(int(time.time()))))

        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))
        )

        browser.find_element_by_class_name('submit-submission').click()

        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )

        el = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text

        if el != "Correct!":
            self.output_text += el
            print(self.output_text)

        assert el == "Correct!", el


