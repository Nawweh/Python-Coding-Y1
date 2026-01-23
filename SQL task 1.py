import sqlite3
import bcrypt

from pathlib import Path
FILE_PATH=Path(__file__).parent
DB_PATH=(FILE_PATH/ "task_1_db.db")

def get_db_connection(): #connects to the database file
    conn=sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Professors(
                     professor_id INTEGER PRIMARY KEY,
                     first_name CHAR(50),
                     last_name CHAR(50),
                     email CHAR(128)
                     );''')
        conn.commit

    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Courses(
                    course_id INTEGER PRIMARY KEY,
                    course_name CHAR(50),
                    course_desc CHAR(50),
                    professor_id INTEGER NOT NULL,
                    FOREIGN KEY (professor_id) REFERENCES Professors(professor_id)
                    );''')
        conn.commit
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Students(
                    student_id INTEGER PRIMARY KEY,
                    first_name CHAR(50),
                    last_name CHAR(50),
                     email CHAR(128),
                     date_of_birth DATE
                    );''')
        conn.commit
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS Enrollments(
                    enrollment_id INTEGER PRIMARY KEY,
                    enrollment_date DATE,
                    student_id INTEGER NOT NULL,
                    course_id INTEGER NOT NULL,
                    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
                    FOREIGN KEY (student_id) REFERENCES Students(student_id)
                    );''')
        conn.commit
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS login_details(
                    login_id INTEGER PRIMARY KEY,
                    hash_pass CHAR(128),
                    student_id INTEGER,
                    professor_id INTEGER,
                    FOREIGN KEY (student_id) REFERENCES Students(student_id),
                    FOREIGN KEY (professor_id) REFERENCES Professors(professor_id)
                    );''')
        conn.commit



def delete_table():
    with get_db_connection() as conn:
        conn.execute('''DROP TABLE login_details;''')
        conn.commit


def column_add():
    with get_db_connection() as conn:
        conn.execute('''ALTER TABLE Students
                     ADD student grades CHAR(2);''')
        conn.commit



def insert_data():
    with get_db_connection() as conn:
        conn.execute('''INSERT INTO Enrollments (enrollment_date, student_id, course_id) 
                     VALUES ('2025-09-03', 1, 3); ''')
        


def alter_table():
    with get_db_connection() as conn:
        conn.execute('''ALTER TABLE Students
                     RENAME COLUMN student TO student_grade''')



def update_data():
    with get_db_connection() as conn:
        conn.execute('''UPDATE Students
                     SET student='E'
                     WHERE student_id=3''')
        
        
def select_professor():
    Professor=input("give me the id of a professor: ")

    with get_db_connection() as conn:
        course = conn.execute('''SELECT *
                     FROM Courses
                     WHERE professor_id=(?)''',(Professor,)).fetchall()
        for i in course:
            print(f"the professor teaches {i['course_name']}")
        


def students_from_courses():
    course=input("give me the id of a course: ")

    with get_db_connection() as conn:
        student = conn.execute('''SELECT *
                     FROM Enrollments
                     WHERE student_id=(?)''',(course,)).fetchall()
        for i in student:
            print(f" student {i['student_id']} enrolls in {i['course_id']}")



def register_login():
    role=int(input("are you a student? (1)\nare you a professor? (2)\n"))

    if role==1:
            student_id=int(input("what is your student id?: "))

            password=input("create a password: ")

            password=password.encode("utf-8")
            salt=bcrypt.gensalt()
            hash=bcrypt.hashpw(password, salt)

            
            with get_db_connection() as conn:
                conn.execute('''INSERT INTO login_details (hash_pass, student_id) 
                            VALUES (?,?); ''',(hash, student_id))
                
    else: 

        professor_id=int(input("what is your professor id?: "))

        password=input("create a password: ")

        password=password.encode("utf-8")
        salt=bcrypt.gensalt()
        hash=bcrypt.hashpw(password, salt)

        
        with get_db_connection() as conn:
            conn.execute('''INSERT INTO login_details (hash_pass, professor_id) 
                        VALUES (?,?); ''',(hash, professor_id))



def student_grade_ui():
    run=True
    while run==True:
        choice=int(input("would you like to alter grades (1) or exit the interface (2)\n"))
        if choice==1:
            student_id=int(input("give the id of the student you would like to alter the grade of?: "))
            student_grade=input("what is the grade that you would like to input?: ")
            with get_db_connection() as conn:
                conn.execute('''UPDATE Students
                     SET student_grade=(?)
                     WHERE student_id=(?)''',(student_grade, student_id))
        else:
            run=False

def check_login():
    role=int(input("are you a student? (1)\nare you a professor? (2)\n"))

    if role==1:
        stu_id_input=int(input("what is your student id?: "))

        with get_db_connection() as conn:
            student = conn.execute('''SELECT student_id
                        FROM login_details
                        WHERE student_id=(?)''',(stu_id_input,)).fetchone()
            student_id=student[0]
            
            hash_pass = conn.execute('''SELECT hash_pass
                        FROM login_details
                        WHERE student_id=(?)''',(stu_id_input,)).fetchone()
            hash=hash_pass[0]
            
        password2=input("input your password: ")
        password2=password2.encode("utf-8")
        hash2=bcrypt.checkpw(password2, hash)


        if student_id==stu_id_input:
            if hash2==True:
                print("access granted")
            else:
                print("access denied")

        else:
                print("access denied")



    else:
        prof_id_input=int(input("what is your professor id?: "))

        with get_db_connection() as conn:
            professor = conn.execute('''SELECT professor_id
                        FROM login_details
                        WHERE professor_id=(?)''',(prof_id_input,)).fetchone()
            professor_id=professor[0]
            
            hash_pass = conn.execute('''SELECT hash_pass
                        FROM login_details
                        WHERE professor_id=(?)''',(prof_id_input,)).fetchone()
            hash=hash_pass[0]
            
        password2=input("input your password: ")
        password2=password2.encode("utf-8")
        hash2=bcrypt.checkpw(password2, hash)


        if professor_id==prof_id_input:
            if hash2==True:
                print("access granted")
            else:
                print("access denied")

        else:
                print("access denied")



def report_card():
    student_id=int(input("what is your student id?: "))
    with get_db_connection() as conn:
        stu_grade = conn.execute('''SELECT student_grade
                        FROM login_details
                        WHERE student_id=(?)''',(student_id,)).fetchone()
    print(f"your grade is {stu_grade[0]}")

report_card()