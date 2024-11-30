from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebTablesPage:
    URL = "https://demoqa.com/webtables"

    # Локаторы
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    DIALOG_BOX = (By.CLASS_NAME, "modal-content")
    SUBMIT_BUTTON = (By.ID, "submit")
    FORM_ERRORS = (By.CSS_SELECTOR, "input:invalid")
    TABLE_ROWS = (By.CLASS_NAME, "rt-tr-group")
    EDIT_BUTTON = (By.CSS_SELECTOR, ".action-buttons span[title='Edit']")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".action-buttons span[title='Delete']")
    FORM_FIELDS = {
        "firstName": (By.ID, "firstName"),
        "lastName": (By.ID, "lastName"),
        "userEmail": (By.ID, "userEmail"),
        "age": (By.ID, "age"),
        "salary": (By.ID, "salary"),
        "department": (By.ID, "department"),
    }

    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.get(self.URL)

    def wait_for_element(self, locator, timeout=5):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    def wait_and_click(self, locator, timeout=5):
        element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def fill_form(self, data):
        for field, locator in self.FORM_FIELDS.items():
            input_field = self.wait_for_element(locator)
            input_field.clear()
            input_field.send_keys(data[field])

    def get_table_rows(self):
        rows = self.browser.find_elements(*self.TABLE_ROWS)
        return [row.text for row in rows if row.text.strip()]

    def is_record_in_table(self, data):
        rows = self.get_table_rows()
        return any(
            data["firstName"] in row and data["lastName"] in row and data["userEmail"] in row
            for row in rows
        )

    def is_dialog_open(self):
        try:
            self.wait_for_element(self.DIALOG_BOX)
            return True
        except:
            return False

    def is_dialog_closed(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.invisibility_of_element(self.DIALOG_BOX))
            return True
        except:
            return False

    def perform_action_on_row(self, data, action):
        rows = self.browser.find_elements(*self.TABLE_ROWS)
        for row in rows:
            if (
                    data["firstName"] in row.text
                    and data["lastName"] in row.text
                    and data["userEmail"] in row.text
            ):
                if action == "edit":
                    row.find_element(By.CSS_SELECTOR, "span[title='Edit']").click()
                elif action == "delete":
                    row.find_element(By.CSS_SELECTOR, "span[title='Delete']").click()
                break
        else:
            raise ValueError("Строка с указанными данными не найдена")