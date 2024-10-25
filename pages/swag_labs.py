from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class SwagLabs(BasePage):
    def exist_icon(self):
        locator = 'div.login_logo'
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def exist_username_field(self):
        locator = '#user-name'
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def exist_password_field(self):
        locator = '#password'
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True
