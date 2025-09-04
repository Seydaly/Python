from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/ajax")

button = WebDriverWait(driver, 16).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary")))

button.click()

message = WebDriverWait(driver, 16).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
)

print(message.text)

driver.quit()
