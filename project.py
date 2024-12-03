from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# Define the search query
query = "laptop"
file = 0

# Ensure the output directory exists
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()

try:
    # Loop through pages
    for i in range(1, 20):
        # Load the Flipkart search results page
        driver.get(f"https://www.flipkart.com/search?q={query}&page={i}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
        time.sleep(2)  # Wait for the page to load
        
        # Find all elements with the specified class
        elems = driver.find_elements(By.CLASS_NAME, "_75nlfW")
        print(f"Page {i}: {len(elems)} items found")
        
        # Process each element
        for elem in elems:
            # Get the HTML content of the element
            d = elem.get_attribute("outerHTML")
            
            # Save to a file
            with open(os.path.join(output_dir, f"{query}_{file}.html"), "w", encoding="utf-8") as f:
                f.write(d)
            file += 1
        time.sleep(2)  # Pause to avoid hitting the server too frequently
finally:
    # Close the driver
    driver.close()
