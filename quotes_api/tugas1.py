from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)  # tunggu loading
    html = driver.page_source
    driver.quit() #biar browsernya ketutup
    return html

def get_quotes():
    url = "https://quotes.toscrape.com/"

    html = get_html(url)
    soup = BeautifulSoup(html,'html.parser')
    
    
    quotes_list = soup.find_all('div', class_='quote')
    thislist = []

    for i in quotes_list:
        
        quote = i.find ("span", class_="text")
        author = i.find("small", class_="author")
        quote = quote.text
        author = author.get_text()
        data = {
            "quote": quote,
            "author": author,
        
            }
        thislist.append(data)
    return {
        "quote": thislist,
        "count": len(thislist),
    }

if __name__ == "__main__":
    get_quotes() 
    
    
       