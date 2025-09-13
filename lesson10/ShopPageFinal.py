# ShopPageFinal.py
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPageFinal:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Ввод данных покупателя")
    def input(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys("Сергей")
        self._driver.find_element(By.ID, "last-name").send_keys("Мирие")
        self._driver.find_element(By.ID, "postal-code").send_keys("777777")

    @allure.step("Нажать кнопку Continue")
    def cont_button(self):
        self._driver.find_element(By.ID, "continue").click()

    @allure.step("Проверка итоговой суммы")
    def actual_total(self):
        total_element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        print(f"Итоговая стоимость: {total_text}")

        expected_total = "$58.29"
        actual_total = total_text.split(":")[-1].strip()
        assert actual_total == expected_total, f"Ожидалось {expected_total}, получено {actual_total}"
