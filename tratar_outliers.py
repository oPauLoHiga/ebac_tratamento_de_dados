import  pandas as pd
from scipy import stats

pd.set_option('display.max_columns', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]

print('Filtro básico\n', df_filtro_basico[['nome', 'idade']])

# Identificar outliers com Z-score
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 3]
print("Outliers pelo Z-score: \n", outliers_z)

# Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df['idade']) < 3)]

# Identificar outliers com IQR
