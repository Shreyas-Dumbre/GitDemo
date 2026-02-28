from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage


class LoginPage: #class
    def __init__(self,driver): #constructor has all the locators
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signInBtn = (By.ID, "signInBtn")

#self makes the variable accessible throughout the program
# *,breaks the tuple into two arguments, for find_element(*self.username_input)


    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")   #Contains code for Login Action
        self.driver.find_element(*self.password).send_keys("Learning@830$3mK2")
        self.driver.find_element(*self.signInBtn).click()
        shop_page = ShopPage(self.driver)
        return shop_page