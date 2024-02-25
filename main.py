import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.google.com"
}

response = requests.get(url, headers=headers).content

soup = BeautifulSoup(response, 'html.parser')

movie_ul = soup.find('ul')

movies_li = soup.find_all('li', class_='ipc-metadata-list-summary-item')

movies = []

for movie in movies_li:
    title = movie.find('h3', class_='ipc-title__text').text
    year = movie.find('span', class_='cli-title-metadata-item').text
    rating = movie.find('span', class_='ipc-rating-star').text

    movies.append([title, year, rating])

df = pd.DataFrame(movies, columns=['Title', 'Year', 'Rating'])

df.to_csv('movies.csv', index=False)
  