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

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("\nSorry, you did not enter a valid option")
            time.sleep(2)
            flag = True
        
        else:    
            print('Choice accepted!')
            flag = False


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
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            choice = int(choice)
            flag = False

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("Task4a_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg


def time_taken_type(): #provides data validation for the selection of issue types. returns the selected type
    print("####################################################")
    print("##### Time taken to resolve an issue by type #######")
    print("####################################################")
    print("")
    print("########## Please select an issue type ##########")
    print("### 1. Customer Account Issue")   
    print("### 2. Delivery Issue") 
    print("### 3. Collection Issue")  
    print("### 4. Service Complaint")
    
    choice = input('Enter your number selection here: ')

    try:
        int(choice)
    except:
        print("Sorry, you did not enter a valid option")
        flag = True
    else:    
        print('Choice accepted!')
        choice = int(choice)
        flag = False

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType

def get_time_type(time_taken_choice):
    df = pd.read_csv("Task4a_data.csv")

    df1=df.groupby(time_taken_choice)["Days To Resolve"].sum()
    print(df1)




# while RUN == True: #while the user wants it to run, the menu runs
main_menu_choice = main_menu()

match main_menu_choice:
    case 1:
        total_menu_choice = total_menu()
        print(get_total_data(total_menu_choice))

    case 2:
        time_taken_choice = time_taken_type()
        get_time_type(time_taken_choice)

    case 3:
        print("placeholder")
        
    case 4:
        print("Okay, leaving the menu...") #if the user selects 4, it ends the program
        time.sleep(3)
        RUN = False



