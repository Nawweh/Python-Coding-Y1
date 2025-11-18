# importing pandas as pd 

import pandas as pd 


# Creating the dataframe 

df = pd.DataFrame({
    "Player": ["Hardik Pandya", "KL Rahul", "Andre Russel", "Jasprit Bumrah", "Virat Kohil", "Rohit Sharma"],
    "Team": ["Mumbai Indians", "Kings Eleven", "Kolkata Knight Riders", "Mumbai Indians", "RCB", "Mumbai Indians"],
    "Category": ["Batsman", "Batsman", "Batsman", "Bowler", "Batsman", "Batsman"],
    "BidPrice": [13, 12, 7, 10, 17, 15],
    "Runs": [1000, 2400, 900, 200, 3600, 3700]
})
 

# Print the dataframe 

# df=df.sort_values(ascending=False,by="B")
# print(max(df.value_counts(subset="A")))

# print(df.groupby("Team")[["BidPrice"]].max())



print(df.groupby("Team")[["Runs"]].agg(["mean","min"]))

df[["Runs","BidPrice"]].max