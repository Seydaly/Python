from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window() # сайт на весь экран
driver.get("https://www.transmetall.ru/catalog/katalog_oborudovaniya/promyshlennyye_shveynyye_mashiny/odnoigolnyye_pryamostrochnyye_shveynyye_mashiny/detail/promyshlennaya_mashina_red_shark_rs_1508ae_golovastol_35361") # переход на сайт

# driver.get("https://vk.com/")
# driver.save_screenshot("script.png") # делает снимок экрана (созранить в директорию рабочего файла)

# driver.set_window_size(640, 480) # изменить разрешение

# driver.back()

sleep(20) 