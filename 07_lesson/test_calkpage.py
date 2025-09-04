from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Pages.CalkPage import CalkPage

def test_calkpage():
    browser = webdriver.Chrome()
    calk_page = CalkPage(browser)
    calk_page.delay_field("45")

    calk_page.button_nums()

    result = calk_page.result()
    assert result == 15

    browser.quit()


