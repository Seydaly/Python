from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def test_shop():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    try:
        driver.get("https://www.saucedemo.com/")

        wait = WebDriverWait(driver, 10)

        username_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-onesie"))).click()

        cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()

        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        last_name_input = driver.find_element(By.ID, "last-name")
        postal_code_input = driver.find_element(By.ID, "postal-code")

        first_name_input.send_keys("Сергей")
        last_name_input.send_keys("Мирие")
        postal_code_input.send_keys("777777")

        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        total = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_text = total.text

        print(f"Итоговая стоимость: {total_text}")

        expected_total = "$58.29"
        actual_total = total_text.split(":")[-1].strip()

        assert actual_total == expected_total

    except Exception as e:
        print(f"Ошибка во время теста: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_shop()
