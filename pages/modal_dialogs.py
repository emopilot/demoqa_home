from selenium.webdriver.common.by import By

class ModalDialogsPage:
    URL = "https://demoqa.com/modal-dialogs"
    MENU_BUTTONS = (By.CSS_SELECTOR, "ul.menu-list > li.btn.btn-light")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.URL)

    def get_menu_buttons(self):
        return self.driver.find_elements(*self.MENU_BUTTONS)
