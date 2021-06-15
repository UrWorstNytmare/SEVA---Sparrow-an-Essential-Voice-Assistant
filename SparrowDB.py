import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Sparrow.db")

def create_connection():
    connection = sqlite3.connect(db_path)
    return connection

def get_ques_and_ans():

    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM database")

    return cur.fetchall()

def insert_ques_and_ans(question, answer):
    con = create_connection()
    cur = con.cursor()

    query = "INSERT INTO database values('"+question+"', '"+answer+"')"
    cur.execute(query)
    con.commit()

def get_answer_from_database(question):

    rows = get_ques_and_ans()
    answer = ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break

    return answer

#get_ques_and_ans()