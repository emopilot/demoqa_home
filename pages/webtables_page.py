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

    ADD_BUTTON = (By.ID, "addNewRecordButton")
    DIALOG_BOX = (By.CLASS_NAME, "modal-content")
    SUBMIT_BUTTON = (By.ID, "submit")
    FORM_ERRORS = (By.CSS_SELECTOR, "input:invalid")
    TABLE_ROWS = (By.CSS_SELECTOR, ".rt-tr-group")
    TABLE_CELL = (By.CLASS_NAME, "rt-td")

    FIRST_NAME_FIELD = (By.ID, "firstName")
    LAST_NAME_FIELD = (By.ID, "lastName")
    EMAIL_FIELD = (By.ID, "userEmail")
    AGE_FIELD = (By.ID, "age")
    SALARY_FIELD = (By.ID, "salary")
    DEPARTMENT_FIELD = (By.ID, "department")

    def click_add_button(self):
        add_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        )
        add_button.click()

    def is_dialog_open(self):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(self.DIALOG_BOX)
            )
            return True
        except:
            return False

    def submit_form(self):
        submit_button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        submit_button.click()

    def is_form_error_displayed(self):
        try:
            errors = self.browser.find_elements(*self.FORM_ERRORS)
            return len(errors) > 0
        except:
            return False

    def fill_form(self, first_name, last_name, email, age, salary, department):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.FIRST_NAME_FIELD)
        )
        self.browser.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        self.browser.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.browser.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*self.AGE_FIELD).send_keys(age)
        self.browser.find_element(*self.SALARY_FIELD).send_keys(salary)
        self.browser.find_element(*self.DEPARTMENT_FIELD).send_keys(department)

    def is_dialog_closed(self):
        try:
            WebDriverWait(self.browser, 3).until_not(
                EC.visibility_of_element_located(self.DIALOG_BOX)
            )
            return True
        except:
            return False

    def is_record_in_table(self, first_name, last_name, email):
        rows = self.browser.find_elements(*self.TABLE_ROWS)
        print("Таблица содержит строки:")
        for row in rows:
            cells = row.find_elements(*self.TABLE_CELL)
            print([cell.text for cell in cells])  # Логируем содержимое строк
        try:
            WebDriverWait(self.browser, 5).until(
                lambda driver: any(
                    first_name in cell.text and last_name in cell.text and email in cell.text
                    for row in driver.find_elements(*self.TABLE_ROWS)
                    if row.find_elements(*self.TABLE_CELL)
                    for cell in row.find_elements(*self.TABLE_CELL)
                )
            )
            return True
        except:
            return False

