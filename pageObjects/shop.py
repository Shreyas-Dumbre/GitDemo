from selenium.webdriver.common.by import By

from pageObjects.checkout_confirmation import CheckoutConfirmation


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.shop_link = (By.LINK_TEXT, "Shop")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.cart = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")


    def addToCart(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        phones = self.driver.find_elements(*self.product_cards)

        for phone in phones:
            phoneName = phone.find_element(By.XPATH, "div/h4/a").text  # //div[@class='card h-100']/div/h4/a Chaining
            if phoneName == product_name:
                phone.find_element(By.XPATH, "//button[@class='btn btn-info']").click() #These are sublocators, henc not added in constuctor

    def goToCart(self):
        self.driver.find_element(*self.cart).click()  # understand
        checkout_confirmation = CheckoutConfirmation(self.driver)
        return checkout_confirmation