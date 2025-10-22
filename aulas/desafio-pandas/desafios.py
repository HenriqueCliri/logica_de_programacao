# %%
import pandas as pd
db = pd.read_csv("./data.csv", encoding="utf-8", decimal=",") 
df = pd.DataFrame(db)

# tratamento de dados para a coluna 'Calories'
df['Calories'] = df['Calories'].dropna().astype(float)

#tamanho da tabela
max_val = 0
for line in db.count():
    max_val = max(line, max_val)

print(f'maior linha: {max_val}')

rows, columns = 0, 0

for col in db.count(axis='columns'):
    columns+=1

for row in db.count(axis='rows'):
    rows+=1

print(f'{columns}x{rows}') # ?


# %%
##Nomes e tipos de dados das colunas

print(f'Tipos de dados:\n{df.dtypes}')

nome_colunas = df.columns
# nome_colunas.astype(str)
upper_colunas = nome_colunas.map(lambda x: x.upper())
print(f'\nNome das colunas: {upper_colunas.to_list()}')

# %%
#resumo estatístico descritivo

#são 8 métricas estatísticas
#quartil 25% (Q1), nesse caso apenas os valores da metáde do range são consideradas (isso em um lista ordenada) - 
# os valores antes da mediana, então encontrados, encontramos a média destes, que no caso são os 25%,
# assim, 25% dessa lista estão abaixo da média que encontramos.
# funciona apenas para lista ordenada?

nome_indices = {
    'count': 'Quantidade',
    'mean': 'Média',
    'std': 'Desvio Padrão',
    'min': 'Mínimo',
    '25%': 'Q1 (25%), quartil',
    '50%': 'Q2 (50%), quartil', 
    '75%': 'Q3 (75%), quartil',
    'max': 'Máximo'
}

metricas_renomeadas = df.describe().rename(index=nome_indices)

round(metricas_renomeadas)
# print("Resumo estatístico descritvo")
# print(f'{round(metricas_renomeadas)}') 

# então para Q2 (50%), temos a metade da lista, sendo que cada parte contém metade acima e metade abaixo do meio.

# Q3 basicamente é a mesma coisa que o Q1, a diferença é que trabalhamos com o range acima da média.        



# %%
# Verificar se há valores vazios nas colunas. caso sim, contá-los

print(df.isnull().any())

for val in df.columns:
    sum = df[val].isnull().sum()
        
    if sum > 0:
        print(f'coluna {val} contém valor(es) nulo(s)')
        print(f'quantidade de células nulas: {sum}')

# %%
# media da coluna 'Pulse'

media_pulse = round(df['Pulse'].mean(), 2)
print(f'media da coluna Pulse: {media_pulse}')

# %%
# exibir as 8 primeiras linhas do dataframe

_8_primeiras_linhas = df.head(8)
print(f'8 primeiras linhas:\n {_8_primeiras_linhas}')

# %%
# mediana da coluna Duration

# mid = df['Duration'].to_list()

# meio = len(mid / 2) - (len(mid % 2))

# mediana = (len(mid) % 2 == 0 ? ((mid[meio] + mid[meio + 1]) / 2) : mid[meio])
# print(3 / 2)

mediana_duration = df['Duration'].median()
print(f'mediana da colun "Duration": {round(mediana_duration)}')

# %%
# media moda da coluna 'Maxpulse'
moda_max_pulse = df['Maxpulse'].mode()
print(f'valor da media moda da coluna "Maxpulse": {moda_max_pulse.to_list()[0]}')

# %%
# media da coluna calorias, apenas para valores acima de 60
filtro = df['Calories'] > 60.0
calorias = df[filtro]
media_acima_de_60 = calorias.mode()

media_calorias_filtrado = media_acima_de_60['Calories'].to_list()[0]
print(f'filtro (acima de 60 calorias) para a coluna "Calories": {media_calorias_filtrado}')

# %%
#mediana para Maxpulse, sendo válido apenas para valores maiores que 110

filtro_max_pulse_110 = df['Maxpulse'] > 110

max_pulse_filtrado = df[filtro_max_pulse_110]
median_max_pulse = max_pulse_filtrado['Maxpulse'].median()

str_median_max_pulse = str(median_max_pulse)
print(f'mediana da coluna "Maxpulse": {float(str_median_max_pulse)}')


# %%
#calcular o desvio padrão da coluna 'Calories'

desvio_padrao_calories = df['Calories'].std()
print(f'valor do desvio padrão da coluna "Calories": {desvio_padrao_calories}')

# %%
#calcular a variância da coluna 'Pulse'

variancia = df['Pulse'].var()
print(f'variancia da colun "Pulse": {float(variancia)}')

# %%
#amplitude da coluna 'Duration'
max_duration = max(df['Duration'])
min_duration = min(df['Duration'])

amplitude = max_duration - min_duration
print(f'amplitude da coluna "Duration": {amplitude}')

# %%
quartis = ['25%', '50%', '75%']
resumo = df['Maxpulse'].describe()

nomes_quartis = {
    '25%': 'Q1 (25%)', 
    '50%': 'Q2 (50%)', 
    '75%': 'Q3 (75%)',
    }

resumo_renomeado = resumo.loc[quartis].rename(index=nomes_quartis)
df_resumo_renomeado = pd.DataFrame(resumo_renomeado).reset_index().rename(columns={"index": "Quartis"})
df_resumo_renomeado

# %%
#desvio padrão da coluna 'Calories'

calories_desvio_padrao = df['Calories'].std()
coeficiente_de_variacao = calories_desvio_padrao / df['Calories'].mean()
print(f'Coeficiente de variação da coluna "Calories": {float(coeficiente_de_variacao)}')

# %%



