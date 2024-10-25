from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    base_url = 'https://www.saucedemo.com/'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def visit(self):
        self.driver.get(self.base_url)

    def find_element(self, locator: str):
        return self.driver.find_element(By.CSS_SELECTOR, locator)
