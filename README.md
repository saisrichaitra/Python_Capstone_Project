# Capstone Project: End-to-End Book Data Pipeline & Analytics System

This project contain capstone instructions: scrape the first 20 books from `books.toscrape.com`, store them in SQLite through an object-oriented database manager, expose CRUD operations through FastAPI, export CSV data, and generate a price-vs-rating scatter plot.

## Project structure

```text
book_data_capstone/
├── scraper.py
├── database.py
├── pipeline.py
├── main.py
├── client.py
├── visualize.py
├── requirements.txt
└── README.md
```

Generated at runtime:
- `books.db`
- `exported_books.csv`
- `price_vs_rating.png`

## 1. Create virtual environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Scrape and load the first 20 books

```bash
python pipeline.py
```

This directly requests the main Books to Scrape page, extracts the first 20 records, and stores them in `books.db`.

## 4. Start the FastAPI service

```bash
uvicorn main:app --reload
```

API:
- `GET /books`
- `GET /books/{id}`
- `POST /books`
- `PUT /books/{id}`
- `DELETE /books/{id}`

Interactive API documentation:
```text
http://127.0.0.1:8000/docs
```

## 5. Run the analytical client

Keep FastAPI running in one terminal and open another terminal:

```bash
python client.py
```

This fetches `/books`, loads the response into a Pandas DataFrame, prints it, and creates:

```text
exported_books.csv
```

## 6. Generate visualization

```bash
python visualize.py
```

Output:

```text
price_vs_rating.png
```

The X-axis is Price and the Y-axis is Rating from 1 to 5.

## End-to-end flow

```text
books.toscrape.com
        |
        v
    scraper.py
        |
        v
    pipeline.py
        |
        v
     books.db
        |
        v
     main.py
     FastAPI
        |
        v
     client.py
        |
        v
 Pandas DataFrame
        |
        +----> exported_books.csv
        |
        +----> visualize.py
                    |
                    v
             price_vs_rating.png
```

## CRUD design

`BookDatabaseManager` provides:
- Create: `create_book()`
- Read: `get_books()`, `get_book()`
- Update: `update_book()`
- Delete: `delete_book()`

The database schema contains:
- `id`
- `title`
- `price`
- `in_stock`
- `rating`
