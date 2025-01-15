import pandas as pd
from matplotlib import pyplot as plt

# Criação do DataFrame
dados = {
    'Produto': ['Celular', 'Notebook', 'Tablet', 'Monitor', 'Teclado', 'Cabo HDMI', 'Mouse', 'Impressora'],
    'Categoria': ['Eletrônicos', 'Eletrônicos', 'Eletrônicos', 'Periféricos', 'Periféricos', 'Acessórios', 'Acessórios', 'Periféricos'],
    'Preço Unitário': [1500, 3000, 1200, None, 200, 50, 100, 800],
    'Quantidade': [10, 5, None, 12, 15, 30, 50, None],
    'Fornecedor': ['A', 'B', 'C', None, 'E', 'F', 'G', 'H'],
    'Data Última Compra': ['2025-01-01', '2024-12-20', None, '2025-01-10', '2024-11-30', '2024-10-15', None, '2024-12-01']
}

df = pd.DataFrame(dados)

# Convertendo datas
df['Data Última Compra'] = pd.to_datetime(df['Data Última Compra'], errors='coerce')

print("Tabela de produtos em estoque:")
print(df)

# 1. Preencha os valores ausentes na coluna "Preço Unitário" com a média dos preços disponíveis.
media_preços = df['Preço Unitário'].mean()
df['Preço Unitário'] = df['Preço Unitário'].fillna(media_preços)
print("\nDataFrame com valores ausentes na coluna 'Preço Unitário' preenchidos com a média:")
print(df)

# 2. Preencha os valores ausentes na coluna "Quantidade" com zero, indicando que não há estoque atual para esses produtos.
df['Quantidade'] = df['Quantidade'].fillna(0)
print("\nDataFrame com valores ausentes na coluna 'Quantidade' preenchidos com 0(zero):")
print(df)

# 3. Encontre e exiba o produto com o preço unitário mais alto.

# 4. Calcule o valor total de estoque (multiplicação de preço unitário por quantidade) e adicione uma nova coluna chamada "Valor Estoque".
df['Valor Estoque'] = df['Preço Unitário'] * df['Quantidade']
print("\nAdiciona coluna com valor total de estoque.")
print(df)

# 5. Substitua os valores ausentes na coluna "Fornecedor" pelo texto "Desconhecido".
df['Fornecedor'] = df['Fornecedor'].fillna('Desconhecido')
print("\nSubstitui valores nulos em fornecedor por 'Desconhecido'")
print(df)

# 6. Identifique os produtos que não têm data de última compra registrada e exiba seus nomes.
produtos_sem_data = df[df['Data Última Compra'].isna()]
print("\nProdutos sem data de última compra registrada:")
print(produtos_sem_data['Produto'])

# 7. Filtre os produtos cuja categoria seja "Eletrônicos" e o valor total de estoque seja superior a 10.000.
tabela_filtrada = df[(df['Categoria'] == 'Eletrônicos') & (df['Valor Estoque'] > 10000)]
print("\nTabela filtrada para eletrônicos com valor total de estoque > 10000.")
print(tabela_filtrada)

# 8. Adicione uma nova coluna chamada "Status Estoque", com as seguintes condições:
#    - 'Estoque Baixo' para produtos com quantidade menor que 10.
#    - 'Estoque Médio' para produtos com quantidade entre 10 e 20 (inclusive).
#    - 'Estoque Alto' para produtos com quantidade maior que 20.
def classificar_estoque(quantidade):
    if quantidade < 10:
        return 'Estoque Baixo'
    elif quantidade <= 20:
        return  'Estoque Médio'
    else:
        return 'Estoque Alto'
    
df['Status Estoque'] = df['Quantidade'].apply(classificar_estoque)
print("\nAdiciona colina com status de estoque.")
print(df)

# 9. Classifique os produtos em ordem decrescente de "Valor Estoque".
tabela_ordenada = df.sort_values('Valor Estoque', ascending=False)
print("\nTabela ordenada por valor em estoque decrescente.")
print(tabela_ordenada)

# 10. Crie um gráfico de barras mostrando o valor total de estoque por categoria.
estoque_categoria = df.groupby('Categoria')['Valor Estoque'].sum()
plt.title("Valor de Estoque por Categoria")
estoque_categoria.plot(kind='bar',x='Categoria',y='Valor Estoque')
plt.show()

df.to_csv("arquivos_csv/produtos3.csv", index=False)