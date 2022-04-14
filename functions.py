from bs4 import BeautifulSoup as bs4
import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}

def scraper(url):
    page = requests.get(url, headers=header).content
    soup = bs4(page, "html.parser").findAll("p")
    for div in soup:
        with open("raw_text.txt", mode="a", encoding="utf-8",) as p:
            p.write(div.text)
            
