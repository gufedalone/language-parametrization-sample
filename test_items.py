from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart_button_is_displayed(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")))
        element_is_found = True
    except:
        element_is_found = False
    assert element_is_found, '"Add to cart" button is not displayed'
