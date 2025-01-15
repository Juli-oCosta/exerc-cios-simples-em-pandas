import pandas as pd
from matplotlib import pyplot as plt

dados = {
    'Produto': ['Celular', 'Notebook', 'Tablet', 'Monitor', 'Teclado'],
    'Preço': [1500, 3000, 1200, None, 200],
    'Quantidade': [10, 5, 8, 12, 15],
    'Categoria': ['Eletrônicos', 'Eletrônicos', 'Eletrônicos', 'Periféricos', 'Periféricos']
}
df = pd.DataFrame(dados)

# 1. Exiba as 3 primeiras linhas do DataFrame.
print("\nTabela apresentando apenas as 3 primeiras linhas.")
print(df.head(3))

# 2. Filtre e exiba apenas os produtos da categoria "Periféricos".
tabela_filtrada = df[df['Categoria'] == 'Periféricos']
print("\nTabela filtrada exibindo apenas produtos na categoria'Periféricos'.")
print(tabela_filtrada)

# 3. Calcule o valor total de estoque (Preço * Quantidade) para cada produto e adicione como uma nova coluna.
df['Valor total'] = df['Preço'] * df['Quantidade']
print("\nAdiciona nova coluna 'Valor total'")
print(df)

# 4. Substitua os valores nulos (se houver) na coluna "Preço" pela média dos preços.
media_preco = df['Preço'].mean()
df['Preço'] = df['Preço'].fillna(media_preco)
print("\nCaso exista, substituindo valores nulos em 'Preço' pela média")
print(df)

# 5. Agrupe os produtos por "Categoria" e calcule a soma total dos estoques (Quantidade).
soma_estoques = df.groupby('Categoria')['Quantidade'].size()
print("\nAgrupando por Categoria e calculando soma total dos estoques.")
print(soma_estoques)

# 6. Crie uma nova coluna chamada "Produto Premium" que seja True para preços acima de 2000 e False caso contrário.
df['Produto Premium'] = df['Preço'].apply(lambda x: True if pd.notna(x) and x > 2000 else False)
print("\nCriando coluna premium para preços acima de 2000")
print(df)

# 7. Exporte o DataFrame para um arquivo CSV chamado `produtos.csv`.
df.to_csv("arquivos_csv/produtos.csv", index=False)

# 8. Ordene o DataFrame pelo preço em ordem decrescente.
ordenado_por_preco = df.sort_values('Preço', ascending=False)
print("\nOrdenando por Preço em decrescente.")
print(ordenado_por_preco)

# 9. Filtre os produtos cujo valor total de estoque seja maior que 5000.
filtrada_por_valor = df[df['Valor total'] > 5000]
print("\nValor total maior que 5000.")
print(filtrada_por_valor)

# 10. Plote um gráfico de barras mostrando a quantidade de produtos por categoria.
categoria_quantidade = df.groupby('Categoria')['Quantidade'].sum()
plt.title("Produtos por categoria")
categoria_quantidade.plot(kind='bar',x='Categoria',y='Quantidade')
plt.show()