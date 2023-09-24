import sqlite3

def create_record(character_1, character_2, anime_name, email):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    statement = """ INSERT INTO records 
    (character_1, character_2, character_1_votes, character_2_votes, anime_name, user_who_uploaded)
    VALUES (?,?,?,?,?, ?)
    """
    print("statement:", statement)
    cur.execute(statement, [character_1, character_2, 0, 0, anime_name, email])
    con.commit()
    con.close()
    return

def get_records():
    con = sqlite3.connect("test.db")
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
    print("statement", statement)
    cur.execute(statement)
    records = cur.fetchall()
    print("records", records)
    con.commit()
    con.close()
    return records

def update_vote(id, character):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    statement = """ Update records
    Set character_1_votes = character_1_votes + 1
    Where id = ? and character_1 =?
    """
    cur.execute(statement, (id, character))
    statement = """ Update records
    Set character_2_votes = character_2_votes + 1
    Where id = ? and character_2 =?
    """
    cur.execute(statement, (id, character))
    con.commit()
    con.close()
    return 
def get_comments():
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    statement = """
    SELECT comment_id, user_email, comment, uploaded_timestamp, record_id
    FROM comments 
    """
    cur.execute(statement)
    comments = cur.fetchall()
    print("comments", comments)
    con.commit()
    con.close()
    return comments

def insert_comment(email, comment, id):
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    statement = """ 
    INSERT INTO comments
    (user_email, comment, record_id)
    VALUES (?,?,?)
    """
    print("statement", statement)
    cur.execute(statement, [email, comment, id])
    con.commit()
    con.close()
    return

