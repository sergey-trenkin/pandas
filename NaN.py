import pandas as pd
df = pd.read_csv('googleplaystore.csv')

print(df.iloc[10472])
columns = list(df.columns)
index = 10472
for i in range(len(columns) -1, 1, -1):
   df[columns[i]][index] = df[columns[i - 1]][index]

df['Category'][index] = 'LIFESTYLE'
df['Genres'][index] = 'Lifestyle'

print(df.iloc[10472])
