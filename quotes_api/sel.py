import selenium
import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/")
time.sleep(2)
# tunggu 2 detik untuk memastikan halaman sudah dimuat

html = driver.page_source
# mengembalikan HTML lengkap dari halaman yang sudah dimuat.
print(html)

driver.quit()
# menutup browser setelah selesai

# ngambil html pake selenium 
# pindahin selenium ke tugas 1.py
