from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects import shop
from pageObjects.checkout_confirmation import CheckoutConfirmation
from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage


def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    shop_page = loginPage.login() # We can call all the methods of individual pages like LoginPage
    shop_page.addToCart("Blackberry")
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()


