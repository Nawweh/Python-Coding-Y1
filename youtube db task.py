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
    df1=df1.sort_values("highest_yearly_earnings",ascending=True)
    df1=df1.tail(5)

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
    
def urban_pop_to_dens_yt():

    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)

    df1=df["Urban_population"].value_counts()
    print(df1.head(1))

def dens_channel_month():


    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)

    df1=df["created_month"].value_counts()
    print(df1.head(1))

def success_to_years():
    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)

    df1=df.groupby("created_year")[["highest_yearly_earnings"]].max()
    df1=df1.reset_index()
    df1=df1.head(250)
    df1.plot(kind="bar",x="created_year",y="highest_yearly_earnings")
    plt.xticks(rotation=90)
    plt.show()

def category_most_views():
    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)

    df1=df.groupby("category")[["video views"]].sum()
    df1=df1.reset_index()
    df1=df1.head(100)

    df1.plot(kind="bar",x="category",y="video views")
    plt.xticks(rotation=90)
    plt.show()

def lowest_education():
    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)

    df1=df.groupby("Country")[["Gross tertiary education enrollment (%)"]].mean()

    df1=df1.reset_index()

    df1.plot(kind="bar",x="Country",y="Gross tertiary education enrollment (%)")
    plt.xticks(rotation=90)
    plt.show()

def lowest_education_youtubers():
    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)

    df1=df.loc[ (df["Country"]=="Samoa")]
    df1=df1.groupby("Youtuber")[["video views"]].max()

    df1=df1.reset_index()

    df1.plot(kind="bar",x="Youtuber",y="video views")
    plt.xticks(rotation=90)
    plt.show()

def successful_youtubers_2013():

    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)

    df1=df.loc[ (df["created_year"]==2013)]

    df1=df1.groupby("Youtuber")[["video views"]].sum()
    df1=df1.reset_index()

    df1.plot(kind="bar",x="Youtuber",y="video views")
    plt.xticks(rotation=90)
    plt.show()

def views_most_year():

    FILE_PATH=Path(__file__).parent 

    CSV_PATH=(FILE_PATH/"Global YouTube StatisticsFixed.csv")

    df=pd.read_csv(CSV_PATH)

    df1=df.groupby("created_month")[["uploads"]].sum()
    df1=df1.reset_index()

    df1.plot(kind="bar",x="created_month",y="uploads")
    plt.xticks(rotation=90)
    plt.show()
