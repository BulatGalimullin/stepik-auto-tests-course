
def test_cart_button_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    browser.implicitly_wait(5)
    card_button = browser.find_elements_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")

    assert len(card_button) > 0, "Кнопка добавления в корзину не найдена"

