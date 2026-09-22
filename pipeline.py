from database import BookDatabaseManager
from scraper import scrape_first_20_books

def load_scraped_books():
    books = scrape_first_20_books()
    db = BookDatabaseManager("books.db")

    # Re-running the pipeline should not keep duplicating the same 20 records.
    db.clear_books()

    for book in books:
        db.create_book(
            book["title"],
            book["price"],
            book["in_stock"],
            book["rating"]
        )

    print(f"Loaded {len(books)} books into books.db")

if __name__ == "__main__":
    load_scraped_books()
