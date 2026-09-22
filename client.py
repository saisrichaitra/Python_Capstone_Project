import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/books"

def fetch_books():
    response = requests.get(API_URL, timeout=20)
    response.raise_for_status()
    return response.json()

def main():
    data = fetch_books()
    df = pd.DataFrame(data)

    print("\nBook DataFrame:\n")
    print(df.to_string(index=False))

    df.to_csv("exported_books.csv", index=False)
    print("\nCSV exported as exported_books.csv")

if __name__ == "__main__":
    main()
