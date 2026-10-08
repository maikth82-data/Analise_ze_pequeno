# Analise_ze_pequeno

**Analise de vendas para a atividade em grupo da disciplina de Modelagem de Dados SCTEC** 

Análise de Vendas — Zé Pequeno Paçocas e Rolhas Ltda.

Este repositório contém a análise de dados das vendas da Zé Pequeno Paçocas e Rolhas Ltda, uma empresa que utiliza o amendoim para a produção de paçoca e reaproveita as cascas para a fabricação de rolhas.

O projeto foi desenvolvido em **Python**, com utilização intensiva de **funções `lambda`** e manipulação de dataframes com **Pandas** para responder a perguntas do negócio levantadas pelo time comercial.

---

## Objetivos do Projeto

1. **Entender o desempenho de produtos:** Identificar qual linha de produtos (Paçoca ou Rolhas) gera maior faturamento e volume.
2. **Avaliar canais de distribuição:** Comparar a performance das vendas entre o **E-commerce** e a **Loja Física**.
3. **Classificação das vendas:** Verificar a quantidade de vendas que pode ser considerada de ticket alto e as vendas padrão de acordo com o limite estipulado


---

## Tecnologias e Bibliotecas Utilizadas

* **Python 3.x**
* **Pandas** (Tratamento, agrupamento e manipulação de dados)
* **OpenPyXL** (Leitura de arquivos Excel `.xlsx`)

---

## Tratamento e Higienização dos Dados

Antes do início das análises, os dados passaram por um processo rigoroso de limpeza:
* **Padronização de Categoria:** Unificação de divergências de digitação nas colunas Proudto, Canal e Região.
* **Remoção de Outliers:** Exclusão de 5 registros inconsistentes com valores `R$ 99.999,00` e `R$ 999.999,00`, reduzindo a distorção da média do faturamento.
* **Formatos Decimais:** Arredondamento da coluna de valores para 2 casas decimais.

---

## Códigos e Funções Lambda Utilizadas

# 1. Calculo o faturamento total por Produto:

faturamento_produto = df.groupby('Produto')['Valor_Venda'].apply(lambda x: x.sum()).reset_index()

faturamento_produto['Faturamento_Formatado'] = faturamento_produto['Valor_Venda'].apply(
    lambda valor: f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

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

---

## Como Executar o Projeto:

**Clone o repositório:**

git clone https://github.com/maikth82-data/Analise_ze_pequeno.git

 **Instale as dependências se necessárias:**

pip install pandas 
pip isntall openpyxl

**Execute o script principal em Python:**

historia_vendas_lambda.py

**Se necessário carregue o arquivo no script indicando a pasta de origem**

 Exemplo:

df= pd.read_csv ('/Users/michaelthomazoniespiritosanto/Analise_ze_pequeno/tabela_vendas_zepequeno_LIMPA.csv')
