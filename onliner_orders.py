import time
from selenium import webdriver

try:
    # order book
    browser = webdriver.Chrome()
    browser.get("https://oz.by/books/more10685389.html")
    # add to cart
    add_button = browser.find_element_by_class_name("b-product-control__button.i-button.i-button_large.i-button_orange.addtocart-btn.first-button")
    add_button.click()
    # dealy
    time.sleep(3)
    # order game
    browser.get("https://oz.by/boardgames/more1093680.html")
    # add to cart
    add_button = browser.find_element_by_class_name("b-product-control__button.i-button.i-button_large.i-button_orange.addtocart-btn.first-button")
    add_button.click()
    #check cart
    cart = browser.find_elements_by_css_selector(".good")
    print(len(cart))
    assert len(cart) == 2

finally:
    time.sleep(3)
    # close browser
    browser.quit()

