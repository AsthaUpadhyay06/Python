import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for q, a in zip(quotes[:5], authors[:5]):  # show first 5
    print(q.text, "-", a.text)