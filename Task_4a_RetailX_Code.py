import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import time

FILE_PATH=Path(__file__).parent
CSV_PATH=(FILE_PATH /"Task_4a_RetailX_data.csv")

#Outputs the main menu and checks the user input
def main_menu():
    try:
        flag = True

        while flag:

            print("-"*66)
            print("---------- RetailX Sales Analysis Module ------------- ")
            print("-"*66)
            print("")
            print("--------------------- Main Menu --------------------- ")
            print("1. Total sales by product")
            print("2. Sales of different categories of products")
            print("3. Income and profit made by different products")

            choice = input('Enter your number selection here: ')

            if choice.isdigit():
                flag = False
            else:
                flag = True

        return int(choice)
    except:
        print("Unexpected input in the main menu, please only type 1 - 3 for your choice.")

#Generates submenu of available product codes and allows user to select a product to view
def get_product_id ():

    df = pd.read_csv(CSV_PATH)

    product_codes = df["Product ID"].unique().tolist()
    try:
        flag = True

        while flag:

            print("-"*66)
            print("---------- RetailX Sales Analysis Module ------------- ")
            print("-"*66)
            print("")
            print("-------------- Total sales by product -------------- ")
            print("Select a product code:")
            for i in range(len(product_codes)):
                print(i+1, " ", product_codes[i])

            selection = input('Enter your number selection here: ')

            if selection.isdigit():
                selection = int(selection)
                flag = False
            else:
                flag = True

            
            product_ID = product_codes[selection -1]
    
        print("You have selected product id:",product_ID)
        return product_ID
    except:
        print("Incorrect input. Please only enter valid product codes displayed on the screen")

#gets and converts user input from string to date format
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

#extracts data based on product ID within a user specified date range.
def get_data_by_ID_and_date(product_id, start_date, end_date):
    all_data = pd.read_csv(CSV_PATH)
    product_data = all_data.loc[all_data["Product ID"] == product_id].copy()

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]



    return extracted_data

#generates a total of the number of items sold for the extracted data
def calculate_total_sale (date_ID, product_id, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    print('The total number of sales for product {}, between {} and {} was: {}'.format(product_id, start_date, end_date, total_sales))


def sales_dif_cat(): #this shows the amount of sales dependent on the products category
    try:
        df = pd.read_csv(CSV_PATH)
        df1 = df.groupby("Category")["Qty Sold"].sum() #adds up the total sales by category
        df1.reset_index()
        df1.plot(kind="barh",x="Category",y="Qty Sold",figsize=(10,8))

        plt.title("Amount Of Sales For Categories") #changes the title
        plt.show()
    except:
        print("There has been an unexpected error with this function. Please check the csv is stored in the same file as this program and try again.")



def income_profit_products(): #gives the income and profit of each product
    try:
        df = pd.read_csv(CSV_PATH)
        income = df["Sales Price"] * df["Qty Sold"] #calculates the income of each product
        profit = income - (df["Cost Price"] * df["Qty Sold"]) #calculates the profit of each product
        df["Income"] = income
        df["Profit"] = profit #both lines add the income and profit as new columns to the database

        df1=df.groupby("Product ID")["Income"].sum()
        df1.reset_index()

        df1.plot(kind="bar",x="Product ID",y="Income",xlabel="Product",ylabel="Income",figsize=(10,8)) #plots the graph
        plt.title("Income Of Each Product") #changes the title
        plt.show()

        df1=df.groupby("Product ID")["Profit"].sum() #groups the products by the sum of all of their profits
        df1.reset_index()

        df1.plot(kind="bar",x="Product ID",y="Profit",xlabel="Product",ylabel="Profit",figsize=(10,8)) #replots the graph for the profit graph
        plt.title("Profit Of Each Product") #rechanges the title
        plt.show()
    except:
        print("There has been an unexpected error with this function. Please check the csv is stored in the same file as this program and try again.")



main_menu_choice = main_menu()


if main_menu_choice == 1:
    product_id = get_product_id()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
    calculate_total_sale (date_ID, product_id, start_date, end_date)

elif main_menu_choice == 2:
    sales_dif_cat()

elif main_menu_choice == 3:
    income_profit_products()

else:
    print("there are no options higher than 3")


