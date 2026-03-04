import sqlite3
import time
from os import system
from os import name as os_name
def clear_tui(toggle=True):
    if os_name == "nt":
        system("cls")
    else:
        system("clear")

from pathlib import Path
FILE_PATH=Path(__file__).parent
DB_PATH=(FILE_PATH/ "Finance_Tracker_DB.db")



def get_db_connection(): #connects to the database file
    conn=sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn



def create_DB(): #creates the database

    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Categories(
                    category_id INTEGER PRIMARY KEY,
                    name CHAR(50)
                    );''')
        conn.commit

    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Transactions(
                    transaction_id INTEGER PRIMARY KEY,
                    type CHAR(10),
                    amount REAL,
                    date CHAR(15),
                    description CHAR(200),
                    category CHAR(50)
                    );''')
        conn.commit
        
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Budgets(
                    budget_id INTEGER PRIMARY KEY,
                    category CHAR(50),
                    budget REAL
                    );''')
        conn.commit



class FinanceTracker_:
    def __init__(self,transaction):
        self.transaction=[]
        for i in transaction:
            self.transaction.append(i)
        


class Transaction_:
    def __init__(self,amount,date,category,description):
        self.amount=amount
        self.date=date
        self.category=category
        self.description=description

        self.Transaction=[self.amount, self.date, self.category, self.description]
    


    def print_transaction(self):

        return [self.amount, self.date, self.category, self.description]
    


    def calc_budget(self):

        try:
            with get_db_connection() as conn:
                budget_info=conn.execute('''SELECT budget,category FROM Budgets
                            WHERE category = (?)''',(self.category,)).fetchone()
        except:
            print("sorry, there has been an error in the budget calculation, please add the right category and try again")

        print(budget_info["budget"])
        budget=budget_info["budget"]+self.amount

        with get_db_connection() as conn:
            conn.execute('''UPDATE Budgets
                     SET budget=(?)
                     WHERE category=(?)''',(budget, self.category))
            


    def is_over_budget(self):
        with get_db_connection() as conn:
                budget_info=conn.execute('''SELECT budget,category FROM Budgets
                            WHERE category = (?)''',(self.category,)).fetchone()
        
        budget=budget_info["budget"]
        
        if budget<0:
            print(f"{self.category} has exceeded budget.")


class Budget_:
    def __init__(self,category,budget_amount):
        self.category=category
        self.budget_amount=budget_amount

        

class Income(Transaction_):
    def __init__(self, amount, date, category, description, type):
        self.type=type
        super().__init__(amount, date, category, description)

class Expense(Transaction_):
    def __init__(self, amount, date, category, description, type):
        self.type=type
        super().__init__(amount, date, category, description)



def Income_Input():
    valid=False
    count=1
    while valid==False:
        type="Income"
        amount=float(input("\nwhat is the cost of the transaction (input as 0.00): "))*-1
        date=input("what is the date the transaction happened (input as YYYY-MM-DD): ")
        category=input("what is the category of the transaction: ")
        description=input("give a description of the transaction (leave this blank for no description): ")

        with get_db_connection() as conn:
            categories = conn.execute('''SELECT * FROM Categories''').fetchall()

        for i in categories:
            category_name=i["name"]
            if category_name==category:
                count=0

        if count==1:
            print("this is invalid, please try again")
            time.sleep(1)
            valid=False
        else:
            valid=True
            print("Input accepted")
            time.sleep(.5)

    Income_1=Income(amount, date, category, description, type)
    Transaction_Add_DB(type,amount,date,category,description)

    clear_tui()



def Expense_Input():
    valid=False
    count=1
    while valid==False:
        type="Expense"
        amount=float(input("\nwhat is the cost of the transaction (input as 0.00): "))*-1
        date=input("what is the date the transaction happened (input as YYYY-MM-DD): ")
        category=input("what is the category of the transaction: ")
        description=input("give a description of the transaction (leave this blank for no description): ")

        with get_db_connection() as conn:
            categories = conn.execute('''SELECT * FROM Categories''').fetchall()

        for i in categories:
            category_name=i["name"]
            if category_name==category:
                count=0

        if count==1:
            print("this is invalid, please try again")
            time.sleep(1)
            valid=False
        else:
            valid=True
            print("Input accepted")
            time.sleep(.5)

    Expense_1=Expense(amount, date, category, description, type)
    Transaction_Add_DB(type,amount,date,category,description)
    clear_tui()

    Expense_1.calc_budget()
    Expense_1.is_over_budget()
    


def Set_Budget():
    count=1
    while count==1:

        category=input("\nwhat category do you want to set a budget for: ")
        budget=float(input("what is the budget: "))

        with get_db_connection() as conn:
                categories = conn.execute('''SELECT * FROM Categories''').fetchall()

        for i in categories:
            category_name=i["name"]
            if category_name==category:
                print("Input accepted")
                count=0

        if count==1:
            print("this is invalid, please try again")

    budget_1=Budget_(category, budget)
    Add_Budget(category, budget)

    clear_tui()



def Add_Budget(category, budget):
    with get_db_connection() as conn:
        conn.execute('''INSERT INTO Budgets(category, budget)
                            VALUES (?,?)''', (category, budget))
        


def Update_Budget():
    category=input("\nwhat category do you want to update the budget for: ")
    budget=float(input("what is the budget: "))
    with get_db_connection() as conn:
        conn.execute('''UPDATE Budgets
                     SET budget=(?)
                     WHERE category=(?)''',(budget,category))



def Register_Category():
    count=0
    while count==0:
        category=input("add a category: ")

        with get_db_connection() as conn:
                    categories = conn.execute('''SELECT * FROM Categories''').fetchall()

        for i in categories:
            category_name=i["name"]
            if category_name==category:
                print("This category already exists, please try again")
                count=0
            else:
                count=1
            
    with get_db_connection() as conn:
        conn.execute('''INSERT INTO Categories (name)
                        VALUES (?)''', (category,))
        print("Category added")

    clear_tui()



def View_Transactions():
    print("okay, here are your transactions")
    time.sleep(1)
    with get_db_connection() as conn:
        Transactions=conn.execute('''SELECT * FROM Transactions''').fetchall()
    for i in Transactions:
        print(f'''Transaction ID: {i['transaction_id']}
        Transaction type: {i['type']}
        Cost of transaction: {i['amount']}
        Date: {i['type']}
        Added notes: {i['type']}
        Category of transaction: {i['type']}\n''')
    
    temp=input("\npress any key to leave\n")


        
def Transaction_Add_DB(type,amount,date,category,description):
        with get_db_connection() as conn:
            conn.execute('''INSERT INTO Transactions(type, amount, date, description, category)
                         VALUES (?,?,?,?,?)''', (type,amount,date,description,category))
            conn.commit()



def Generate_Report():
    Expenses=[]
    Incomes=[]
    net_balance=0.00

    min_date=input("what is the minimum date of the range of transactions you would like to look at? (input as YYYY-MM-DD): ")
    max_date=input("what is the maximum date of the range of transactions you would like to look at? (input as YYYY-MM-DD): ")

    min_date_y=min_date[0:4]
    min_date_m=min_date[5:7]
    min_date_d=min_date[8:10]

    min_date=min_date_y+min_date_m+min_date_d
    min_date=int(min_date)

    max_date_y=max_date[0:4]
    max_date_m=max_date[5:7]
    max_date_d=max_date[8:10]

    max_date=max_date_y+max_date_m+max_date_d
    max_date=int(max_date)


    with get_db_connection() as conn:

        transaction_dates=conn.execute('''SELECT * FROM Transactions''').fetchall()

        expenses=conn.execute('''SELECT * FROM Transactions
                              WHERE type=(?)''',("Expense",)).fetchall()
        
        incomes=conn.execute('''SELECT * FROM Transactions
                              WHERE type=(?)''',("Income",)).fetchall()
        
        categories=conn.execute('''SELECT * FROM Categories''').fetchall()

        budgets=conn.execute('''SELECT * FROM Budgets''')


    print("Transaction summary: \n")
    for i in transaction_dates:
        date=i["date"]
        date_y=date[0:4]
        date_m=date[5:7]
        date_d=date[8:10]

        date=date_y+date_m+date_d
        date=int(date)


        if date>min_date and date<max_date:
            print(f'''Transaction ID: {i['transaction_id']}
            Transaction type: {i['type']}
            Cost of transaction: {i['amount']}
            Date: {i['date']}
            Added notes: {i['description']}
            Category of transaction: {i['category']}\n''')

    temp=input("Press any key to see Net Balance: ")
        
    for i in incomes:
        net_balance=net_balance+i["amount"]
        
    print(f"\nnet balance: {net_balance}")

    temp=input("\nPress any key to see a breakdown of the incomes and expenses for each category: ")

    for i in categories:
        category=i["name"]
        print(f"{category}:")

        for x in expenses:
            expense_category=x["category"]
            if expense_category==category:
                print(f'''\nTransaction type: Expense
                        Amount: {x["amount"]}
                        Date: {x["date"]}''')
                
        for j in incomes:
            income_category=j["category"]
            if income_category==category:
                print(f'''\nTransaction type: Income
                        Amount: {x["amount"]}
                        Date: {x["date"]}''')
                
    temp=input("\nPress any key to see if any budgets have been exceeded: ")
    
    for i in budgets:
        budget=i["budget"]
        if budget<0:
            print(f"{i[category]} is over budget by {budget*-1}")



def View_Categories():
    print("okay, here you go")
    time.sleep(1)
    with get_db_connection() as conn:
        categories=conn.execute('''SELECT * FROM Categories''').fetchall()
    for i in categories:
        print(i["name"])
    temp=input("\npress any key to leave\n")
    clear_tui()



run=True
while run==True:
    options=0
    options=int(input('''
What do you want to do?
1: Income
2: Expense
3: Set budgets
4: Update budgets
5: View all transactions
6: Generate a report
7: Create a category
8: view categories
9: Leave
                          
'''))
    clear_tui()
    match options:
        case 1:
            Income_Input()
        
        case 2:
            Expense_Input()

        case 3:
            Set_Budget()
        
        case 4:
            Update_Budget()
        
        case 5:
            View_Transactions()

        case 6:
            Generate_Report()

        case 7:
            Register_Category()

        case 8:
            View_Categories()

        
        case 9:
            print("okay, ending program")
            time.sleep(1)
            run=False