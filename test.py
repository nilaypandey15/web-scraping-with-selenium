from bs4 import BeautifulSoup
import os
import pandas as pd

# List to store product data
product_data = []

# Directory containing HTML files
data_dir = "data"

# Iterate through all files in the directory
for file in os.listdir(data_dir):
    with open(f"{data_dir}/{file}", encoding="utf-8") as f:
        html_doc = f.read()

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Extract product details
    for product in soup.find_all("div", class_="_75nlfW"):
        try:
            # Extract the title
            title = product.find("div", class_="KzDlHZ").text.strip()

            # Extract the price
            price = product.find("div", class_="Nx9bqj").text.strip()

            # Extract the link
            link_element = product.find("a", class_="CGtC98")
            link = link_element["href"] if link_element else None

            # Append the details to the list
            product_data.append({"Title": title, "Price": price, "Link": f"https://www.flipkart.com{link}"})
        except Exception as e:
            print(f"Error extracting details from file {file}: {e}")

# Convert data to DataFrame
df = pd.DataFrame(product_data)

# Save to CSV
df.to_csv("extracted_products.csv", index=False)
print("Data saved to extracted_products.csv")
