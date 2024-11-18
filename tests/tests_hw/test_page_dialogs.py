# import pytest
# from pages.modal_dialogs import ModalDialogsPage
#
#
# def test_modal_elements(browser):
#     # Создаем объект страницы
#     page = ModalDialogsPage(browser)
#
#     # Переходим на страницу
#     page.open_page()
#
#     # Получаем список кнопок подменю
#     menu_buttons = page.get_menu_buttons()
#     print(f"Найдено кнопок: {len(menu_buttons)}")  # Для отладки
#
#     # Проверяем, что кнопок подменю 5
#     assert len(menu_buttons) == 5, f"Ожидается 5 кнопок, но найдено {len(menu_buttons)}"
