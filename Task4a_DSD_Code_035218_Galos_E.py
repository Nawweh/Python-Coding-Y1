import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import time

FILE_PATH = Path(__file__).parent
CSV_PATH = (FILE_PATH/"Task4a_Glenstar_data.csv")

def main_menu(): #Outputs the main menu and checks the user input
    valid = False

    while valid == False:
        print(" ") #each blank print at the start of a function is to give space for the previous function to improve readability
        print("-"*70)
        print("---------- Athlete Performance Analysis Module ------------- ")
        print("-"*70)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("1. Places achieved by athlete")
        print("2. Performance based on rule sets")
        print("3. Amount of prize money achieved")

        choice = input('Enter your number selection here: ')

        if choice.isdigit(): #if the input isnt a digit then the input is not allowed to pass
            choice = int(choice)

            if choice <= 3 and choice >= 1: #if the input isnt between the amount of options in the menu then it also cant pass
                valid = True
                time.sleep(0.5) #each "time.sleep" is so the user has enough time to read the text before the next print statement
            else:
                 print("Please enter a value between 1 and 3")
                 time.sleep(1) #each incorrect input takes twice as long to give extra feedback to the user what is and isnt correct
    
        else:
            print("Sorry You did not enter a valid option")
            time.sleep(1)

    return int(choice)

def get_athlete_names():

    df = pd.read_csv(CSV_PATH) #loads the CSV

    athletes = df["Athlete"].unique().tolist() #grabs a list of all unique athletes

    valid = False

    while valid == False:
        print(" ")
        print("-"*70)
        print("---------- Athlete Performance Analysis Module ------------- ")
        print("-"*70)
        print("")
        print("--------------------- Athlete Positions Menu --------------------- ")
        print("Select an athlete:")
        for i in range(len(athletes)): #prints out the list of athletes below eachother
            print(i+1, " ", athletes[i])

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)

            if selection <= len(athletes) and selection >= 1: #if the input isnt between the amount of options in the menu then it cant pass
                valid = True
            else:
                print("Please enter a value between 1 and 10")
                time.sleep(1)
        else:
            print("Sorry You did not enter a valid option")
            time.sleep(1)

        
    chosen_athlete = athletes[selection -1] #retrieves the selected athlete from the list
   
    print("You have selected athlete: ",chosen_athlete)
    time.sleep(0.5)
    return chosen_athlete

def get_date(start_end):
    
    valid = False
    
    while valid == False:
        print(" ")
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end)) #asks for a date input for both start and end dates

        try:
           pd.to_datetime(date, format="%d/%m/%Y") #changes the input into a date
        except:
            print("Sorry, you did not enter a valid date") #if it cant be changed to a date it runs this
            valid = False
            time.sleep(1)
        else:
            valid = True
            time.sleep(0.5)
    
    return date

def get_data_by_athlete_and_date(athlete, start_date, end_date):
    df = pd.read_csv(CSV_PATH) #loads the csv
    athlete_data = df.loc[df["Athlete"] == athlete].copy() #grabs all of the data that has the selected athlete in the row

    athlete_data["Date"]= pd.to_datetime(athlete_data["Date"], format="%d/%m/%Y", errors="raise") #converts all stored dates into a format that pandas can recognise
    
    date_range = (athlete_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (athlete_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" )) #creates an if statement for if the date is within range of start and end dates
    
    athlete_extract = athlete_data.loc[date_range] #the statement prior is used here

    return athlete_extract

def calculate_places (athlete_extract, athlete, start_date, end_date):
    gold = athlete_extract['Place'].value_counts().get("Gold")
    silver = athlete_extract['Place'].value_counts().get("Silver")
    bronze = athlete_extract['Place'].value_counts().get("Bronze")
    top_10= athlete_extract['Place'].value_counts().get("Top 10")
    no_place = athlete_extract['Place'].value_counts().get("Not Placed") #counts how many times the athlete got each placement



    print(" ")
    print("Here is the break down of the performance of {} between {} and {}: ".format(athlete, start_date, end_date)) #prints them out here
    print("Gold medals: ", gold)
    print("Silver medals:", silver)
    print("Bronze medals: ", bronze)
    print("Top 10: ", top_10)
    print("Not placed: ", no_place)

def placement_on_ruleset(athlete_extract):
    athlete_extract = athlete_extract.groupby("Rule Set")["Place"].value_counts() #groups the rule sets and placements together by how many times the athlete has gotten that placement
    athlete_extract.reset_index()
    athlete_extract.plot(kind="barh",x="Rule Set",y="Place",xlabel = "Rule Set", ylabel = "Placement", title = "Placement based on ruselet")
    plt.figure(1, (10,10)) 
    plt.show() #shows all of the graphs currently queued up (in this case is just 1)

def earnings_achieved(athlete_extract, athlete, start_date, end_date):
    earnings = str(athlete_extract["Prize Money"].sum())
    earnings = ("£"+earnings)
    print(" ")
    print("{} earned {} between {} and {}".format(athlete, earnings, start_date, end_date))
    time.sleep(1)

    athlete_extract = athlete_extract.groupby("Date")["Prize Money"].sum() #groupds each Date to the total prize earnings that day
    athlete_extract.reset_index()
    athlete_extract.plot(kind="line",x="Date",y="Prize Money") #plots the graph
    plt.show() #shows all of the graphs currently queued up (in this case is just 1)



def run_main_menu():

    main_menu_choice = main_menu() #grabs a number from the main menu and picks a choice corresponding to that number

    if main_menu_choice == 1:
        athlete = get_athlete_names()
        start_date = get_date("start")
        end_date = get_date("end")
        athlete_extract = get_data_by_athlete_and_date(athlete, start_date, end_date)
        calculate_places (athlete_extract, athlete, start_date, end_date)

    elif main_menu_choice == 2:
        athlete = get_athlete_names()
        start_date = get_date("start")
        end_date = get_date("end")
        athlete_extract = get_data_by_athlete_and_date(athlete, start_date, end_date)
        placement_on_ruleset(athlete_extract)

    elif main_menu_choice == 3:
        athlete = get_athlete_names()
        start_date = get_date("start")
        end_date = get_date("end")
        athlete_extract = get_data_by_athlete_and_date(athlete, start_date, end_date)
        earnings_achieved(athlete_extract, athlete, start_date, end_date)

    else:
        print("This is not an option, please try again")

    return True

main_menu_ran = run_main_menu()

if main_menu_ran == True: #allows for the user to continue if the program has already been ran once
    run = True

    while run == True:
        valid = False

        while valid == False:

            try:
                time.sleep(1)
                print(" ")
                choice = int(input('''Would you like to continue:
1: yes
2: no
Input Here: '''))

                if choice == 1:
                    time.sleep(0.5)
                    run_main_menu()
                    valid = True

                elif choice == 2:
                    print("Okay, closing the program")
                    time.sleep(0.5)
                    valid = True
                    run = False

                else:
                    print("Please input a number that is 1 or 2")
            except:
                print("Please input a number")