🛒 Saucedemo Product Scraper

A Python project for scraping product data from the Saucedemo
 website using BeautifulSoup and Pandas.

⭐ STAR Summary

Situation:
The Saucedemo website offers a sample e-commerce storefront for testing, but it doesn't provide direct access to product data in structured format.

Task:
Build a simple scraper that extracts product information such as names, prices, descriptions, and image URLs for testing or analysis.

Action:

Sent HTTP requests directly to the Saucedemo product page (static HTML)

Used BeautifulSoup to parse the HTML content and extract relevant data

Processed and exported the data into a structured format using Pandas

Result:
Successfully created a clean dataset of products from Saucedemo that can be used for further testing, data visualization, or machine learning models.

🔧 Features

Extracts product name, price, description, and image URL

Parses static HTML content without needing Selenium

Outputs results in CSV or XLSX format using Pandas

Simple and lightweight — ideal for beginner scraping projects

📦 How to Use
git clone https://github.com/filzaaisya/quotes_api
cd quotes_api
pip install -r requirements.txt
python saucedemo_scraper.py

📝 Output Example

The script will generate a CSV file 

📁 Requirements

requests

beautifulsoup4

pandas

Install via:

pip install -r requirements.txt

📌 About

This is a beginner-level Python scraping project focused on extracting product data from the static HTML of the Saucedemo
 site.
It’s a simple example to demonstrate web scraping without needing advanced tools like Selenium.