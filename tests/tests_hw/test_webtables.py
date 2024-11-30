from pages.webtables_page import WebTablesPage

def test_webtables_crud_operations(browser):
    page = WebTablesPage(browser)

    page.open_page()

    page.wait_and_click(page.ADD_BUTTON)
    assert page.is_dialog_open(), "Диалоговое окно не открылось"

    page.wait_and_click(page.SUBMIT_BUTTON)
    assert len(browser.find_elements(*page.FORM_ERRORS)) > 0, "Ошибки формы не отображаются при сохранении пустой формы"

    new_record = {
        "firstName": "Tom",
        "lastName": "Soyer",
        "userEmail": "tom.soyer@fin.com",
        "age": "10",
        "salary": "230000",
        "department": "Engineering",
    }

    page.fill_form(new_record)
    page.wait_and_click(page.SUBMIT_BUTTON)

    assert page.is_dialog_closed(), "Диалоговое окно не закрылось"
    assert page.is_record_in_table(new_record), "Запись не добавилась в таблицу"

    page.perform_action_on_row(new_record, "edit")

    assert page.is_dialog_open(), "Диалоговое окно не открылось для редактирования"
    for field, locator in page.FORM_FIELDS.items():
        input_field = page.browser.find_element(*locator)
        assert input_field.get_attribute("value") == new_record[field], f"Поле {field} не соответствует ожидаемым данным"

    updated_record = new_record.copy()
    updated_record["firstName"] = "Jane"
    page.fill_form(updated_record)
    page.wait_and_click(page.SUBMIT_BUTTON)

    assert page.is_dialog_closed(), "Диалоговое окно не закрылось"
    assert page.is_record_in_table(updated_record), "Запись не обновилась в таблице"

    page.perform_action_on_row(updated_record, "delete")

    assert not page.is_record_in_table(updated_record), "Запись не была удалена из таблицы"
