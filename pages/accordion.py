from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Accordion(BasePage):
    section1_content = (By.CSS_SELECTOR, "#section1Content > p")
    section1_heading = (By.CSS_SELECTOR, "#section1Heading")

    section2_content_first = (By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")
    section2_content_second = (By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")
    section3_content = (By.CSS_SELECTOR, "#section3Content > p")

    def __init__(self, driver, base_url='https://demoqa.com/accordian'):
        super().__init__(driver, base_url)

    def section1_content_is_visible(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.section1_content)
            )
            print("Section 1 content is visible.")
            return element.is_displayed()
        except Exception as e:
            print(f"Error waiting for section 1 content visibility: {e}")
            return False

    def click_section1_heading(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.section1_heading)
            )
            element.click()
            print("Section 1 heading clicked.")
        except Exception as e:
            print(f"Error clicking section 1 heading: {e}")

    def section2_content_first_is_hidden(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located(self.section2_content_first)
            )
            return element
        except Exception as e:
            print(f"Error waiting for section 2 first content invisibility: {e}")
            return True

    def section2_content_second_is_hidden(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located(self.section2_content_second)
            )
            return element
        except Exception as e:
            print(f"Error waiting for section 2 second content invisibility: {e}")
            return True

    def section3_content_is_hidden(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located(self.section3_content)
            )
            return element
        except Exception as e:
            print(f"Error waiting for section 3 content invisibility: {e}")
            return True
