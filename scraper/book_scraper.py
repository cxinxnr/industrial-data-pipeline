import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/"
URL = BASE_URL + "catalogue/page-1.html"

def scrape_books():
    print("🔍 Coletando dados dos livros...")
    books = []
    
    for page in range(1, 3):  # coleta de 2 páginas por enquanto
        url = f"{BASE_URL}catalogue/page-{page}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select(".product_pod")

        for item in items:
            title = item.h3.a["title"]
            price = item.select_one(".price_color").text.strip()
            rating = item.select_one("p.star-rating")["class"][1]  # ex: "Three"
            link = BASE_URL + "catalogue/" + item.h3.a["href"]

            books.append({
                "titulo": title,
                "preco": price,
                "avaliacao": rating,
                "link": link
            })
    
    print(f"✅ {len(books)} livros encontrados.")
    return books

if __name__ == "__main__":
    livros = scrape_books()
    df = pd.DataFrame(livros)
    df.to_csv("data/raw/livros.csv", index=False)
    print("💾 Dados salvos em 'data/raw/livros.csv'")
