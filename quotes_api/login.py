import selenium 
import time
from bs4 import BeautifulSoup
from selenium import webdriver


def get_html():
    driver = webdriver.Chrome()
    url = "https://www.saucedemo.com/"
    driver.get(url)

    username = driver.find_element("id", "user-name")
    password = driver.find_element("id", "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    login_button = driver.find_element("id", "login-button")
    login_button.click()
    html_sumber = driver.page_source
    return html_sumber

def parsing ():
    html = get_html()
    soup = BeautifulSoup(html,'html.parser')
    
    print(soup.prettify())


    # thislist = []
    product = soup.find_all('div', class_='inventory_item')
    thislist = []
    
    for i in soup :
    
        product = soup.find_all('div', class_='inventory_item')
        
        for i in soup:
        
            nama = i.find ("div", class_="inventory_item_name")
            harga = i.find("div", class_="inventory_item_price")
            keterangan = i.find("div", class_="inventory_item_desc")
            nama = nama.text
            harga = harga.get_text()
            keterangan = keterangan.get_text()
            data = {
                "nama": nama,
                "harga": harga,
                "keterangan": keterangan,
            
                }
            print(data)
    
    return data
if __name__ == "__main__":
    parsing() 
    
