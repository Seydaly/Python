from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/dynamicid")
    time.sleep(2)
    button = driver.find_element(By.XPATH, "//button[contains(text(), 'Button')]")
    button.click()
    print("Кнопка нажата")
    time.sleep(1)

finally:
    driver.quit()
