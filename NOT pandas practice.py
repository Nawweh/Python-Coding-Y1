import pandas as pd
import matplotlib.pyplot as plt
import numpy
from pathlib import Path
 
def main():
    FILE_PATH=Path(__file__).parent
    CSV_PATH=(FILE_PATH /"Global Youtube StatisticsFixed.csv")
    df=pd.read_csv(CSV_PATH)
   
    #Country with most views
    # df1=df.groupby("Country")["video views"].sum()
    # df1=df1.reset_index()
    # df1=df1.sort_values('video views', ascending=False)
    # print(df1.head(1))
 
    #Country with most subscribers
    # df1=df.groupby("Country")["subscribers"].sum()
    # df1=df1.reset_index()
    # df1=df1.sort_values('subscribers', ascending=False)
    # print(df1.head(1))
 
    #Youtuber with most views
    # df1=df.groupby("Youtuber")["video views"].sum()
    # df1=df1.reset_index()
    # df1=df1.sort_values('video views', ascending=False)
    # print(df1.head(1))
 
    #Youtuber with highest earnings in specified country
    # df1=df.loc[(df['Country']=='United States')]
    # df1=df1.sort_values('highest_yearly_earnings', ascending=False)
    # print(df1.iat[0,1])
 
    #Graph of unemplyment to succes
    # df1=df.groupby("Unemployment rate")["video views"].sum()
    # df1=df1.reset_index()
    # df1.plot(kind="scatter",x="Unemployment rate",y="video views")
    # plt.show()
 
    #Highest density of youtubers compared to urban population
    # df1=df["Urban_population"].value_counts()
    # print(df1.head(1))
 
    #Month with the highest density of channels created
    # df1=df['created_month'].value_counts()
    # print(df1.head(1))
 
    #Year with the most successful channels
    # df1=df.sort_values('video views', ascending=False)
    # df1=df1.reset_index()
    # df1=df1.head(100)
    # df1=df1['created_year'].value_counts()
    # print(df1.head(1))
 
    #Which category has the most overall video views
    # df1=df.groupby('category')['video views'].sum()
    # df1=df1.reset_index()
    # df1.plot(kind="bar",x="category",y="video views")
    # plt.show()
 
    #Which country has the lowest gross tertiary education enrollment
    # df1=df.groupby('Country')['Gross tertiary education enrollment (%)'].mean()
    # df1=df1.reset_index()
    # df1.plot(kind="bar",x="Country",y="Gross tertiary education enrollment (%)")
    # plt.show()
 
    #Top 5 youtubers from the lowest GTEE
    # df1=df.sort_values('Gross tertiary education enrollment (%)')
    # lowest=df1.iat[0,7]
    # df1=df1.loc[(df['Country']==lowest)]
    # df1=df1.groupby('Youtuber')['video views'].sum()
    # df1=df1.reset_index()
    # df1=df1.head(5)
    # df1.plot(kind="bar",x="Youtuber",y="video views")
    # plt.show()
 
    #Most successful from 2013
    # df1=df.loc[(df['created_year']==2013)]
    # df1=df1.groupby('Youtuber')['video views'].sum()
    # df1=df1.reset_index()
    # df1=df1.sort_values('video views',ascending=False)
    # df1.plot(kind='bar',x='Youtuber',y='video views')
    # plt.show()
 
    #Year with most uploads
    df1=df.groupby('created_month')['uploads'].sum()
    df1=df1.reset_index()
    df1.plot(kind='bar',x='created_month',y='uploads')
    plt.show()
   
main()