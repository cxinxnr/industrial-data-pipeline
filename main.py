from scraper.book_scraper import scrape_books
from cleaner.clean_books_data import limpar_dados
from analysis.analyze_books import analisar_dados
from database.save_to_db import salvar_em_banco

RAW_PATH = "data/raw/livros.csv"
CLEAN_PATH = "data/processed/livros_limpos.csv"
DB_PATH = "data/livros.db"

def main():
    print("🚀 Iniciando pipeline completa...\n")

    # 1. Coleta de dados
    scrape_books()

    # 2. Limpeza de dados
    limpar_dados(RAW_PATH)

    # 3. Análise exploratória
    analisar_dados(CLEAN_PATH)

    # 4. Salvando em banco de dados
    salvar_em_banco(CLEAN_PATH, DB_PATH)

    print("\n✅ Pipeline finalizada com sucesso!")

if __name__ == "__main__":
    main()
