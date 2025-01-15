import pandas as pd

# Dados de exemplo:
dados = {
    'Funcionario': ['Lucas', 'Mariana', 'Pedro', 'Carla', 'João'],
    'Departamento': ['TI', 'RH', 'Financeiro', 'TI', 'RH'],
    'Salario': [3500, 5000, 4000, 4500, 3000],
    'Data Contratacao': ['2015-06-01', '2018-08-15', '2020-01-12', '2019-05-30', '2022-09-10'],
    'Horas Semanais': [40, 35, 40, 38, 30],
    'Projetos': [5, 3, 2, 4, 1]
}

df = pd.DataFrame(dados)
df['Data Contratacao'] = pd.to_datetime(df['Data Contratacao'], errors='coerce')

# 1. Filtre os funcionários que têm um salário superior a 4000 e trabalham mais de 35 horas semanais.
df_filtrado_salario_horas = df[(df['Salario'] > 4000) & (df['Horas Semanais'] > 35)]
print("\nFuncionários com salário > 4000 e horas semanais > 35.")
print(df_filtrado_salario_horas)

# 2. Crie uma nova coluna chamada "Bonus" que calcula 10% do salário de cada funcionário como bônus.
df['Bonus'] = (df['Salario'] * 10) / 100
print("\nCria nova coluna que calcula bônus de 10%.")
print(df)

# 3. Encontre a média de horas semanais de todos os funcionários.
media_horas = df.groupby('Funcionario')['Horas Semanais'].mean()
print("\nMédia de horas semanais por funcionário.")
print(media_horas)

# 4. Crie uma coluna chamada "Anos de Empresa" que calcule o número de anos desde a contratação de cada funcionário.
df['Anos de Empresa'] = (pd.to_datetime('today') - df['Data Contratacao']).dt.days // 365
print("\nAdiciona coluna 'Anos de Empresa' com o número de anos desde a contratação.")
print(df)

# 5. Calcule o número total de projetos executados por todos os funcionários.
projetos_totais = df['Projetos'].sum()
print(f"\nTotal de projetos por funcionários: {projetos_totais}")

# 6. Exiba o nome do funcionário com o maior número de projetos.
# Encontra o maior número de projetos
maior_numero_projetos = df['Projetos'].max()

# Filtra o(s) funcionário(s) com esse número de projetos
funcionario_maior_projeto = df[df['Projetos'] == maior_numero_projetos]['Funcionario']
print(f"\nFuncionário(s) com o maior número de projetos: {funcionario_maior_projeto.to_string(index=False)}")

# 7. Encontre a soma total de salários por departamento.
soma_salario_por_departamento = df.groupby('Departamento')['Salario'].sum()
print("\nTotal de salário por departamento.")
print(soma_salario_por_departamento)

# 8. Ordene os funcionários por "Salario" de forma descendente.
tabela_ordenada = df.sort_values('Salario', ascending=False)
print("\nOrdenado por salário de forma decrescente.")
print(tabela_ordenada)

# 9. Encontre o funcionário mais recente na empresa (com base na "Data Contratacao").
funcionario_mais_recente = df.loc[df['Data Contratacao'].idxmax()]['Funcionario']
print("\nFuncionário mais recente na empresa:", funcionario_mais_recente)

# 10. Adicione uma nova coluna chamada "Eficiência" que calcula a média de horas semanais por projeto para cada funcionário.
df['Eficiência'] = (df['Horas Semanais'] / df['Projetos']).round()
print("\nAdicona coluna de eficiência.")
print(df)