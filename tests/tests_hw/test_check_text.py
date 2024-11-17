from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

def test_footer_text(browser):
    page = BasePage(browser, base_url='https://demoqa.com/')
    page.visit()
    footer_text = page.find_element('footer').text
    assert footer_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.', "Footer text does not match"


def test_elements_page_text(browser):
    page = BasePage(browser, base_url='https://demoqa.com/')
    page.visit()
    print("Visited the homepage.")

    elements_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div > div > div.home-body > div > div:nth-child(1)'))
    )
    print("Elements button found.")
    elements_button.click()

    WebDriverWait(browser, 20).until(
        lambda driver: driver.current_url == 'https://demoqa.com/elements'
    )
    print(f"Current URL: {browser.current_url}")
    assert browser.current_url == 'https://demoqa.com/elements', "Failed to navigate to /elements"

    center_text = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.col-12.mt-4.col-md-6'))
    ).text
    print(f"Center text: {center_text}")

    assert center_text == 'Please select an item from left to start practice.', "Center text does not match"
