import sqlite3

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
    

create_tables()

