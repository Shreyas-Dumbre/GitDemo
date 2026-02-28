import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH, "//input[@placeholder='Type to Select Countries']").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
value = driver.find_element(By.XPATH, "//input[@placeholder='Type to Select Countries']").get_attribute("value")
print(value)
assert value == "India"

