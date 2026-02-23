import sqlite3

from pathlib import Path
FILE_PATH=Path(__file__).parent
DB_PATH=(FILE_PATH/ "task_1_db.db")

def get_db_connection(): #connects to the database file
    conn=sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

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
        return self.Transaction

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