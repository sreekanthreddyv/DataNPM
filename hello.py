import pandas as pd

df = pd.read_csv("gapminder.tsv", sep='\t')

# print(df.head())

print(df.shape)

print(df.columns)

print(df.dtypes)
