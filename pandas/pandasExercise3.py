import pandas as pd

df = pd.read_csv('./data/Titanic-Dataset.csv')
print(df.describe(), "\n")

# Busca valores nulos de edad y sustituyelos por un valor que tenga sentido, explica por qué
numNull = df['Age'].isna().sum()
print("# of NA/Null age values:\n", numNull)
newDf = df['Age']
