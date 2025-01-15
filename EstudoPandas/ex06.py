import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
import math

dados = {
    'Funcionário': ['Alice', 'Bruno', 'Clara', 'Diego', 'Elisa'],
    'Departamento': ['RH', 'TI', 'TI', 'Financeiro', 'RH'],
    'Salário': [4000, 5000, 4500, 6000, 3500],
    'Idade': [30, 28, 35, 40, 25],
    'Contratado em': ['2020-05-10', '2019-08-15', '2021-01-12', '2018-07-23', '2022-11-01']
}

df = pd.DataFrame(dados)

df['Contratado em'] = pd.to_datetime(df['Contratado em'])

# 1. Exiba os funcionários com salário acima de 4500.
funcionarios_acima_4500 = df[df['Salário'] > 4500]
print("\nFuncionario com salário > 4500.")
print(funcionarios_acima_4500)

# 2. Crie uma nova coluna "Faixa Etária" que categoriza os funcionários em 'Jovem', 'Meia-idade' e 'Sênior' baseado na idade.
def faixa_etaria(idade):
    if idade <= 30:
        return 'Jovem'
    elif idade <= 45:
        return 'Meia-idade'
    else:
        return 'Sênior'
    
df['Faixa Etária'] = df['Idade'].apply(faixa_etaria)
print("\nAdiciona coluna com faixa etária.")
print(df)

# 3. Calcule a média salarial por departamento.
media_salarial = df.groupby('Departamento')['Salário'].mean()
print("\nMédia salarial por departamento.")
print(media_salarial)

# 4. Calcule a diferença de anos entre a data de contratação e a data atual e adicione uma nova coluna "Anos na Empresa".
data_atual = datetime.now()
df['Anos na Empresa'] = ((data_atual - df['Contratado em']).dt.days / 365).apply(math.trunc)
print("Adiciona nova coluna com anos trabalhados na empresa")
print(df)

# 5. Crie uma nova coluna "Faixa Salarial" que categorize os salários em 'Baixo', 'Médio' e 'Alto'.
def faixa_salarial(salario):
    if salario < 4000:
        return 'Baixo'
    elif salario <= 6000:
        return 'Médio'
    else:
        return 'Alto'

df['Faixa Salarial'] = df['Salário'].apply(faixa_salarial)
print("\nAdciona coluna de faixa salarial")
print(df) 

# 6. Filtre os funcionários do departamento 'TI' e exiba apenas aqueles com salário superior a 4500.
funcionarios_filtrados = df[(df['Departamento'] == 'TI') & (df['Salário'] > 4500)]
print("\nTI com salário > 4500")
print(funcionarios_filtrados)

# 7. Exiba o funcionário com a maior idade.
funcionario_mais_velho = df.loc[df['Idade'].idxmax()]
print("\nFuncionário mais velho.")
print(funcionario_mais_velho)

# 8. Plote um gráfico de barras mostrando o salário médio por departamento.
salario_medio_por_departamento = df.groupby('Departamento')['Salário'].mean()
plt.title("Salário médio por departamento")
salario_medio_por_departamento.plot(kind='bar',x='Funcionário',y='Departamento')
plt.show()

# 9. Ordene os funcionários por idade em ordem crescente.
tabela_ordenada = df.sort_values('Idade', ascending=True)
print("\nTabela ordenada por idade crescente.")
print(tabela_ordenada)

# 10. Exporte o DataFrame para arquivos CSV e XLSX chamado `funcionarios.csv`.
df.to_csv("arquivos_csv/funcionarios.csv", index=False)
df.to_excel("arquivos_excel/funcionarios2.xlsx", index=False)