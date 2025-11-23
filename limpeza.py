import os
print("Arquivos na pasta atual:", os.listdir())
import pandas as pd
#E
def extrair_dados():
    df = pd.read_csv("vendas.csv")
    return df

#T
def transformar_dados(df):
    df = df.dropna()
    df["valor"] = df["valor"].astype(float)
    df["quantidade"] = df["quantidade"].astype(float)    
    df["valor_total"] = df["valor"] * df["quantidade"]    
    df["valor_total"] = df["valor_total"].apply(lambda x: f"R${x:,.2f}")   
    df["valor_com_imposto"] = df["valor_total"] * 1.10    
    df["valor_com_imposto"] = df["valor_com_imposto"].apply(lambda x: f"R${x:,.2f}")
    return df

#L
def carregar_dados(df):
    df.to_csv("vendas_processadas.csv", index=False)
    print("✅ Dados processados e salvos com sucesso!")


def pipeline():
    dados = extrair_dados()
    dados = transformar_dados(dados)
    carregar_dados(dados)


pipeline()
