from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_e2e(browser):
    driver = browser
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    #driver.find_element(By.LINK_TEXT, "Shop").click()

    phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    for phone in phones:
        phoneName = phone.find_element(By.XPATH, "div/h4/a").text  # //div[@class='card h-100']/div/h4/a Chaining
        if phoneName == "Blackberry":
            phone.find_element(By.XPATH, "//button[@class='btn btn-info']").click()

    driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()  # understand
    driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("ind")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()
    driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    successText = driver.find_element(By.CLASS_NAME, "alert-success").text

    assert "Success! Thank you!" in successText