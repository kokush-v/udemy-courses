import time

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

class SeleniumModule:
    def __init__(self):
        url = "https://docs.google.com/forms/d/e/1FAIpQLScgNU3Uz8mZE6gOmvMBqI96hJlFjMw7uuRDkety7wh_idyxhg/viewform"
        options = ChromeOptions()
        options.add_experimental_option('detach',True)
        self.web_driver = Chrome(options=options)
        self.web_driver.get(url)


    def send_data_to_form(self, links: list[dict]):
        for link in links:
            address_field = self.web_driver.find_element(By.XPATH,
                                                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field = self.web_driver.find_element(By.XPATH,
                                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field = self.web_driver.find_element(By.XPATH,
                                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit = self.web_driver.find_element(By.XPATH,
                                                  '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
            time.sleep(2)
            address_field.send_keys(link["address"])
            price_field.send_keys(link["price"])
            link_field.send_keys(link["link"])
            submit.click()
            time.sleep(2)
            send_more = self.web_driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            send_more.click()

