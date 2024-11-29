from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_timer_alert(browser):
    browser.get("https://demoqa.com/alerts")

    TIMER_ALERT_BUTTON = (By.ID, "timerAlertButton")

    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(TIMER_ALERT_BUTTON)).click()

    WebDriverWait(browser, 10).until(EC.alert_is_present(), "Алерт не появился через 5 секунд")

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Текст алерта: {alert_text}")

    alert.accept()

    try:
        WebDriverWait(browser, 2).until_not(EC.alert_is_present())
        print("Алерт успешно закрыт.")
    except:
        raise AssertionError("Алерт не закрылся после нажатия OK.")
