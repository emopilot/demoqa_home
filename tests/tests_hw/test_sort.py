from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sort_columns_by_class(browser):
    browser.get("https://demoqa.com/webtables")

    COLUMN_HEADERS = [
        (By.CSS_SELECTOR, "div.rt-th:nth-child(1)"),  # First Name
        (By.CSS_SELECTOR, "div.rt-th:nth-child(2)"),  # Last Name
        (By.CSS_SELECTOR, "div.rt-th:nth-child(3)"),  # Age
        (By.CSS_SELECTOR, "div.rt-th:nth-child(4)"),  # Email
        (By.CSS_SELECTOR, "div.rt-th:nth-child(5)"),  # Salary
        (By.CSS_SELECTOR, "div.rt-th:nth-child(6)"),  # Department
    ]

    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "rt-table"))
    )

    for header in COLUMN_HEADERS:
        header_element = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable(header)
        )

        initial_class = header_element.get_attribute("class")

        header_element.click()

        WebDriverWait(browser, 5).until(
            lambda driver: header_element.get_attribute("class") != initial_class
        )

        sorted_class = header_element.get_attribute("class")
        assert sorted_class != initial_class, f"Класс для заголовка не изменился после клика: {header_element.text}"

        header_element.click()

        WebDriverWait(browser, 5).until(
            lambda driver: header_element.get_attribute("class") != sorted_class
        )

        reversed_class = header_element.get_attribute("class")
        assert reversed_class != sorted_class, f"Класс для заголовка не изменился после второго клика: {header_element.text}"

