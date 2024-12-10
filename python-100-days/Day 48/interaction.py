import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from datetime import datetime

driver_options = ChromeOptions()
driver_options.add_experimental_option("detach", True)

driver = Chrome(driver_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')
store = driver.find_elements(By.CSS_SELECTOR, '#store div')
store.reverse()

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    try:
        cookie.click()
        for elem in store:
            elem_class = elem.get_attribute("class")
            if not 'grayed' in elem_class:
                elem.click()

    except:
        cookie = driver.find_element(By.ID, 'cookie')
        store = driver.find_elements(By.CSS_SELECTOR, '#store div')
        store.reverse()


# driver.quit()