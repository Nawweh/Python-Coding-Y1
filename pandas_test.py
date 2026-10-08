import pandas as pd
from pathlib import Path

FILE_PATH = Path(__file__).parent
CSV_PATH = (FILE_PATH/"Task3_Glenstar_data.csv")

df = pd.read_csv(CSV_PATH)

df['Date'] = pd.to_datetime(df['Date'],format="Mixed",dayfirst=True)

print(df['Date'])

df = df.loc[(df['Date'] >= '2026-01-03') & (df['Date'] < '2026-01-04')]

print(df['Date'])

