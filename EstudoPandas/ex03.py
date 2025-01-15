import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import math

# DataFrame inicial
dados = {
    'Funcionário': ['Alice', 'Bruno', 'Clara', 'Diego', 'Elisa'],
    'Departamento': ['RH', 'TI', 'TI', None, 'RH'],
    'Salário': [4000, 5000, 4500, 6000, 3500],
    'Idade': [30, 28, 35, 40, 25],
    'Contratado em': ['2020-05-10', '2019-08-15', '2021-01-12', '2018-07-23', '2022-11-01']
}
df = pd.DataFrame(dados)

# 1. Converta a coluna "Contratado em" para o tipo datetime.
df['Contratado em'] = pd.to_datetime(df['Contratado em'], errors='coerce')

# 2. Calcule a idade média dos funcionários.
idade_media = df['Idade'].mean()
print(f"\nIdade média: {idade_media}")

# 3. Filtre os funcionários do departamento "TI" com salário acima de 4500.
funcionarios_filtrados = df[(df['Departamento'] == 'TI') & (df['Salário'] > 4500)]
print("\nTI com salário > 4500")
print(funcionarios_filtrados)

# 4. Adicione uma nova coluna chamada "Anos na Empresa" calculando a diferença entre a data atual e a data de contratação.
data_atual = datetime.now()
df['Anos na Empresa'] = ((data_atual - df['Contratado em']).dt.days / 365).apply(math.trunc)
print("Adiciona nova coluna com anos trabalhados na empresa")
print(df)

# 5. Crie uma nova coluna chamada "Faixa Salarial" que categorize os salários em 'Baixo', 'Médio' e 'Alto'.
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

# 6. Substitua valores nulos (se houver) na coluna "Departamento" por "Não Informado".
df['Departamento'] = df['Departamento'].fillna("Não Informado")
print("\nCaso exista, substituindo valores nulos em 'Departamento' por 'Não Informado'.")
print(df)

# 7. Agrupe os funcionários por "Departamento" e calcule a média salarial.
tabela_agrupada = df.groupby('Departamento')['Salário'].mean()
print("\nAgrupa por departamento e calcula média salarial.")
print(tabela_agrupada)

# 8. Exiba o funcionário mais velho.
funcionario_mais_velho = df.loc[df['Idade'].idxmax()]
print("\nFuncionário mais velho.")
print(funcionario_mais_velho)

# 9. Salve o DataFrame em um arquivo Excel chamado `funcionarios.xlsx`.
df.to_excel("arquivos_excel/funcionarios.xlsx", index=False)

# 10. Plote um gráfico de barras mostrando a distribuição de funcionários por "Departamento".
funcionarios_por_departamento = df.groupby('Departamento')['Funcionário'].count()
plt.title("funcionarios por departamento")
funcionarios_por_departamento.plot(kind='bar',x='Funcionário',y='Departamento')
plt.show()