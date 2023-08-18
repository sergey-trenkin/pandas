import pandas as pd
df = pd.read_csv('GoogleApps.csv')

print(df['Category'].value_counts())

temp = df['Content Rating'].value_counts()
print('Соотношение:', round(temp['Teen'] / temp['Everyone 10+'], 2))


temp = df.groupby(by = 'Type')['Rating'].mean()
print(temp['Paid'])

print(round(temp['Paid'] - temp['Free'], 2))

print(df.groupby(by = 'Category')['Size'].agg(['min', 'max']))


temp = df[df['Rating'] > 4.5]['Category'].value_counts()
print(temp['FINANCE'])


temp = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(temp['Free'] / temp['Paid'])
