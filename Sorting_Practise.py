from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browserveggies = []
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggies = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggies:
    browserveggies.append(element.text)
originalveggies = browserveggies.copy()

browserveggies.sort()

assert originalveggies == browserveggies