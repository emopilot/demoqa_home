from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebTablesPage:
    URL = "https://demoqa.com/webtables"

    def __init__(self, browser):
        self.browser = browser

    # Открыть страницу
    def open_page(self):
        self.browser.get(self.URL)

    # Локаторы
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    DIALOG_BOX = (By.CLASS_NAME, "modal-content")
    SUBMIT_BUTTON = (By.ID, "submit")
    FORM_ERRORS = (By.CSS_SELECTOR, "input:invalid")

    # Нажать кнопку Add
    def click_add_button(self):
        add_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        )
        add_button.click()

    # Проверить, что диалоговое окно открыто
    def is_dialog_open(self):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(self.DIALOG_BOX)
            )
            return True
        except:
            return False

    # Нажать Submit в диалоговом окне
    def submit_form(self):
        submit_button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        submit_button.click()

    # Проверить наличие ошибок формы
    def is_form_error_displayed(self):
        try:
            errors = self.browser.find_elements(*self.FORM_ERRORS)
            return len(errors) > 0
        except:
            return False
