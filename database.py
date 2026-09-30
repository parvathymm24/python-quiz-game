import sqlite3

def create_database():
    # Connect to the database file
    conn = sqlite3.connect("quiz_score.db")
    cursor =conn.cursor()

    # To create scores table if it doesn't already exist
    cursor.execute("""
       CREATE TABLE IF NOT EXISTS scores(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT NOT NULL,
        score INTEGER NOT NULL,
        total_questions INTEGER NOT NULL,
        percentage INTEGER
       )
    """)

    # Save changes
    conn.commit()
    # Close the database
    conn.close()

def save_score(player_name,score,total_questions):
    # Calculate player's percentage
    percentage=int(score/total_questions*100)

    # Connect to the database file
    conn = sqlite3.connect("quiz_score.db")
    cursor=conn.cursor()

    #Insert quiz result to scores table
    cursor.execute(""" 
        INSERT INTO scores
        (player_name,score,total_questions,percentage)
         VALUES(?,?,?,?)
     """,(player_name,score,total_questions,percentage))

    # Save changes
    conn.commit()
    # Close the database
    conn.close()

