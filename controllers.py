import sqlite3
import psycopg2
import os

def create_record(character_1, character_2, anime_name, email):
    # con = sqlite3.connect("test.db")
    con = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD")
    )
    cur = con.cursor()
    statement = """ INSERT INTO records 
    (character_1, character_2, character_1_votes, character_2_votes, anime_name, user_who_uploaded)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    # print("statement:", statement)
    cur.execute(statement, [character_1, character_2, 0, 0, anime_name, email])
    con.commit()
    con.close()
    return

def get_records():
    # con = sqlite3.connect("test.db")
    con = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD")
    )
    cur = con.cursor()
    statement = """ SELECT 
    id, 
    character_1, 
    character_2, 
    character_1_votes, 
    character_2_votes, 
    anime_name, 
    character_1_votes + character_2_votes as total_votes
    FROM records
    ORDER BY total_votes DESC
    """
    # print("statement", statement)
    cur.execute(statement)
    records = cur.fetchall()
    print("records", records)
    con.commit()
    con.close()
    return records

def update_vote(id, character):
    con = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD")
    )
    cur = con.cursor()
    statement = """ Update records
    Set character_1_votes = character_1_votes + 1
    Where id = %s and character_1 =%s
    """
    cur.execute(statement, (id, character))
    statement = """ Update records
    Set character_2_votes = character_2_votes + 1
    Where id = %s and character_2 =%s
    """
    cur.execute(statement, (id, character))
    con.commit()
    con.close()
    return 
def get_comments(id):
    # con = sqlite3.connect("test.db")
    con = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD")
    )
    cur = con.cursor()
    statement = """
    SELECT comment_id, user_email, comment, uploaded_timestamp, record_id
    FROM comments 
    WHERE record_id = %s
    """
    cur.execute(statement, [id])
    comments = cur.fetchall()
    print("comments", comments)
    con.commit()
    con.close()
    return comments

def insert_comment(email, comment, id):
    # con = sqlite3.connect("test.db")
    con = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD")
    )
    cur = con.cursor()
    statement = """ 
    INSERT INTO comments
    (user_email, comment, record_id)
    VALUES (%s,%s,%s)
    """
    # print("statement", statement)
    cur.execute(statement, [email, comment, id])
    print("inserting comment", comment)
    con.commit()
    con.close()
    return

