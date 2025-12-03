import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path 

def views():

    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)


    df1=df.groupby("Country")[["video views"]].sum()
    df1=df1.reset_index()
    df1.plot(kind="bar",x="Country",y="video views")
    plt.xticks(rotation=90)
    plt.show()
    
def subs():

    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)


    df1=df.groupby("Country")[["subscribers"]].sum()
    df1=df1.reset_index()
    df1.plot(kind="bar",x="Country",y="subscribers")
    plt.xticks(rotation=90)
    plt.show()

def yt_views():

    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)


    df1=df.groupby("Youtuber")[["video views"]].sum()
    df1=df1.reset_index()
    df1=df1.sort_values("video views")
    df1=df1.tail(50)
    df1.plot(kind="bar",x="Youtuber",y="video views")
    plt.xticks(rotation=90)
    plt.show()

def yt_earnings_spec_country():

    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)
    

    df1=df.loc[ (df["Country"]=="United States")]
    df1=df1.sort_values("highest_yearly_earnings",ascending=False)
    df1=df1.head(5)

    df1.plot(kind="bar",x="Youtuber",y="highest_yearly_earnings")
    plt.xticks(rotation=90)
    plt.show()

def yt_unempreate_to_ytsuccess():

    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)


    df1=df.groupby("Unemployment rate")[["highest_monthly_earnings"]].max()
    df1=df1.reset_index()
    df1.plot(kind="scatter",x="Unemployment rate",y="highest_monthly_earnings")
    plt.xticks(rotation=90)
    plt.show()
    
yt_unempreate_to_ytsuccess()