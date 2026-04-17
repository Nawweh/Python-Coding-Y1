import pandas as pd
import matplotlib.pyplot as plt
import time

RUN = True

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Time taken to resolve an issue by type")
        print("### 3. Issues and resolutions based on region")
        print("### 4. Leave")

        try:
            choice = input('Enter your number selection here: ')
            choice = int(choice)
            if choice > 4 or choice < 1: #if choice is not valud, then it will re run the code from the loop
                print("Sorry, you did not enter a valid option, the inputted number is out of range")
            
            else:
                print("choice accepted")
                flag = False
        except:
            print("\nSorry, you did not enter a valid option")
            time.sleep(2)
            flag = True

    return choice

  # Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            choice = input('Enter your number selection here: ')
            choice = int(choice)
            if choice > 4 or choice < 1: #if choice is not valud, then it will re run the code from the loop
                print("Sorry, you did not enter a valid option, the inputted number is out of range")
            
            else:
                print("choice accepted")
                flag = False
        except:
            print("\nSorry, you did not enter a valid option")
            time.sleep(2)
            flag = True


    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("Task4a_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg

def get_time_type(): #gets the total days spent resolving each issue
    df = pd.read_csv("Task4a_data.csv")

    df1 = df.groupby("Issue Type")["Days To Resolve"].sum()
    df1 = df1.reset_index()
    df1.plot(kind = "barh", x="Issue Type", y="Days To Resolve", ylabel="Days Spent Resolving")
    plt.show()

def get_iss_res(): #gets a single region out of a list of all regions then pulls their issue and how it was resolved.
    
    regions = ["South West", "West Midlands","London","North Wales","South East","East of England","North East","East Midlands","Scotland","Yorkshire and The Humber","South Wales","North West","Northern Ireland"]
    df = pd.read_csv("Task4a_data.csv")
    

    df1 = df.groupby("Region")["Issue Type"]
    print(df1)
    df1 = df.groupby("Region")["How Resolved"]
    print(df1)

df = pd.read_csv("Task4a_data.csv")
df1=df["Region"]
df1 = df1.drop_duplicates()
print(df1)
while RUN == True: #while the user wants it to run, the menu runs
    
    main_menu_choice = main_menu()

    match main_menu_choice:
        case 1:
            total_menu_choice = total_menu()
            print(get_total_data(total_menu_choice))

        case 2:
            get_time_type()

        case 3:
            get_iss_res()
            
        case 4:
            print("Okay, leaving the menu...") #if the user selects 4, it ends the program
            time.sleep(3)
            RUN = False



