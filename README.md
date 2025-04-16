# 🏭 Industrial Data Pipeline

Projeto desenvolvido com foco em **coleta, limpeza, análise e armazenamento de dados** para fins educativos.
## 📌 Objetivo

Simular um pipeline de dados completo, extraindo informações de produtos , tratando os dados, realizando análises simples e armazenando em banco de dados.

---

## ⚙️ Funcionalidades

- 🔍 Web scraping de dados de um site simulado
- 🧹 Limpeza e padronização dos dados
- 📊 Análise estatística descritiva
- 🗃️ Armazenamento em SQLite
- 🔁 Pipeline automatizado via `main.py`

---

## 🧰 Tecnologias utilizadas

- Python 3.11
- `requests`, `BeautifulSoup4` – Web Scraping
- `pandas` – Manipulação de dados
- `sqlite3` – Banco de dados local
- `matplotlib` – Visualização (gráficos)
- `venv` – Ambiente virtual

---

## 🚀 Como executar

Clone o repositório:

```bash
git clone https://github.com/cxinxnr/industrial-data-pipeline.git
cd industrial-data-pipeline
```

Crie o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate    # (Windows)
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o pipeline completo:

```bash
python main.py
```

---

## 📁 Estrutura de Pastas

```
industrial-data-pipeline/
│
├── main.py                   # Pipeline completa
├── scraper/                  # Coleta de dados
│   └── scraper.py
├── cleaner/                  # Limpeza de dados
│   └── clean_books_data.py
├── analyzer/                 # Análise e visualização
│   └── analyze_books_data.py
├── database/                 # Armazenamento
│   └── save_to_db.py
├── data/                     # Dados brutos e tratados
│   ├── raw/
│   ├── processed/
├── requirements.txt
└── README.md
```

