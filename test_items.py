import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_basket(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_element_by_css_selector(".btn-add-to-basket")