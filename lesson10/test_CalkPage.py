import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from CalkPage import CalkPage

@allure.title("Проверка калькулятора с задержкой 45 секунд")
@allure.description("Тест проверяет отображение результата вычисления 7 + 8 с задержкой 45 секунд")
@allure.feature("Функциональное тестирование калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
def test_calkpage():
    with allure.step("Запуск браузера Chrome"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        calk_page = CalkPage(browser)

        with allure.step("Установка задержки вычисления"):
            calk_page.delay_field("45")

        with allure.step("Ввод выражения и получение результата"):
            calk_page.button_nums()
            result = calk_page.result()

        with allure.step("Проверка результата"):
            assert result == 15, f"Ожидалось 15, получено {result}"

    finally:
        with allure.step("Закрытие браузера"):
            browser.quit()
