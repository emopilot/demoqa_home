import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.modal_dialogs import ModalDialogsPage


def test_modal_elements(browser):
    # Создаем объект страницы
    page = ModalDialogsPage(browser)

    # Открываем страницу
    page.open_page()

    try:
        # Ожидаем, пока кнопки появятся на странице
        menu_buttons = WebDriverWait(browser, 20).until(
            EC.presence_of_all_elements_located(page.MENU_BUTTONS)
        )

        # Логируем найденные кнопки
        print(f"Найдено {len(menu_buttons)} кнопок:")
        for btn in menu_buttons:
            print(f"- Текст кнопки: {btn.text}, HTML: {btn.get_attribute('outerHTML')}")

        # Проверяем, что кнопок ровно 5
        assert len(menu_buttons) == 5, f"Ожидается 5 кнопок, но найдено {len(menu_buttons)}"

    except Exception as e:
        # Логируем ошибку и делаем скриншот
        browser.save_screenshot("screenshot_error.png")
        pytest.fail(f"Ошибка при проверке кнопок подменю: {e}")
