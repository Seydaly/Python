from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    WebDriverWait(driver, 20).until(
        lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3
    )

    images = driver.find_elements(By.TAG_NAME, "img")

    if len(images) >= 3:
        third_image = images[2]
        WebDriverWait(driver, 20).until(
            lambda d: third_image.get_attribute("complete") == "true" or third_image.get_attribute("complete") is True
        )

        src_value = third_image.get_attribute("src")
        print(src_value)
    else:
        print("На странице меньше 3 изображений.")

finally:
    driver.quit()