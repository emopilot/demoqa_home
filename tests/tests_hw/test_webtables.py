def test_webtables(browser):
    from pages.webtables_page import WebTablesPage

    # Создаем объект страницы
    page = WebTablesPage(browser)

    # Переходим на страницу
    page.open_page()

    # Проверяем наличие кнопки Add
    page.click_add_button()
    assert page.is_dialog_open(), "Диалоговое окно не открылось"

    # Нажимаем Submit без заполнения формы
    page.submit_form()
    assert page.is_dialog_open(), "Диалоговое окно закрылось после отправки пустой формы"
    assert page.is_form_error_displayed(), "Ошибка не отображается при отправке пустой формы"
