from flask import Flask, request, render_template, redirect

import sqlite3
import bcrypt

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

create_tables()

def insert_data(username, password):
    with get_db_connection() as conn:
        conn.execute('''INSERT INTO Users (Username, Password) 
                     VALUES (?,?); ''',(username, password))
        



app = Flask(__name__)


@app.route("/")
def landing():
    return redirect("/register")


@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if len(username) + len(password) !=0:

            password=password.encode("utf-8")
            salt=bcrypt.gensalt()
            hash_pass=bcrypt.hashpw(password, salt)

            insert_data(username, hash_pass)
            return redirect("/login")

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        app.logger.info(f"username is {username}. Password is {password}")


        with get_db_connection() as conn:
            login_details = conn.execute('''SELECT *
                         FROM Users''')
            
        if len(username) + len(password) !=0:


            for i in login_details:
                encoded_password=password.encode("utf-8")
                hash_pass = i["Password"]
                hash=bcrypt.checkpw(encoded_password, hash_pass)

                if i["Username"] == username and hash == True:
                        
                    return render_template("login_success.html")
            return render_template("login_fail.html")

    

    return render_template('name.html')

@app.route('/ham_quiz', methods=['GET', 'POST'])
def ham_quiz():

    return render_template('HAM_QUIZZ!!!.html')

if __name__ == '__main__':
    app.run(debug=True)