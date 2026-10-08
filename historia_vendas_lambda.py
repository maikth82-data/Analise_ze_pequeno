# Analise de vendas da empresa de Rolhas e Paçocas Zé Pequeno 

import pandas as pd 

df= pd.read_csv ('/Users/michaelthomazoniespiritosanto/Analise_ze_pequeno/tabela_vendas_zepequeno_LIMPA.csv')

print(df.head())

# transformando a coluna data que está em str npo formato datetime 

df['Data'] = pd.to_datetime(df['Data'])

print(df.dtypes)


# 1. Calculo o faturamento total por Produto:

faturamento_produto = df.groupby('Produto')['Valor_Venda'].apply(lambda x: x.sum()).reset_index()

faturamento_produto['Faturamento_Formatado'] = faturamento_produto['Valor_Venda'].apply(
    lambda valor: f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
)

print("--- FATURAMENTO POR PRODUTO ---")
print(faturamento_produto[['Produto', 'Faturamento_Formatado']])
print( "\n" 'O pruduto com maior faturamento para empresa sao as Rolhas que representam 54% do faturamento da empresa enquanto as Paçocas vem em segundo lugar com 43% do faturamento.')


# 2. Canal com a maior força de vendas

vendas_canal = df.groupby('Canal')['Valor_Venda'].agg([
    ('Qtd_Transacoes', 'count'),
    ('Total_Faturado', 'sum'),
    ('Ticket_Medio', 'mean')
]).reset_index()

vendas_canal['Total_Faturado_R$'] = vendas_canal['Total_Faturado'].apply(lambda x: f"R$ {x:,.2f}")
vendas_canal['Ticket_Medio_R$'] = vendas_canal['Ticket_Medio'].apply(lambda x: f"R$ {x:,.2f}")

print("\n - DESEMPENHO POR CANAL DE VENDA -")
print(vendas_canal[['Canal', 'Qtd_Transacoes', 'Total_Faturado_R$', 'Ticket_Medio_R$']])

print("\n -O E-commerce atua como o canal de maior valor por transação em relação ao ticket médio, sendo responsável pelo maior faturamento absoluto. -")



# 3. Bucando a quantidade de boas realizadas de acordo com limite 

LIMITE = 2000

df['Status'] = df['Valor_Venda'].apply(lambda x: 'Venda alta' if x > LIMITE else 'Venda Padrão')

boas_vendas = df['Status'].value_counts()

print("-CLASSIFICAÇÃO DAS BOAS VENDAS --")
print(boas_vendas)
print("\n os números de boas de vendas de acordo com o imite estipulado superaram as vendas consideradas padrão representando mais de 50% das vendas raalizadas")