import sqlite3

from os import system
from os import name as os_name
def clear_tui(toggle=True):
    if os_name == "nt":
        system("cls")
    else:
        system("clear")

from pathlib import Path
FILE_PATH=Path(__file__).parent
DB_PATH=(FILE_PATH/ "Finance_Tracker_DB")

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
                    category_id INTEGER NOT NULL,
                    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
                    );''')
        conn.commit
        
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Budgets(
                    budget_id INTEGER PRIMARY KEY,
                    name CHAR(50),
                    budget REAL,
                    category_id INTEGER NOT NULL,
                    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
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
    type="Income"
    amount=float(input("what is the cost of the transaction: "))
    date=input("what is the data that this happened (input as Y-M-D): ")
    category=input("what is the category of the transaction: ")
    description=input("give a description of the transaction (leave this blank for no description): ")
    Income_1=Income(amount, date, category, description, type)

def Expense_Input():
    type="Expense"
    amount=float(input("what is the cost of the transaction: "))
    date=input("what is the data that this happened (input as Y-M-D): ")
    category=input("what is the category of the transaction: ")
    description=input("give a description of the transaction (leave this blank for no description): ")
    Expense_1=Expense(amount, date, category, description, type)

def Set_Budget():
    category=input("what category do you want to set a budget for:")
    budget=float(input("what is the budget: "))
    budget_1=Budget_(category, budget)

def main():
    run=True
    while run==True:
        options=int(input('''
What do you want to do?
1: Income
2: Expense
3: Set budgets
4: Update budgets
5: View all transactions
6: Generate a report
7: Leave
                          
'''))
        clear_tui()
        
        if options==1:
            Income_Input()

        elif options==2:
            Expense_Input()

        elif options==3:
            Set_Budget()

        elif options==7:
            run=False

create_DB()
main()