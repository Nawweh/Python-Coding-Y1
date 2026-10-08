import pandas as pd

df = pd.read_csv("Task3_Glenstar_data.csv")

df['Date'] = pd.to_datetime(df['Date'],format='mixed', dayfirst=True) 

print(df['Date'])

df = df.loc[(df['Date'] >= '2026-01-03') & (df['Date'] < '2026-01-04')]

print(df['Date'])

