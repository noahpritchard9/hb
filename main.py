from bs4 import BeautifulSoup
import requests as r

soup = BeautifulSoup(r.get("https://www.sparknotes.com/shakespeare/macbeth/").text)

for link in soup.find_all('a'):
    print(link)
