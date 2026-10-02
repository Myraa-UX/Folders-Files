import pandas as pd

#create data
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
print(data)
df = pd.DataFrame(data)
print(df)
df.to_csv('D:\\Ankshi_Python\\data.csv', index=False)
