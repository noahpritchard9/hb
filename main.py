from bs4 import BeautifulSoup
import requests as r

websites = [
    "https://yahoo.com",
    "https://msn.com",
    "https://www.washingtonpost.com",
    "https://www.huffpost.com",
    "https://www.usmagazine.com",
    "https://www.buzzfeed.com",
    "https://www.nytimes.com",
    "https://www.forbes.com",
    "https://www.tmz.com",
    "https://www.eonline.com",
]
for ws in websites:
    print(f"checking {ws}")
    soup = BeautifulSoup(r.get(ws).text)

    for div in soup.select('div:-soup-contains("bid")'):
        print(div)
