# web-scraping-with-selenium
Flipkart Product Scraper
This project scrapes product data (title, price, and link) for laptops from Flipkart using Selenium for browser automation and BeautifulSoup for HTML parsing. The extracted data is saved as a CSV file for further analysis.

Features
Selenium: Automates browsing through Flipkart's search result pages.
BeautifulSoup: Parses HTML content to extract product details like title, price, and link.
CSV Output: Saves the extracted product data into a CSV file (extracted_products.csv).
Page Iteration: Scrapes data from 20 pages of search results.
Error Handling: Handles missing data and errors gracefully.
Prerequisites
Python 3.x 
Selenium WebDriver for Chrome (or other browsers).
ChromeDriver: Download the appropriate version of ChromeDriver matching your browser version.
BeautifulSoup and pandas for parsing and saving data
