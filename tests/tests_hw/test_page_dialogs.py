import pytest
from pages.modal_dialogs import ModalDialogsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_modal_elements(browser):
    page = ModalDialogsPage(browser)

    page.open_page()

    expected_buttons_count = 5
    actual_buttons_count = page.get_submenu_buttons_count()
    assert actual_buttons_count == expected_buttons_count, \
        f"Ожидается {expected_buttons_count} кнопок, но найдено {actual_buttons_count}"

def test_navigation_modal(browser):
    page = ModalDialogsPage(browser)

    page.open_page()

    browser.refresh()

    WebDriverWait(browser, 20).until(EC.url_contains("modal-dialogs"))

    page.click_home_icon()

    WebDriverWait(browser, 20).until(EC.url_to_be("https://demoqa.com/"))
    assert browser.current_url == "https://demoqa.com/", \
        f"Ожидается URL https://demoqa.com/, но получен {browser.current_url}"

    browser.back()

    WebDriverWait(browser, 20).until(EC.url_contains("modal-dialogs"))

    browser.set_window_size(900, 400)

    browser.forward()

    WebDriverWait(browser, 20).until(EC.url_to_be("https://demoqa.com/"))
    assert browser.current_url == "https://demoqa.com/", \
        f"Ожидается URL https://demoqa.com/, но получен {browser.current_url}"

    WebDriverWait(browser, 20).until(
        lambda driver: driver.title == "DEMOQA"
    )
    assert browser.title == "DEMOQA", \
        f"Ожидается title 'DEMOQA', но получен {browser.title}"

    browser.set_window_size(1000, 1000)
