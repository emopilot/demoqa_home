def test_webtables_add_new_record(browser):
    from pages.webtables_page import WebTablesPage

    page = WebTablesPage(browser)

    page.open_page()

    page.click_add_button()
    assert page.is_dialog_open(), "Диалоговое окно не открылось"

    first_name = "Alice"
    last_name = "Wonderland"
    email = "alice.wonder@land.com"
    age = "25"
    salary = "70000"
    department = "Engineering"
    page.fill_form(first_name, last_name, email, age, salary, department)

    page.submit_form()

    assert page.is_dialog_closed(), "Диалоговое окно не закрылось после отправки формы"

    rows = page.browser.find_elements(*page.TABLE_ROWS)
    print("Таблица содержит строки после добавления записи:")
    for row in rows:
        cells = row.find_elements(*page.TABLE_CELL)
        print([cell.text for cell in cells])

    assert page.is_record_in_table(first_name, last_name, email), \
        "Новая запись не добавлена в таблицу"