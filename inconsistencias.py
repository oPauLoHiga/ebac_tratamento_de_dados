import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes_remove_outliers.csv')

print(df.head())

# Mascarar dados pessoais
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}')

# Corrigir Datas
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01'))
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year
df['idade_ajustada'] -= ((data_atual.month <= df['idade_ajustada'].dt.month) & (data_atual.day < df['idade_ajustada'].dt.day)).astype(int)
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan

# Corrigir campo com multiplas informações
