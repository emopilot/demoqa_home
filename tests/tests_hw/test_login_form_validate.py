# import pytest
# from selenium import webdriver
# from pages.login_form_page import LoginFormPage
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# @pytest.fixture
# def driver():
#     # Убедитесь, что chromedriver установлен
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# def test_login_form_validate(driver):
#     # Переменные для проверки
#     expected_placeholders = {
#         "first_name": "First Name",
#         "last_name": "Last Name",
#         "user_email": "name@example.com",
#     }
#     expected_email_pattern = r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
#
#     # Работа со страницей
#     page = LoginFormPage(driver)
#     page.open()
#
#     # Проверка плейсхолдеров
#     first_name_placeholder = page.get_placeholder(page.first_name_input)
#     last_name_placeholder = page.get_placeholder(page.last_name_input)
#     user_email_placeholder = page.get_placeholder(page.email_input)
#     assert first_name_placeholder == expected_placeholders["first_name"], "First Name placeholder incorrect!"
#     assert last_name_placeholder == expected_placeholders["last_name"], "Last Name placeholder incorrect!"
#     assert user_email_placeholder == expected_placeholders["user_email"], "User Email placeholder incorrect!"
#
#     # Проверка атрибута pattern у email
#     email_pattern = page.get_attribute(page.email_input, "pattern")
#     assert email_pattern == expected_email_pattern, "Email pattern does not match!"
#
# def submit_empty_form(self):
#     submit_button = self.driver.find_element(*self.submit_button)
#
#         # Ожидание, пока кнопка станет кликабельной
#     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.submit_button))
#     submit_button.click()
#
#     # Проверка класса `was-validated` после отправки пустой формы
#     page.submit_empty_form()
#     assert page.is_form_validated(), "Form is not validated after empty submission!"
#
#
#
