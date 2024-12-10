import requests
from bs4 import BeautifulSoup

class WebScrapper:
    def __init__(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.site = response.text
        except Exception as e:
            print(e)
        else:
            self.template = BeautifulSoup(self.site,  'html.parser')

    def get_links(self):
        links = [link['href'] for link in self.template.select('a.StyledPropertyCardDataArea-anchor')]
        addresses = [address.string.strip() for address in self.template.select('div.StyledPropertyCardDataWrapper address')]
        prices = [price.string.strip() for price in self.template.select('span.PropertyCardWrapper__StyledPriceLine')]
        return [{"link": links[index], "address": addresses[index], "price": prices[index]}for index in range(len(links))]