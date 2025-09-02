from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = r"C:\edgedriver\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))

def test_form_validation():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "first-name")))

    driver.find_element(By.NAME, "first-name").send_keys("Сергей")
    driver.find_element(By.NAME, "last-name").send_keys("Мириев")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("Seydaly7777@gmail.com")
    driver.find_element(By.NAME, "phone").send_keys("+79994452378")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Иваново")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "zip-code")))

    fields = {
        "first-name": "зелёный",
        "last-name": "зелёный",
        "address": "зелёный",
        "e-mail": "зелёный",
        "phone": "зелёный",
        "zip-code": "красный",
        "city": "зелёный",
        "country": "зелёный",
        "job-position": "зелёный",
        "company": "зелёный"
    }

    for field_id, expected_color in fields.items():
        field = driver.find_element(By.ID, field_id)
        if expected_color == "зелёный":
            assert "alert-success" in field.get_attribute("class"), f"Поле {field_id} не подсвечено зелёным!"
        elif expected_color == "красный":
            assert "alert-danger" in field.get_attribute("class"), f"Поле {field_id} не подсвечено красным!"

    print("Форма корректна.")

    driver.quit()

if __name__ == "__main__":
    test_form_validation()
