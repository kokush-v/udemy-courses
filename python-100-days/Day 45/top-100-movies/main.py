from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

html = BeautifulSoup(content, 'html.parser')

titles = html.find_all('h3', 'title')
titles.reverse()
titles_text = "\n".join([title.text for title in titles])

with open('movies.txt', mode='w') as file:
    file.write(titles_text)