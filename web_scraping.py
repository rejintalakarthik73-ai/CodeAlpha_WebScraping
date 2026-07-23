import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Lists to store data
titles = []
prices = []

# Find all books
books = soup.find_all("article", class_="product_pod")

# Extract title and price
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    titles.append(title)
    prices.append(price)

# Create DataFrame
df = pd.DataFrame({
    "Book Title": titles,
    "Price": prices
})

# Save to CSV
df.to_csv("books_data.csv", index=False)

print(df.head())
print("✅ Data saved successfully as books_data.csv")