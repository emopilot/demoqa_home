from pages.base_page import BasePage

class BaseComponent(BasePage):
    def get_text(self, locator):
        return str(self.find_element(locator).text)
