import pandas as pd

df = pd.read_csv('data.csv', index_col='region_name')
df.info()

# Представим ситуацию, что из-за невнимательности операциониста, регионы: 
# Республика Алтай, Магаданская обл. оказались не представлены в итоговой сводке.
df.drop(['г. Севастополь', 'Республика Марий Эл', 'Владимирская область'], inplace=True)
df.sort_values('salary', inplace=True)

print(df.head(5).tail(1))
print(df.head(30).tail(1))
print(df.head(43).tail(1))

print(df['salary'].mean())
print(df['salary'].median())
