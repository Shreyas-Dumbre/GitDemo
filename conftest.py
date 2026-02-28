import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request): #request is used to access command line input inside fixture.(What browser name user enters)
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(5)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        #options.add_experimental_option("detach", True) | Firefox does not support add_experimental_option("detach", True)
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        driver.implicitly_wait(5)
    yield driver #whoever is calling the driver, will get the driver(Eg: def test_e2e())
    #driver.close() #post your test function execution
