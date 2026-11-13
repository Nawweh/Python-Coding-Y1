import pandas as pd
import matplotlib.pyplot as plt


# Outputs the main menu and checks the user input
def main_menu():
    valid = False
    while valid == False:
        print("-" * 70)
        print("---------- Athlete Performance Analysis Module ------------- ")
        print("-" * 70)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("1. Places achieved by athlete")
        print("2. Trends for athlete performance")
        print("3. Sum of prize money achieved")
        choice = input('Enter your number selection here: ')
        if choice.isdigit():
            # Checks if the selection is an option in the above list
            choice = int(choice)
            if choice >= 1 and choice <= 3:
                valid = True
            else:
                print("Sorry you did not enter a valid option")
        else:
            print("Sorry you did not enter a valid option")
    return choice

# allows user to select one athlete
def get_athlete_names():
    df = pd.read_csv("Task4a_Glenstar_data.csv")
    # Gets a list of the athlete names from the dataframe
    athletes = df["Athlete"].unique().tolist()
    valid = False
    while valid == False:
        print("-" * 70)
        print("---------- Athlete Performance Analysis Module ------------- ")
        print("-" * 70)
        print("")
        print("--------------------- Athlete Positions Menu --------------------- ")
        print("Select an athlete:")
        lastdigit = 0
        for i in range(len(athletes)):
            print(i + 1, " ", athletes[i])
            lastdigit += 1
        selection = input('Enter your number selection here: ')
        if selection.isdigit():
            selection = int(selection)
            if selection > 0 and selection <= lastdigit:
                valid = True
            else:
                print("Sorry you did not enter a valid option")
        else:
            print("Sorry you did not enter a valid option")
    # Gets the chosen athlete name from the list
    chosen_athlete = athletes[selection - 1]
    print("You have selected athlete: ", chosen_athlete)
    return chosen_athlete

# Gets a date from the user and returns it if valid
def get_date(start_end):
    flag = True
    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))
        try:
            pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    return date

#grabs a a dataframe that contains data from the athlete between the selected dates
def get_data_by_athlete_and_date(athlete, start_date, end_date):
    all = pd.read_csv("Task4a_Glenstar_data.csv")
    # Creates a copy of the section of the dataframe where the name in the 'Athlete' column is the one chosen by the user
    athlete_data = all.loc[all["Athlete"] == athlete].copy()
    # Converts the values in the 'Date' column to dates
    athlete_data["Date"] = pd.to_datetime(athlete_data["Date"], format="%d/%m/%Y", errors="raise")
    # Creates a date range using the entered values to be used when filtering the data
    date_range = (
        (athlete_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y"))
        & (athlete_data["Date"] <= pd.to_datetime(end_date, format="%d/%m/%Y"))
    )
    # Extracts the data that is in the above date range before returning it to the user
    athlete_extract = athlete_data.loc[date_range]
    return athlete_extract


# If no individual athlete is selected, this function is used to return relevant data instead
def get_data_by_date(start_date, end_date):
    all = pd.read_csv("Task4a_Glenstar_data.csv")
    # Converts the date column to dates
    all["Date"] = pd.to_datetime(all["Date"], format="%d/%m/%Y", errors="raise")
    # Creates the date range filter
    date_range = (
        (all["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y"))
        & (all["Date"] <= pd.to_datetime(end_date, format="%d/%m/%Y"))
    )
    # Uses the filter to extract relevant data, then returns it
    date_extract = all.loc[date_range]
    return date_extract

# Calculates how many times an athlete got each placement
def calculate_places(athlete_extract, athlete, start_date, end_date):
    gold = athlete_extract['Place'].value_counts().get("Gold")
    silver = athlete_extract['Place'].value_counts().get("Silver")
    bronze = athlete_extract['Place'].value_counts().get("Bronze")
    top = athlete_extract['Place'].value_counts().get("Top 10")
    no_place = athlete_extract['Place'].value_counts().get("Not Placed")
    placements_array = [gold, silver, bronze, top, no_place]
    for placement in range(5):
        try:
            placements_array[placement] = int(placements_array[placement])
        except:
            placements_array[placement] = 0
    print("Here is the break down of the performance of {} between {} and {}: ".format(athlete, start_date, end_date))
    print("Gold medals: ", gold)
    print("Silver medals:", silver)
    print("Bronze medals: ", bronze)
    print("Top 10: ", top)
    print("Not placed: ", no_place)

    if get_graph_request() == "y":
        plt.bar(["Gold", "Silver", "Bronze", "Top 10", "No Place"], placements_array)
        plt.title(f"Performance of {athlete} between {start_date} and {end_date}")
        plt.xlabel("Placement")
        plt.ylabel("Amount of times achieved")
        plt.show()


# Asks the user if they want the performance of one athlete in different rule sets or the overall performance of athletes in different rulesets
def get_performance_choice():
    valid = False
    while not valid:
        print("-" * 70)
        print("---------- Athlete Performance Analysis Module ------------- ")
        print("-" * 70)
        print("")
        print("--------------------- Athlete Performance Trends Menu --------------------- ")
        print("1. Analyse performance of one athlete in different rulesets in a date range")
        print("2. Compare overall performance of athletes in different rulesets between two dates")
        performance_choice = input('Enter your number selection here: ')
        if performance_choice.isdigit():
            performance_choice = int(performance_choice)
            if performance_choice == 1 or performance_choice == 2:
                return performance_choice
            else:
                print("Sorry, you did not enter a valid choice")
        else:
            print("Sorry, you did not enter a valid choice")


# Compares the performance for an athlete between judo and jiu-jitsu in a date range
def calculate_individual_performance(athlete_data):
    judo_data = athlete_data[(athlete_data['Rule Set'] == "Judo")]
    jiujitsu_data = athlete_data[(athlete_data['Rule Set'] == "Jiu-Jitsu")]
    judo_placements = judo_data['Place'].value_counts()
    jiujitsu_placements = jiujitsu_data['Place'].value_counts()
    possible_placements = ['Gold', 'Silver', 'Bronze', 'Top 10', 'Not Placed']
    judo_placements_output = []
    jiujitsu_placements_output = []
    for placement in possible_placements:

        if judo_placements.get(placement) != None:
            judo_placements_output.append(judo_placements.get(placement))
        else:
            judo_placements_output.append(0)
        if jiujitsu_placements.get(placement) != None:
            jiujitsu_placements_output.append(jiujitsu_placements.get(placement))
        else:
            jiujitsu_placements_output.append(0)

    print(f"Total judo placements for {athlete} between {start_date} and {end_date}:")
    for output in range(5):
        print(f"{possible_placements[output]}: {judo_placements_output[output]}")
    print(f"Total jiu-jitsu placements for {athlete} between {start_date} and {end_date}:")
    for output in range(5):
        print(f"{possible_placements[output]}: {jiujitsu_placements_output[output]}")

    if get_graph_request() == "y":
        print("Graphs created. Close them to return to main menu")
        plt.figure(0, (8, 8))
        plt.bar(possible_placements, judo_placements_output)
        plt.title(f"Total placements for {athlete} in judo between {start_date} and {end_date}:")
        plt.xlabel("Placement")
        plt.ylabel("Amount of times achieved")
        plt.figure(1, (8, 8))
        plt.bar(possible_placements, jiujitsu_placements_output, color="orange")
        plt.title(f"Total placements for {athlete} in jiu-jitsu between {start_date} and {end_date}:")
        plt.xlabel("Placement")
        plt.ylabel("Amount of times achieved")
        plt.show()


# Shows the total amount of placements achieved for judo and jiu-jitsu between two dates
def calculate_overall_performance(date_range_data):
    # Finds the overall placements for each rule set
    judo_data = date_range_data[(date_range_data['Rule Set'] == "Judo")]
    judo_placements = judo_data['Place'].value_counts()
    jiujitsu_data = date_range_data[(date_range_data['Rule Set'] == "Jiu-Jitsu")]
    jiujitsu_placements = jiujitsu_data['Place'].value_counts()
    # Afterwards, it finds how many of each placement was achieved for each rule set
    possible_placements = ['Gold', 'Silver', 'Bronze', 'Top 10', 'Not Placed']
    judo_placements_output = []
    jiujitsu_placements_output = []
    for placement in possible_placements:
        judo_placements_output.append(judo_placements.get(placement))
        jiujitsu_placements_output.append(jiujitsu_placements.get(placement))
    # After the values are put into the same order for each ruleset, outputs the values to the user
    print(f"Total judo placements for all athletes between {start_date} and {end_date}:")
    for output in range(5):
        print(f"{possible_placements[output]}: {judo_placements_output[output]}")
    print(f"Total jiu-jitsu placements for all athletes between {start_date} and {end_date}:")
    for output in range(5):
        print(f"{possible_placements[output]}: {jiujitsu_placements_output[output]}")
    # Creates graphs showing the difference between rulesets and placements if requested
    if get_graph_request() == "y":
        print("Graphs created. Close them to return to main menu")
        plt.figure(0, (8, 8))
        plt.bar(possible_placements, judo_placements_output)
        plt.title(f"Total overall placements (all athletes) for judo between {start_date} and {end_date}:")
        plt.xlabel("Placement")
        plt.ylabel("Amount of times achieved")
        plt.figure(1, (8, 8))
        plt.bar(possible_placements, jiujitsu_placements_output, color="orange")
        plt.title(f"Total overall placements (all athletes) for jiu-jitsu between {start_date} and {end_date}:")
        plt.xlabel("Placement")
        plt.ylabel("Amount of times achieved")
        plt.show()


# Asks the user whether they want to see an individual's sum of prize money or the sum of prize money for all athletes in the data
def get_prize_money_choice():
    valid = False
    while not valid:
        print("-" * 70)
        print("---------- Athlete Performance Analysis Module ------------- ")
        print("-" * 70)
        print("")
        print("--------------------- Athlete Prize Money Menu --------------------- ")
        print("1. Analyse prize money won by an individual athlete between two dates")
        print("2. Compare prize money won by all athletes in the date range provided")
        prize_money_choice = input('Enter your number selection here: ')
        if prize_money_choice.isdigit():
            prize_money_choice = int(prize_money_choice)
            if prize_money_choice == 1 or prize_money_choice == 2:
                return prize_money_choice
            else:
                print("Sorry, you did not enter a valid choice")
        else:
            print("Sorry, you did not enter a valid choice")


# Calculates how much was won over time by an individual athlete
def calculate_individual_winnings(athlete_data):
    money_won = list(athlete_data["Prize Money"])
    # Using a loop to create a list showing how much was won overall through the period of time
    total_amounts = []
    overall_amount = 0
    for amount in money_won:
        overall_amount += amount
        total_amounts.append(overall_amount)

    athlete_data["Total Winnings"] = total_amounts

    print(f"The total amount won by {athlete} between {start_date} and {end_date} was £{overall_amount}")

    if get_graph_request() == "y":
        print("Graphs created. Close them to return to main menu")
        plt.figure(0, (15, 15))
        plt.plot(athlete_data['Date'], athlete_data['Total Winnings'], marker="o")
        plt.title(f"Total money earned over time by {athlete} between {start_date} and {end_date}")
        plt.xlabel("Date")
        plt.ylabel("Amount of money won (£)")
        plt.grid(True)
        plt.show()


# Calculates how much was won by all athletes in a time period
def calculate_overall_winnings(date_range_data):
    # Finds out the total winnings for each of the athletes using the data provided
    sums_for_each_athlete = date_range_data.groupby("Athlete")["Prize Money"].sum().sort_values(ascending=False)
    # Afterwards, it outputs to the user how much each of the athletes won in that time period
    print(f"Total money won for each athlete between {start_date} and {end_date}:")
    for athlete in range(len(sums_for_each_athlete)):
        print(f"{sums_for_each_athlete.index[athlete]}: £{sums_for_each_athlete.values[athlete]}")
    # If chosen by the user, creates and displays a graph comparing the winnings of the athletes in the time period
    if get_graph_request() == "y":
        print("Graphs created. Close them to return to main menu")
        plt.figure(0, (17, 10))
        plt.bar(list(sums_for_each_athlete.index), list(sums_for_each_athlete.values))
        plt.title(f"Comparison of total money earned by all athletes between {start_date} and {end_date}")
        plt.xlabel("Athlete name")
        plt.ylabel("Amount of money won (£)")
        plt.show()


# Validates the dates so that an empty date cannot be submitted (wouldn't cause errors but causes nothing to be returned)
def get_dates():
    dates_entered = False
    while not dates_entered:
        start_date = get_date("start")
        end_date = get_date("end")
        if start_date != "" and end_date != "":
            return start_date, end_date
        else:
            print("Invalid date(s) entered, please try again")


# Asks the user if they want a graph for the data (used in multiple parts of the code, so would be more efficient to use a function for validation rather than add it manually)
def get_graph_request():
    valid = False
    while not valid:
        graph_request = input("Would you like a graph of this data? (Y/N) ")
        if graph_request.lower() == "y" or graph_request.lower() == "n":
            return graph_request.lower()
        else:
            print("Sorry, you did not enter a valid choice")


# Lets the user return to the main menu without having to reopen the program
def get_restart_choice():
    valid = False
    while not valid:
        restart_choice = input("Would you like to go back to the main menu? (Y/N) ")
        if restart_choice.lower() == "y" or restart_choice.lower() == "n":
            return restart_choice.lower()
        else:
            print("Sorry, you did not enter a valid choice")


running = True
while running:
    main_menu_choice = main_menu()
    # Lets the user find out the placements for an athlete in a chosen time range
    if main_menu_choice == 1:
        athlete = get_athlete_names()
        start_date = get_date("start")
        end_date = get_date("end")
        athlete_extract = get_data_by_athlete_and_date(athlete, start_date, end_date)
        calculate_places(athlete_extract, athlete, start_date, end_date)
    # Lets the user analyse trends for performance in different rule sets
    elif main_menu_choice == 2:
        # Allows the user to choose between an individual's performance or overall performance
        performance_choice = get_performance_choice()
        # Gets data between a period of time entered by the user
        start_date, end_date = get_dates()
        # If an individual is chosen, get the name of that athlete
        if performance_choice == 1:
            athlete = get_athlete_names()
            athlete_data = get_data_by_athlete_and_date(athlete, start_date, end_date)
            calculate_individual_performance(athlete_data)
        elif performance_choice == 2:
            date_range_data = get_data_by_date(start_date, end_date)
            calculate_overall_performance(date_range_data)
    # Lets the user analyse the trends with the prize money that is achieved
    elif main_menu_choice == 3:
        # Lets the user choose if they want to analyse one person's winnings or overall winnings
        prize_money_choice = get_prize_money_choice()
        # Gets the user to enter dates and returns the data for that period
        start_date, end_date = get_dates()
        # Gets the name of the athlete if focusing on one person instead of overall
        if prize_money_choice == 1:
            athlete = get_athlete_names()
            athlete_data = get_data_by_athlete_and_date(athlete, start_date, end_date)
            calculate_individual_winnings(athlete_data)
        # If not focusing on one athlete, gets the data for all athletes in the given date range
        elif prize_money_choice == 2:
            date_range_data = get_data_by_date(start_date, end_date)
            calculate_overall_winnings(date_range_data)
    # After using one of the main menu options, this gives the user the choice to return to the main menu rather than closing the program
    restart = get_restart_choice()
    if restart == "n":
        running = False
