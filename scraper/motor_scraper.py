import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.directindustry.com"
SEARCH_URL = f"{BASE_URL}/industrial-manufacturer/electric-motor-68489.html"

def scrape_motors():
    print("🔍 Buscando dados de motores elétricos...")
    response = requests.get(SEARCH_URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.select(".product-item")
    data = []

    for item in items:
        name = item.select_one(".product-item__title")
        brand = item.select_one(".product-item__brand-name")
        link = item.select_one("a")

        if name and brand and link:
            data.append({
                "nome": name.get_text(strip=True),
                "fabricante": brand.get_text(strip=True),
                "link": BASE_URL + link["href"]
            })

    print(f"✅ {len(data)} itens encontrados.")
    return data

if __name__ == "__main__":
    motores = scrape_motors()
    df = pd.DataFrame(motores)
    df.to_csv("data/raw/motores.csv", index=False)
    print("💾 Dados salvos em 'data/raw/motores.csv'")
