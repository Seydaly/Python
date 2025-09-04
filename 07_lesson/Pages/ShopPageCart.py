from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPageCart:

  def __init__(self, driver):
    self._driver = driver

  def check_out(self):
    WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
