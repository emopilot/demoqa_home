from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ModalDialogsPage:
    URL = "https://demoqa.com/modal-dialogs"

    def __init__(self, driver):
        self.driver = driver
        self.menu_buttons_locator = (By.CSS_SELECTOR, ".element-group:nth-child(1) .menu-list a")

    def open_page(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )

    def get_menu_buttons(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(self.menu_buttons_locator)
        )
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located(self.menu_buttons_locator)
        )
