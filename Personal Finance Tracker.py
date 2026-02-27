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
                budget_info=conn.execute('''SELECT budget FROM Budgets
                            WHERE category = (?)''',(self.category,)).fetchone()
        except:
            print("sorry, there has been an error in the budget calculation, please add the right category and try again")
                
        budget=budget_info["budget"]+self.amount

        with get_db_connection() as conn:
            conn.execute('''UPDATE Budgets
                     SET budget=(?)
                     WHERE category=(?)''',(budget, self.category))
        
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

create_DB()

def Income_Input():
    valid=False
    count=1
    while valid==False:
        type="Income"
        amount=float(input("\nwhat is the cost of the transaction: "))
        date=input("what is the data that this happened (input as Y-M-D): ")
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
            valid==False
        else:
            valid==True
            print("Input accepted")

    Income_1=Income(type, amount, date, category, description)
    trans_add_DB(type,amount,date,category,description)

    clear_tui()

def Expense_Input():
    valid=False
    count=1
    while valid==False:
        type="Expense"
        amount=float(input("\nwhat is the cost of the transaction: "))*-1
        date=input("what is the data that this happened (input as Y-M-D): ")
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

    Expense_1=Expense(type, amount, date, category, description)
    trans_add_DB(type,amount,date,category,description)
    clear_tui()

    Expense_1.calc_budget()
    

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
    add_budget(category, budget)

    clear_tui()

def add_budget(category, budget):
    with get_db_connection() as conn:
        conn.execute('''INSERT INTO Budgets(category, budget)
                            VALUES (?,?)''', (category, budget))


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
        conn.execute('''INSERT INTO Categories(name,)
                            VALUES (?)''', (category,))
        print("Category added")

    clear_tui()

        
def trans_add_DB(type,amount,date,category,description):
        with get_db_connection() as conn:
            conn.execute('''INSERT INTO Transactions(type, amount, date, description, category)
                         VALUES (?,?,?,?,?)''', (type,amount,date,description,category))
            conn.commit()

def view_categories():
    print("okay, here you go")
    time.sleep(1)
    with get_db_connection() as conn:
        categories=conn.execute('''SELECT * FROM Categories''').fetchall()
    for i in categories:
        print(i["name"])
    temp=input("\npress ENTER to leave\n")
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

        case 7:
            Register_Category()

        case 8:
            view_categories()

        
        case 9:
            print("okay, ending program")
            time.sleep(1)
            run=False