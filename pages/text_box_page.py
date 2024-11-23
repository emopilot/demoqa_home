from selenium.webdriver.common.by import By

class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"

        # Locators
        self.full_name_input = (By.ID, "userName")
        self.current_address_input = (By.ID, "currentAddress")
        self.submit_button = (By.ID, "submit")
        self.output_full_name = (By.ID, "name")
        self.output_current_address = (By.ID, "output")

    def open(self):
        self.driver.get(self.url)

    def fill_text_box(self, full_name, current_address):
        self.driver.find_element(*self.full_name_input).send_keys(full_name)
        self.driver.find_element(*self.current_address_input).send_keys(current_address)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()

    def get_output_text(self):
        full_name_output = self.driver.find_element(*self.output_full_name).text
        current_address_output = self.driver.find_element(*self.output_current_address).text
        return full_name_output, current_address_output


    # def __init__(self, driver):
    #     self.driver = driver
    #     self.full_name_input = (By.ID, "userName")
    #     self.address_input = (By.ID, "currentAddress")
    #     self.submit_button = (By.ID, "submit")
    #     self.output_full_name = (By.ID, "name")
    #     self.output_address = (By.ID, "#currentAddress")

