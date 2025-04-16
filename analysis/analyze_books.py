import pandas as pd
import matplotlib.pyplot as plt

CLEAN_PATH = "data/processed/livros_limpos.csv"

def analisar_dados(path):
    print("📊 Analisando dados...")
    df = pd.read_csv(path)

    # 1. Análise de distribuição de preços
    plt.figure(figsize=(10, 6))
    plt.hist(df["preco"].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title("Distribuição de Preços")
    plt.xlabel("Preço (£)")
    plt.ylabel("Número de Livros")
    plt.grid(True)
    plt.show()

    # 2. Análise de distribuição de avaliações
    plt.figure(figsize=(10, 6))
    df["avaliacao"].value_counts().sort_index().plot(kind="bar", color='lightgreen', edgecolor='black')
    plt.title("Distribuição de Avaliações")
    plt.xlabel("Avaliação")
    plt.ylabel("Número de Livros")
    plt.xticks(rotation=0)
    plt.show()

    # 3. Relação entre preço e avaliação
    plt.figure(figsize=(10, 6))
    df.plot(kind="scatter", x="preco", y="avaliacao", color='orange')
    plt.title("Relação entre Preço e Avaliação")
    plt.xlabel("Preço (£)")
    plt.ylabel("Avaliação")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    analisar_dados(CLEAN_PATH)
