import pandas as pd
from matplotlib import pyplot as plt

dados = {
    'Produto': ['Celular', 'Notebook', 'Tablet', 'Monitor', 'Teclado', 'Cabo', 'Mouse'],
    'Preço': [1500, 3000, 1200, 800, 200, 50, 100],
    'Quantidade': [10, 5, 8, 12, 15, 30, 50],
    'Categoria': ['Eletrônicos', 'Eletrônicos', 'Eletrônicos', 'Periféricos', 'Periféricos', 'Acessórios', 'Acessórios'],
    'Fornecedor': ['Fornecedor A', None, None, 'Fornecedor D', 'Fornecedor E', 'Fornecedor F', 'Fornecedor G']
}

df = pd.DataFrame(dados)

# 1. Exiba os 5 primeiros produtos do DataFrame.
print("\nTabela apresentando apenas os 5 primeiros produtos.")
print(df['Produto'].head(5))

# 2. Filtre e exiba os produtos da categoria "Acessórios".
tabela_filtrada = df[df['Categoria'] == 'Acessórios']
print('\nFiltrando categoria acessórios.')
print(tabela_filtrada)

# 3. Calcule o valor total de estoque (Preço * Quantidade) para cada produto e adicione como uma nova coluna chamada "Valor Total".
df['Valor Total'] = df['Preço'] * df['Quantidade']
print("\nAdiciona nova coluna com valor total por produto.")
print(df)

# 4. Substitua os valores nulos (se houver) na coluna "Fornecedor" por "Fornecedor indefinido".
df['Fornecedor'] = df['Fornecedor'].fillna('Fornecedor Indefinido')
print("\nCaso exista, substituindo valores nulos em 'Fornecedor' por 'Fornecedor Indefinido'.")
print(df)

# 5. Agrupe os produtos por "Categoria" e calcule a soma total dos estoques (Quantidade) para cada categoria.
tabela_agrupada = df.groupby('Categoria')['Quantidade'].sum()
print("\nAgrupando por Categoria e calculando soma da quantidade.")
print(tabela_agrupada)

# 6. Crie uma nova coluna chamada "Produto Popular" que seja True para produtos com quantidade maior que 20 e False caso contrário.
df['Produto Popular'] = df['Quantidade'].apply(lambda x: True if x > 20 else False)
print("\nAdiciona coluna com popular ou não.")
print(df)

# 7. Filtre os produtos cujo valor total de estoque seja superior a 10000.
tabela_filtrada = df[df['Valor Total'] > 10000]
print("\nFiltrado por Valor total > 10000.")
print(tabela_filtrada)

# 8. Ordene o DataFrame pelo preço de forma crescente.
ordenacao_por_preco = df.sort_values('Preço', ascending=True)
print("\nOrdena por preço de forma crescente.")
print(ordenacao_por_preco)

# 9. Exporte o DataFrame para um arquivo CSV chamado `produtos.csv`.
df.to_csv("arquivos_csv/produtos2.csv", index=False)

# 10. Plote um gráfico de barras mostrando o valor total de estoque por categoria.
valor_estoque = df.groupby('Categoria')['Valor Total'].sum()
plt.title("Valor total por categoria")
valor_estoque.plot(kind='bar',x='Valor Total',y='Catgegoria')
plt.show()