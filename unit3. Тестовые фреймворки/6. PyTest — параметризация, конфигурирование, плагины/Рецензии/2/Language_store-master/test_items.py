from selenium.webdriver.common.by import By
from time import sleep

link =' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_busket_button(browser):
    browser.get(link)
    #sleep(30)
    add_basket=browser.find_element_by_css_selector(".btn-add-to-basket")
    assert add_basket, 'No add button on page'