import pytest
from pages.swag_labs import SwagLabs

def test_icon_exists(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.exist_icon(), "Login icon is missing"

def test_username_field_exists(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.find_element('input#user-name'), "Username field is missing"

def test_password_field_exists(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.find_element('input#password'), "Password field is missing"
