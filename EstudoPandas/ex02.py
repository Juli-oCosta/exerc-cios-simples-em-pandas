import pandas as pd
from matplotlib import pyplot as plt

# DataFrame inicial
dados = {
    'Cliente': ['Carlos', 'Maria', 'João', 'Ana', 'Pedro'],
    'Compras': [3, 7, 2, 5, 4],
    'Valor Total': [500, 1200, 300, 800, 2500],
    'Frequência': [None, 'Alta', 'Baixa', 'Média', 'Alta'],
    'Última Compra': ['2025-01-05', '2025-01-01', '2025-01-10', '2025-01-03', '2025-01-02']
}
df = pd.DataFrame(dados)

# 1. Converta a coluna "Última Compra" para o tipo datetime.
df['Última Compra'] = pd.to_datetime(df['Última Compra'], errors='coerce')

# 2. Exiba o cliente com o maior valor total de compras.
cliente_maior_valor = df.loc[df['Valor Total'].idxmax()]
print("\nCliente com o maior valor total de compras.")
print(cliente_maior_valor)

# 3. Calcule a média do valor total das compras.
media_valor_total = df['Valor Total'].mean()
print(f"\nMedia de Valor total: {media_valor_total}")

# 4. Filtre e exiba os clientes com "Frequência" igual a "Alta".
tabela_filtrada = df[df['Frequência'] == 'Alta']
print("\nClientes com alta frequência.")
print(tabela_filtrada)

# 5. Adicione uma nova coluna chamada "Desconto" que aplique 10% de desconto ao valor total.
df['Desconto de 10%'] = df['Valor Total'] - ((df['Valor Total'] * 10) / 100)
print("\nAdicona nova coluna com 10% de desconto")
print(df)

# 6. Substitua valores nulos (se houver) na coluna "Frequência" por "Indefinida".
df['Frequência'] = df['Frequência'].fillna("Indefinida")
print("\nCaso exista, substituindo valores nulos em 'Frequência' por 'Indefinida'")
print(df)

# 7. Agrupe os clientes pela "Frequência" e calcule a soma do valor total para cada grupo.
soma_por_frequencia = df.groupby('Frequência')['Valor Total'].sum()
print("\nSoma do valor total por frequência.")  
print(soma_por_frequencia)

# 8. Crie uma nova coluna chamada "Compras Recentes" que seja True para compras realizadas após "2025-01-03".
df['Compras Recentes'] = df['Última Compra'].apply(lambda x: True if x > pd.to_datetime("2025-01-03") else False)
print("\nNova coluna verificando se compra recente ou não")
print(df)

# 9. Ordene os clientes pelo valor total em ordem decrescente.
tabela_ordenada = df.sort_values('Valor Total', ascending=False)
print("\nOrdenando valor total em decrescente.")
print(tabela_ordenada)

# 10. Exporte o DataFrame para um arquivo CSV chamado `clientes.csv`.
df.to_csv("arquivos_csv/clientes.csv", index=False)

# 11. Plote um gráfico de pizza mostrando a distribuição de clientes por "Frequência".
frequencia_contagem = df['Frequência'].value_counts()
plt.title("Distribuição de Clientes por Frequência")
frequencia_contagem.plot(kind='pie', autopct='%1.1f%%', startangle=90, legend=True)
plt.ylabel('')
plt.show()
