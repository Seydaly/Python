from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Pages.ShopPageLogin import ShopPageLogin
from Pages.ShopPageMain import ShopPageMain
from Pages.ShopPageCart import ShopPageCart
from Pages.ShopPageFinal import ShopPageFinal

def test_calkpage():
    browser = webdriver.Chrome()
    shop_page = ShopPageLogin(browser)
    shop_page.login()

    main_page = ShopPageMain(browser)
    main_page.add_buy()
    main_page.cart_button()

    cart_page = ShopPageCart(browser)
    cart_page.check_out()

    final_page = ShopPageFinal(browser)
    final_page.input()
    final_page.cont_button()
    final_page.actual_total()

    browser.quit()


