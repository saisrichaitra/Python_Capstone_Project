import re
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_first_20_books():
    response = requests.get(BASE_URL, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for article in soup.select("article.product_pod")[:20]:
        title_tag = article.select_one("h3 a")
        price_tag = article.select_one("p.price_color")
        availability_tag = article.select_one("p.instock.availability")
        rating_tag = article.select_one("p.star-rating")

        title = title_tag.get("title", "").strip()
        price_text = price_tag.get_text(strip=True)
        price = float(re.sub(r"[^0-9.]", "", price_text))

        availability = availability_tag.get_text(" ", strip=True)
        in_stock = "in stock" in availability.lower()

        rating_classes = rating_tag.get("class", [])
        rating_words = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating = next((rating_words[word] for word in rating_words if word in rating_classes), None)

        books.append({
            "title": title,
            "price": price,
            "in_stock": in_stock,
            "rating": rating
        })

    return books

if __name__ == "__main__":
    data = scrape_first_20_books()
    for index, book in enumerate(data, start=1):
        print(f"{index}. {book}")
