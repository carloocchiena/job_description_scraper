from bs4 import BeautifulSoup as bs4
import requests

def scraper(url):
    page = requests.get(url).content
    soup = bs4(page, "html.parser").findAll("p")
    for div in soup:
        with open("raw_text.txt", mode="a", encoding="utf-8",) as p:
            p.write(div.text)