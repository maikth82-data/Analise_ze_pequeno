# Analise_ze_pequeno

Analise de vendas para a atividade em grupo da disciplina de Modelagem de Dados SCTEC

Análise de Vendas — Zé Pequeno Paçocas e Rolhas Ltda.

Este repositório contém a análise de dados das vendas da Zé Pequeno Paçocas e Rolhas Ltda, uma empresa que utiliza o amendoim para a produção de paçoca e reaproveita as cascas para a fabricação de rolhas.

O projeto foi desenvolvido em **Python**, com utilização intensiva de **funções `lambda`** e manipulação de dataframes com **Pandas** para responder a perguntas do negócio levantadas pelo time comercial.

---

## Objetivos do Projeto

1. **Entender o desempenho de produtos:** Identificar qual linha de produtos (Paçoca ou Rolhas) gera maior faturamento e volume.
2. **Avaliar canais de distribuição:** Comparar a performance das vendas entre o **E-commerce** e a **Loja Física**.
3. **Higienizar e padronizar os dados:** Tratar inconsistências de texto, caixa alta/baixa, espaços extras e remover outliers de teste (`99999` e `999999`).

---

## Tecnologias e Bibliotecas Utilizadas

* **Python 3.x**
* **Pandas** (Tratamento, agrupamento e manipulação de dados)
* **OpenPyXL** (Leitura de arquivos Excel `.xlsx`)

---

## 🧹 Tratamento e Higienização dos Dados (`ETL`)

Antes do início das análises, os dados passaram por um processo rigoroso de limpeza:
* **Padronização de Categoria:** Unificação de divergências de digitação (`PAÇOCA`, `paçoca` $\rightarrow$ `Paçoca`; `loja física` $\rightarrow$ `Loja Física`; `JOINVILLE`, `blumenau` $\rightarrow$ `Joinville`, `Blumenau`).
* **Remoção de Outliers:** Exclusão de 5 registros inconsistentes com valores `R$ 99.999,00` e `R$ 999.999,00`, reduzindo a distorção da média do faturamento.
* **Formatos Decimais:** Arredondamento da coluna de valores para 2 casas decimais (`.round(2)`).

---

## Códigos e Funções Lambda Utilizadas

### 1. Faturamento por Produto

```python

faturamento_produto = df.groupby('Produto')['Valor_Venda'].apply(lambda x: x.sum()).reset_index()

faturamento_produto['Faturamento_Formatado'] = faturamento_produto['Valor_Venda'].apply(
    lambda valor: f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
)
print(faturamento_produto[['Produto', 'Faturamento_Formatado']])


