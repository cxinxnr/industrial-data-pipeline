import pandas as pd

RAW_PATH = "data/raw/livros.csv"
CLEAN_PATH = "data/processed/livros_limpos.csv"

def limpar_dados(path):
    print("🧹 Limpando os dados...")
    df = pd.read_csv(path)

    print(f"📊 Dados brutos: {df.shape[0]} linhas")

    df.drop_duplicates(inplace=True)

    df["preco"] = df["preco"].str.replace("£", "", regex=False)
    df["preco"] = df["preco"].str.replace(r"[^\d.]", "", regex=True)  # remove qualquer caractere não numérico
    df["preco"] = pd.to_numeric(df["preco"], errors="coerce")  # converter para numérico, e gerar NaN para erros

    df["titulo"] = df["titulo"].str.lower().str.strip()
    df["avaliacao"] = df["avaliacao"].str.lower()

    df = df[df["link"].str.startswith("http")]

    print(f"✅ Dados limpos: {df.shape[0]} linhas")
    return df

if __name__ == "__main__":
    df_limpo = limpar_dados(RAW_PATH)
    df_limpo.to_csv(CLEAN_PATH, index=False)
    print(f"💾 Arquivo limpo salvo em: {CLEAN_PATH}")
