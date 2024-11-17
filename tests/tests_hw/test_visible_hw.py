import pytest
from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    page = Accordion(browser)
    page.visit()

    assert page.section1_content_is_visible(), "Section 1 content is not visible initially"

    page.click_section1_heading()

    time.sleep(2)

    assert not page.section1_content_is_visible(), "Section 1 content is still visible after click"


def test_visible_accordion_default(browser):
    page = Accordion(browser)
    page.visit()

    assert page.section2_content_first_is_hidden(), "Section 2 first content is visible by default"
    assert page.section2_content_second_is_hidden(), "Section 2 second content is visible by default"
    assert page.section3_content_is_hidden(), "Section 3 content is visible by default"
