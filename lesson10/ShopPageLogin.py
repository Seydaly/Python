# ShopPageLogin.py
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPageLogin:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Вход в систему с логином standard_user")
    def login(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")
        self._driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self._driver.find_element(By.ID, "login-button").click()
