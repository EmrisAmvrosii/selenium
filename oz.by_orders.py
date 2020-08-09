import time
import urllib
import requests
import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

try:
    # order book
    browser = webdriver.Chrome()
    browser.get("https://oz.by/books/more10685389.html")
    # add to cart
    add_button = browser.find_element_by_class_name("b-product-control__button.i-button.i-button_large.i-button_orange.addtocart-btn.first-button")
    add_button.click()
    # delay
    time.sleep(3)
    # order game
    browser.get("https://oz.by/boardgames/more1093680.html")
    # add to cart
    add_button = browser.find_element_by_class_name("b-product-control__button.i-button.i-button_large.i-button_orange.addtocart-btn.first-button")
    add_button.click()
    time.sleep(3)
    #check cart
    p = urlopen("https://oz.by/checkout/#") 
    sp = BeautifulSoup(p, "html.parser")
    # work on this moment
    cart = sp.find("span", {"class":"top-panel__userbar__cart__count"}).text
    print(cart)
    #assert len(cart) == 2

finally:
    time.sleep(3)
    # close browser
    browser.quit()

r = requests.get('https://oz.by/')
class TestStringMethods(unittest.TestCase):
	def test_oz_by_code_t(self):
		self.assertTrue(r.status_code == 200)
	def test_oz_by_code_f(self):
		self.assertFalse(r.status_code == 404)
	def test_oz_by_encoding(self):
		self.assertFalse(r.encoding == 'utf-8')

if __name__ == '__main__':
    unittest.main()
