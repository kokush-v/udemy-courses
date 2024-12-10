from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, 'q')
# print(search_bar.get_attribute("placeholder"))

events_date = [date.get_attribute("datetime").split("T")[0] for date in driver.find_elements(By.CSS_SELECTOR, 'div.event-widget ul li time')]
events_names = driver.find_elements(By.CSS_SELECTOR, 'div.event-widget ul li a')
events_dict = {}

for key, date in enumerate(events_date):
    events_dict[key] = {"time": date, "name": events_names[key].text}

print(events_dict)


driver.quit()
