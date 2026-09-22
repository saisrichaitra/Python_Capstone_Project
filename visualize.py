import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "exported_books.csv"
OUTPUT_FILE = "price_vs_rating.png"

def create_scatter_plot():
    df = pd.read_csv(CSV_FILE)

    plt.figure(figsize=(9, 6))
    plt.scatter(df["price"], df["rating"], alpha=0.75)

    plt.title("Book Price vs Rating")
    plt.xlabel("Price (£)")
    plt.ylabel("Rating (1–5)")
    plt.yticks([1, 2, 3, 4, 5])
    plt.grid(True, alpha=0.25)

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)
    plt.close()

    print(f"Scatter plot saved as {OUTPUT_FILE}")

if __name__ == "__main__":
    create_scatter_plot()
