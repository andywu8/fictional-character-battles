import sqlite3

def create_record(character_1, character_2):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    statement = """ INSERT INTO records 
    (character_1, character_2, character_1_votes, character_2_votes)
    VALUES (?,?,?, ?)
    """
    print("statement:", statement)
    cur.execute(statement, [character_1, character_2, 0, 0])
    con.commit()
    con.close()

def create_record(character_1, character_2, email):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    statement = """ INSERT INTO records 
    (character_1, character_2, character_1_votes, character_2_votes, user_who_uploaded)
    VALUES (?,?,?,?,?)
    """
    print("statement:", statement)
    cur.execute(statement, [character_1, character_2, 0, 0, email])
    con.commit()
    con.close()
    return

def get_records():
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    statement = """ SELECT character_1, character_2, character_1_votes, character_2_votes FROM records
    """
    print("statement", statement)
    cur.execute(statement)
    records = cur.fetchall()
    print("records", records)
    con.commit()
    con.close()
    return records



def update_vote():
    return 