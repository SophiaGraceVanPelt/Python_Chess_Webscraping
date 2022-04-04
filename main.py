import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd

url = 'https://www.chess.com/article/view/fide-candidates-chess-tournament-2022'

page = requests.get(url)  # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser')  # Parsing content using beautifulsoup

my_data = []
candidates = soup.select("tr")

for candidate in candidates:
    name = candidate.select('h4')[0].get_text()

    my_data.append({"name": name})

pprint(my_data)


df = pd.DataFrame(my_data)
print(df)

df = df.drop(labels=5, axis=0)
print(df)

df[['name', 'age']] = df['name'].str.split('(', expand=True)
print(df)

df['age'] = df['age'].str.replace(')', '')
print(df)

