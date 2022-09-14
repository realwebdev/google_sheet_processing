import pandas as pd
df = pd.read_csv('pokemon_data.csv')
print(df.head(3)) # limit the finding

print(df.iloc[2,1])
