from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url='https://www.saucedemo.com/'):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

class BasePage1:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_element_visible(self, locator):
        try:
            self.wait_for_element(locator)
            return True
        except:
            return False
