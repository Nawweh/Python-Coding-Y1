from flask import Flask, request, render_template
import sqlite3

from pathlib import Path
FILE_PATH=Path(__file__).parent
DB_PATH=(FILE_PATH/ "website_DB")

def get_db_connection(): #connects to the database file
    conn=sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Users(
                     USER_ID INTEGER PRIMARY KEY,
                     Username CHAR(16),
                     Password CHAR(16)
                     );''')
        conn.commit

def insert_data():
    with get_db_connection() as conn:
        conn.execute('''INSERT INTO Users (USER_ID, Username, Password) 
                     VALUES (1, 'bob', '1234'); ''')


app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with get_db_connection() as conn:
            login_details = conn.execute('''SELECT *
                         FROM Users''')
            
        for i in login_details:
            if i["Password"] == password:
                print("spogebob")


    return render_template('name.html')

if __name__ == '__main__':
    app.run(debug=True)