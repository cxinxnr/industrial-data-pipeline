import pandas as pd
import sqlite3
import os

CLEAN_PATH = "data/processed/livros_limpos.csv"
DB_PATH = "data/livros.db"

def salvar_em_banco(csv_path, db_path):
    print("💾 Salvando dados no banco SQLite...")

    df = pd.read_csv(csv_path)

    conn = sqlite3.connect(db_path)

    df.to_sql("livros", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    print(f"✅ Dados salvos com sucesso em '{db_path}'!")

if __name__ == "__main__":
    salvar_em_banco(CLEAN_PATH, DB_PATH)
