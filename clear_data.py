import pandas as pd

df = pd.read_csv('GooglePlayStore_wild.csv')

print(df.info())
print(len(df[pd.isnull(df['Rating'])]))
df['Rating'].fillna(-1, inplace = True)
print(df['Size'].value_counts())


def set_size(size):
   if size[-1] == 'M':
      return float(size[:-1])
   elif size[-1] == 'k':
      return float(size[:-1]) / 1024
   return -1

df['Size'] = df['Size'].apply(set_size)
print(df[df['Category'] == 'TOOLS']['Size'].max())

def set_installs(installs):
   if installs == '0':
       return 0
   return int(installs[:-1].replace(',', ''))

df['Installs'] = df['Installs'].apply(set_installs)
print(round(df.pivot_table(index = 'Content Rating', columns = 'Type', values = 'Installs', aggfunc = 'mean')), 1)
print(df[pd.isnull(df['Type'])])
df['Type'].fillna('Free', inplace = True)


print(df.info())
