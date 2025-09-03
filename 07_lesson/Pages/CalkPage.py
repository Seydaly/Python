from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalkPage:

  def __init__(self, driver):
    self._driver = driver
    self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    self._driver.implicitly_wait(4)
    self._driver.maximize_window()

  def delay_field(self, value):
    delay_field = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
    delay_field.clear()
    delay_field.send_keys(value)

  def button_nums(self):
    btn7 = WebDriverWait(self._driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']"))
        )
    btn7.click()

    btn_plus = WebDriverWait(self._driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']"))
        )
    btn_plus.click()

    btn8 = WebDriverWait(self._driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']"))
        )
    btn8.click()

    btn_equal = WebDriverWait(self._driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']"))
        )
    btn_equal.click()

  def result(self):
    result_element = WebDriverWait(self._driver, 50).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.screen"))
    )
    WebDriverWait(self._driver, 50).until(lambda d: result_element.text == "15")
    result_value = int(result_element.text)
    print(f"Результат: {result_value}")
    return result_value



