# import pytest
# from selenium import webdriver
# from pages.text_box_page import TextBoxPage
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# def test_text_box(driver):
#     full_name = "Alice Wonderland"
#     current_address = "1 Christchurch, Oxford"
#
#     page = TextBoxPage(driver)
#     page.open()
#     page.fill_text_box(full_name, current_address)
#     page.submit_form()
#
#     output_name, output_address = page.get_output_text()
#     assert full_name in output_name, "Full Name does not match!"
#     assert current_address in output_address, "Current Address does not match!"
