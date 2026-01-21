import sqlite3

from pathlib import Path
FILE_PATH=Path(__file__).parent
DB_PATH=(FILE_PATH/ "practice_db.db")

def get_db_connection(): #connects to the database file
    conn=sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS company(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL, 
                    age INT NOT NULL,
                    address CHAR(50),
                    salary REAL
                    );''')
        conn.commit()

    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS job(
                     jobID INTEGER PRIMARY KEY,
                     title TEXT NOT NULL,
                     bossID INT,
                     FOREIGN KEY (bossID) REFERENCES company(id)
                     ); ''')
        conn.commit()

def insert_data():
    with get_db_connection() as conn:
        conn.execute('''INSERT INTO company (name, age, address, salary) 
                     VALUES ('kyle', 52, '123 poop drive', 0.50); ''')
        
        for i in range(2):
            name = input("give me your name NOW: ")
            age = int(input("what is your age?: "))
            address = input("what is your address?: ")
            salary = input("what is your salary?: ")
            
            conn.execute('''INSERT INTO company(name, age, address, salary)
                         VALUES (?,?,?,?)''', (name,age,address,salary))
            
            conn.execute('''INSERT INTO job(title, bossID) VALUES ("chief toastie maker", 1) ''')

def select_employees():
    with get_db_connection() as conn:
        user_id = 1
        employees = conn.execute('''SELECT name, age, address, salary FROM company
                                 WHERE id = (?) ''',(user_id,)).fetchone()
        print(f"the name is {employees['name']}, they are {employees['age']} old. \n They earn an amazing {employees['salary']} per year")

def select_all_employees():
    with get_db_connection() as conn:
        
        employees = conn.execute('''SELECT * FROM company''').fetchall()
        for i in employees:
            print(f"the name is {i['name']}, they are {i['age']} old. \n They earn an amazing {i['salary']} per year")


select_employees()

