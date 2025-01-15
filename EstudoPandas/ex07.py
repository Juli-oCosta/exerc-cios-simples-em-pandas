import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime, timedelta

# Dados iniciais para criar os DataFrames:
dados_vendas = {
    'Vendedor': ['Alice', 'Bruno', 'Clara', 'Diego', 'Elisa', 'Fábio', 'Gustavo'],
    'Região': ['Norte', 'Sul', 'Sul', 'Norte', 'Leste', 'Oeste', 'Leste'],
    'Vendas': [3000, 4500, 5200, 3100, 2800, 4000, 4100],
    'Data': ['2025-01-05', '2025-01-04', '2025-01-03', '2025-01-06', '2025-01-07', '2025-01-08', '2025-01-09']
}
df_vendas = pd.DataFrame(dados_vendas)

df_vendas['Data'] = pd.to_datetime(df_vendas['Data'], errors='coerce')

dados_clientes = {
    'Cliente': ['João', 'Maria', 'Pedro', 'Ana', 'Luiza', 'Carlos', 'Beatriz'],
    'Compras': [5, 7, 2, 10, 4, 3, 6],
    'Gasto Total': [1500, 2100, 800, 3200, 1200, 950, 1800],
    'Região': ['Norte', 'Sul', 'Sul', 'Norte', 'Leste', 'Oeste', 'Leste']
}
df_clientes = pd.DataFrame(dados_clientes)

# 1. Exiba o total de vendas por região.
df_vendas_total_por_vendas = df_vendas.groupby('Região')['Vendas'].sum()
print("\nTotal de vendas por região.")
print(df_vendas_total_por_vendas)

# 2. Calcule o ticket médio (gasto médio por cliente) de cada região.
df_clientes_gasto_medio = df_clientes.groupby('Região')['Gasto Total'].mean()
print("\nGasto médio por clientes de cada região.")
print(df_clientes_gasto_medio)

# 3. Adicione uma nova coluna ao DataFrame de vendas chamada "Comissão (5%)", calculando 5% das vendas.
df_vendas['Comissão'] = (df_vendas['Vendas'] * 5) / 100
print("\nAdiciona tabela com comissão de 5%.")
print(df_vendas)

# 4. Filtre apenas os vendedores que realizaram vendas acima de 4000.
vendas_acima_4000 = df_vendas[df_vendas['Vendas'] > 4000]
print("\nVendedores com vendas acima de 4000:")
print(vendas_acima_4000)

# 5. Crie uma nova coluna no DataFrame de clientes chamada "Frequência", categorizando clientes com base no número de compras:
# 'Baixa' (1-3), 'Média' (4-6) e 'Alta' (7+).
def classificar_frequencia(compras):
    if compras <= 3:
        return 'Baixa'
    elif compras <= 6:
        return 'Média'
    else:
        return 'Alta'

df_clientes['Frequência'] = df_clientes['Compras'].apply(classificar_frequencia)
print("\nDataFrame de clientes com frequência:")
print(df_clientes)

# 6. Combine os DataFrames de vendas e clientes usando a coluna 'Região' como base.
df_combinado = pd.merge(df_vendas, df_clientes, on='Região', how='inner')
print("\nDataFrame combinado (vendas e clientes):")
print(df_combinado)

# 7. Calcule a soma das vendas e do gasto total para cada região no DataFrame combinado.
soma_vendas_gastos = df_combinado.groupby('Região')[['Vendas', 'Gasto Total']].sum()
print("\nSoma de vendas e gastos totais por região:")
print(soma_vendas_gastos)

# 8. Ordene o DataFrame de vendas em ordem decrescente pelo valor das vendas.
df_vendas_ordenado = df_vendas.sort_values('Vendas', ascending=False)
print("\nDataFrame de vendas ordenado por vendas decrescentemente:")
print(df_vendas_ordenado)

# 9. Adicione uma coluna ao DataFrame de vendas indicando se a venda foi realizada no final de semana.
df_vendas['Final de Semana'] = df_vendas['Data'].dt.weekday.isin([5, 6])
print("\nDataFrame de vendas com indicação de final de semana:")
print(df_vendas)

# 10. Plote um gráfico de barras mostrando o total de vendas por vendedor.
vendas_por_vendedor = df_vendas.groupby('Vendedor')['Vendas'].sum()
plt.title("Vendas por vendedor")
vendas_por_vendedor.plot(kind='bar',x='Vendedor',y='Vendas')
plt.show()

df_clientes.to_csv("arquivos_csv/clientes3.csv", index=False)
df_vendas.to_csv("arquivos_csv/vendas.csv", index=False)