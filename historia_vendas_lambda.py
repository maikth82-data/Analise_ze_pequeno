# Analise de vendas da empresa de Rolhas e Paçocas Zé Pequeno 

import pandas as pd 

df= pd.read_csv ('/Users/michaelthomazoniespiritosanto/Analise_ze_pequeno/tabela_vendas_zepequeno_LIMPA.csv')

print(df.head())

# transformando a coluna data que está em str npo formato datetime 

df['Data'] = pd.to_datetime(df['Data'])

print(df.dtypes)


# 1. Calcular o faturamento total por Produto:

faturamento_produto = df.groupby('Produto')['Valor_Venda'].apply(lambda x: x.sum()).reset_index()

faturamento_produto['Faturamento_Formatado'] = faturamento_produto['Valor_Venda'].apply(
    lambda valor: f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
)

print("--- FATURAMENTO POR PRODUTO ---")
print(faturamento_produto[['Produto', 'Faturamento_Formatado']])
print( "\n" '-- O pruduto com maior faturamento para empresa sao as Rolhas que representam 54% do faturamento da empresa enquanto as Paçocas vem em segundo lugar com 43% do faturamento.--')