from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_calc():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        delay_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_field.clear()
        delay_field.send_keys("45")

        btn7 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']"))
        )
        btn7.click()
        print("Кнопка 7 нажата")

        btn_plus = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']"))
        )
        btn_plus.click()
        print("Кнопка + нажата")

        btn8 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']"))
        )
        btn8.click()
        print("Кнопка 8 нажата")

        btn_equal = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']"))
        )
        btn_equal.click()
        print("Кнопка = нажата")

        result_element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.screen"))
        )

        WebDriverWait(driver, 50).until(lambda d: result_element.text == "15")
        result_text = result_element.text
        print(f"Результат: {result_text}")
        assert result_text == "15", f"Ожидалось '15', но получено '{result_text}'"

    except Exception as e:
        print(f"Ошибка во время теста: {e}")

    finally:
        driver.quit()
        print("Браузер закрыт")
