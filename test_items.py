import pytest
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_find_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    find_buttons = browser.find_elements_by_css_selector('#add_to_basket_form .btn-add-to-basket')
    assert len(find_buttons) > 0, 'Не найдена кнопка добавления в корзину'
    assert len(find_buttons) < 2, 'Кнопка добавления в корзину не уникальна'
