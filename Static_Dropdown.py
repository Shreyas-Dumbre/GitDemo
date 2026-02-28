import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "dropdown-class-example").click()
dropdowns = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdowns.select_by_visible_text("Option1")
driver.find_element(By.TAG_NAME, "body").click()
input("Press any key to exit")