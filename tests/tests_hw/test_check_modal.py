from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_modal_dialogs(browser):
    browser.get("https://demoqa.com/modal-dialogs")

    SMALL_MODAL_BUTTON = (By.ID, "showSmallModal")
    LARGE_MODAL_BUTTON = (By.ID, "showLargeModal")
    SMALL_MODAL = (By.ID, "example-modal-sizes-title-sm")
    LARGE_MODAL = (By.ID, "example-modal-sizes-title-lg")
    CLOSE_SMALL_MODAL_BUTTON = (By.ID, "closeSmallModal")
    CLOSE_LARGE_MODAL_BUTTON = (By.ID, "closeLargeModal")


    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SMALL_MODAL_BUTTON)).click()

    small_modal = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(SMALL_MODAL)
    )
    assert small_modal.is_displayed(), "Small modal не открылся"

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(CLOSE_SMALL_MODAL_BUTTON)
    ).click()

    WebDriverWait(browser, 5).until(
        EC.invisibility_of_element_located(SMALL_MODAL)
    )

    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(LARGE_MODAL_BUTTON)).click()

    large_modal = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LARGE_MODAL)
    )
    assert large_modal.is_displayed(), "Large modal не открылся"

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(CLOSE_LARGE_MODAL_BUTTON)
    ).click()

    WebDriverWait(browser, 5).until(
        EC.invisibility_of_element_located(LARGE_MODAL)
    )
