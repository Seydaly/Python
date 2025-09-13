import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPageMain:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Добавить товары в корзину")
    def add_buy(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
        ).click()
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-onesie"))
        ).click()

    @allure.step("Нажать кнопку корзины")
    def cart_button(self):
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
