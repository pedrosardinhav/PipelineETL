# 🚀 ETL de Processamento de Vendas

Este projeto implementa um pipeline ETL (Extract, Transform, Load) em Python para processar dados de vendas.  
Ele lê um arquivo CSV, trata os dados, calcula valores derivados e gera um novo arquivo já processado.

---

## 📌 Funcionalidades

- Extração do arquivo `vendas.csv`
- Remoção de valores nulos
- Conversão de colunas numéricas
- Cálculo de valor total
- Formatação monetária em reais
- Cálculo de valor com imposto (10%)
- Geração do arquivo `vendas_processadas.csv`

---

## 📁 Estrutura Esperada do Projeto

📦 etl-vendas  
┣ 📄 vendas.csv  
┣ 📄 vendas_processadas.csv  
┣ 📄 seu_script.py  
┗ 📄 README.md  

---

## ▶️ Como Executar

1. Instale as dependências:
   `pip install pandas`

2. Coloque o arquivo `vendas.csv` na mesma pasta do script.

3. Execute o programa:
   `python seu_script.py`

4. O arquivo `vendas_processadas.csv` será criado automaticamente.

---

## 📝 Sobre o Projeto

Este projeto foi desenvolvido para estudo e prática de conceitos de ETL e manipulação de dados utilizando Python e Pandas.  
O fluxo segue o padrão clássico: **Extrair → Transformar → Carregar**, garantindo clareza e organização no processamento dos dados.
