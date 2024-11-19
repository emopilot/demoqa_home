from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ModalDialogsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/modal-dialogs"
        self.submenu_buttons = (By.CSS_SELECTOR, "div.element-list.collapse.show > ul.menu-list > li.btn.btn-light")  # Локатор кнопок подменю
        self.home_icon = (By.CSS_SELECTOR, "#app > header > a")  # Локатор иконки на главную

    def open_page(self):
        self.driver.get(self.url)

    def get_submenu_buttons_count(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.submenu_buttons)
        )
        return len(self.driver.find_elements(*self.submenu_buttons))

    def click_home_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.home_icon)
        ).click()
