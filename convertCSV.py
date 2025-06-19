import pandas as pd
data = pd.read_csv('sentences.csv')
df = pd.DataFrame(data)
print(df)

nested_json = df.to_json('sentences.json', orient='records')


