import pytest
from selenium import webdriver
from pages.login_form_page import LoginFormPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_fill_state_and_city(driver):
    state = "Haryana"
    city = "Karnal"

    page = LoginFormPage(driver)
    page.open()

    page.select_state(state)
    page.select_city(city)

    selected_state = page.get_selected_state()
    selected_city = page.get_selected_city()

    assert selected_state == state, f"Expected state '{state}', but got '{selected_state}'"
    assert selected_city == city, f"Expected city '{city}', but got '{selected_city}'"
