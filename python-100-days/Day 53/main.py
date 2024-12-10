from selenim_module import SeleniumModule
from web_scrapper import WebScrapper

url = "https://appbrewery.github.io/Zillow-Clone/"
web_scrapper = WebScrapper(url)
selenium_module = SeleniumModule()

links = web_scrapper.get_links()
selenium_module.send_data_to_form(links)
print(links)