from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.email_input = (By.ID, "userEmail")
        self.submit_button = (By.ID, "submit")
        self.form = (By.ID, "userForm")

    def open(self):
        self.driver.get(self.url)

    def get_placeholder(self, locator):
        element = self.driver.find_element(*locator)
        return element.get_attribute("placeholder")

    def get_attribute(self, locator, attribute):
        element = self.driver.find_element(*locator)
        return element.get_attribute(attribute)

    def submit_empty_form(self):
        self.driver.find_element(*self.submit_button).click()

    def is_form_validated(self):
        form = self.driver.find_element(*self.form)
        return "was-validated" in form.get_attribute("class")


class LoginFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

        self.state_dropdown = (By.ID, "state")
        self.city_dropdown = (By.ID, "city")
        self.state_selected = (By.CSS_SELECTOR, "#state .css-1uccc91-singleValue")
        self.city_selected = (By.CSS_SELECTOR, "#city .css-1uccc91-singleValue")

    def open(self):
        self.driver.get(self.url)

    def select_state(self, state_name):
        state_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.state_dropdown)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", state_input)
        state_input.click()

        action = ActionChains(self.driver)
        action.send_keys(state_name).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.state_selected)
        )

    def select_city(self, city_name):
        city_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.city_dropdown)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", city_input)
        city_input.click()

        action = ActionChains(self.driver)
        action.send_keys(city_name).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.city_selected)
        )

    def get_selected_state(self):
        selected_state = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.state_selected)
        )
        return selected_state.text

    def get_selected_city(self):
        selected_city = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.city_selected)
        )
        return selected_city.text