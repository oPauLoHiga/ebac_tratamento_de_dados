import pandas as pd

# Função para calcular o cubo de um numero
def elevar_cubo(x):
    return x ** 3

# Expressão de lambda para calcular o cubo de um numero
elevar_cubo_lambda = lambda x: x ** 3

print(elevar_cubo(2))
print(elevar_cubo_lambda(2))

df = pd.DataFrame({'numeros':[1, 2, 3, 4, 5, 10]})

df['cubo_funcao'] = df['numeros'].apply(elevar_cubo)
df['cubo_lambda'] = df['numeros'].apply(lambda x: x ** 3)
print(df)