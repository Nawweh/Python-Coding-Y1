import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path 

def test():
    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"vgsales.csv")

    df=pd.read_csv(CSV_PATH)

    df1=df["Name"].str.contains("LEGO")
    df1=df1.sort_values("Global_Sales",ascending=False)

    df1.plot(kind="bar",x="Platform",y="Global_Sales")
    plt.xticks(rotation=90)
    plt.title("hi")
    plt.show()

test()