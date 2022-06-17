import pandas as pd

data = pd.read_csv('data_sets/neo.csv')

df = pd.DataFrame(data=data)

print(df.columns)

print(df[['est_diameter_min', 'est_diameter_max', 'hazardous']])


