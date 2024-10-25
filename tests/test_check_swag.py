from pages.swag_labs import SwagLabs

def test_icon_exists(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_icon() == True, "Icon not found on the page"

def test_username_field_exists(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_username_field() == True, "Username field not found on the page"

def test_password_field_exists(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_password_field() == True, "Password field not found on the page"
