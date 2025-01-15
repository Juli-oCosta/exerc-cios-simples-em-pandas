import pandas as pd
from matplotlib import pyplot as plt

dados = {
    'Cliente': ['Carlos', 'Maria', 'João', 'Ana', 'Pedro'],
    'Compras': [3, 7, 2, 5, 4],
    'Valor Total': [500, 1200, 300, 800, 600],
    'Frequência': ['Baixa', 'Alta', 'Baixa', 'Média', 'Média'],
    'Última Compra': ['2025-01-05', '2025-01-01', '2025-01-10', '2025-01-03', '2025-01-02']
}

df = pd.DataFrame(dados)

# 1. Exiba o cliente com o maior valor total de compras.
cliente_maior_valor_total = df.loc[df['Valor Total'].idxmax()]
print("\ncliente com maior valor em compras")
print(cliente_maior_valor_total)

# 2. Converta a coluna "Última Compra" para o tipo datetime.
df['Última Compra'] = pd.to_datetime(df['Última Compra'])

# 3. Calcule a soma total das compras de todos os clientes.
soma_total = df['Compras'].sum()
print(f"\nSoma total de compras: {soma_total}")

# 4. Crie uma nova coluna chamada "Desconto" que aplique 10% de desconto ao valor total de compras de cada cliente.
df['Desconto de 10%'] = df['Valor Total'] - ((df['Valor Total'] * 10) / 100)
print(f"\nAdiciona coluna com 10% de deconto.")
print(df)

# 5. Adicione uma coluna "Compras recentes" que seja True para clientes que realizaram compras após "2025-01-03" e False caso contrário.
df['Compras recentes'] = df['Última Compra'].apply(lambda x: True if x > pd.to_datetime("2025-01-03") else False)
print("\nAdiciona coluna de compras recentes")
print(df)

# 6. Agrupe os clientes pela "Frequência" e calcule a soma do valor total para cada grupo.
tabela_agrupada = df.groupby('Frequência')['Valor Total'].sum()
print("\nAgrupa por frequência e calcula soma de Valor Total")
print(tabela_agrupada)

# 7. Exiba os 3 clientes com maior número de compras.
top_3_compras = df.sort_values(by='Compras', ascending=False).head(3)
print("\nExibe os 3 clientes com as maiores compras")
print(top_3_compras)

# 8. Crie um gráfico de pizza mostrando a distribuição de clientes por "Frequência".
frequencia_contagem = df['Frequência'].value_counts()
plt.title("Distribuição de Clientes por Frequência")
frequencia_contagem.plot(kind='pie', autopct='%1.1f%%', startangle=90, legend=True)
plt.ylabel('')
plt.show()

# 9. Ordene os clientes pelo "Valor Total" em ordem decrescente.
tabela_ordenada = df.sort_values('Valor Total', ascending=False)
print("\nOrdenado por Valor Total crescente.")
print(tabela_ordenada)

# 10. Exporte o DataFrame para um arquivo CSV chamado `clientes.csv`.
df.to_csv("arquivos_csv/clientes2.csv")