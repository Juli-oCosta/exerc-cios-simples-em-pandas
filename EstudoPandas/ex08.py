import pandas as pd
import numpy as np

# Dados fictícios sobre funcionários e projetos
dados = {
    'Funcionário': ['Alice', 'Bruno', 'Clara', 'Diego', 'Elisa'],
    'Departamento': ['TI', 'TI', 'RH', 'Financeiro', 'RH'],
    'Salário': [5000, 4500, 4000, 6000, 3500],
    'Projetos': [3, 2, 5, 1, 4],
    'Horas Semanais': [40, 35, 45, 20, 30],
    'Data Contratação': ['2019-08-15', '2020-05-10', '2018-07-23', '2021-01-12', '2022-11-01']
}

df = pd.DataFrame(dados)

df['Data Contratação'] = pd.to_datetime(df['Data Contratação'], errors='coerce')

# 1. Crie uma nova coluna chamada "Carga de Trabalho" que classifique os funcionários em 'Alta', 'Média' ou 'Baixa' 
# com base nas horas semanais:
# - 'Alta' para horas acima de 40
# - 'Média' para horas entre 30 e 40 (inclusive)
# - 'Baixa' para horas abaixo de 30
def classificar_carga(horas):
    if horas > 40:
        return 'Alta'
    elif horas >= 30:
        return 'Média'
    else:
        return 'Baixa'
    
df['Carga de Trabalho'] = df['Horas Semanais'].apply(classificar_carga)
print("\nDataFrame com carga de trabalho.")
print(df)

# 2. Calcule o número total de projetos por departamento.
total_projetos = df.groupby('Departamento')['Projetos'].sum()
print("\nTotal de projetos por departamento.")
print(total_projetos)

# 3. Adicione uma nova coluna chamada "Eficiência" que calcula a média de horas trabalhadas por projeto 
# para cada funcionário ('Horas Semanais' por 'Projetos').
df['Eficiência'] = (df['Horas Semanais'] / df['Projetos']).round()
print("\nAdiciona coluna 'Eficiência' que calcula horas semanais dividido por projetos.")
print(df)

# 4. Plote um gráfico de barras que mostre o total de horas semanais trabalhadas por departamento.

# 5. Encontre o funcionário mais antigo na empresa (baseando-se na "Data Contratação").
indice_funcionario_mais_antigo = df['Data Contratação'].idxmin()
funcionario_mais_antigo = df.loc[indice_funcionario_mais_antigo]
print("\nFuncionário mais antigo.")
print(funcionario_mais_antigo)

# 6. Filtre os funcionários que têm mais de 3 projetos e estão no departamento de RH.
df_filtrada_por_projetos = df[(df['Projetos'] > 3) & (df['Departamento'] == 'RH')]
print("\nFuncionários com mais de 3 projetos no departamento de RH.")
print(df_filtrada_por_projetos)

# 7. Salve o DataFrame resultante com as colunas atualizadas em um arquivo CSV chamado "funcionarios_projetos.csv".
df.to_csv("arquivos_csv/funcionarios_projetos.csv", index=False)