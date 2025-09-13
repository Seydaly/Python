import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from ShopPageLogin import ShopPageLogin
from ShopPageMain import ShopPageMain
from ShopPageCart import ShopPageCart
from ShopPageFinal import ShopPageFinal
from time import sleep


@allure.feature("Покупка товара")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка процесса покупки с итоговой суммой")
@allure.description("Тест добавляет товары в корзину, оформляет заказ и проверяет итоговую стоимость, она должна быть равна $58.29")
def test_calkpage():
    with allure.step("Запуск браузера и открытие страницы логина"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        with allure.step("Вход в систему"):
            shop_page = ShopPageLogin(browser)
            shop_page.login()

        with allure.step("Добавление товаров в корзину и переход в корзину"):
            main_page = ShopPageMain(browser)
            main_page.add_buy()
            main_page.cart_button()

        with allure.step("Оформление заказа"):
            cart_page = ShopPageCart(browser)
            cart_page.check_out()

        with allure.step("Ввод данных покупателя и продолжение"):
            final_page = ShopPageFinal(browser)
            final_page.input()
            final_page.cont_button()

        with allure.step("Проверка итоговой суммы"):
            final_page.actual_total()

    finally:
        with allure.step("Закрытие браузера"):
            browser.quit()
