import unittest
import sqlite3
from database import create_database, save_score

class TestDatabase(unittest.TestCase):

    def test_database_creation(self):
        create_database()

        conn=sqlite3.connect("quiz_score.db")
        cursor=conn.cursor()

        cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name='scores'
    """)
        result= cursor.fetchone()
        conn.close()
        self.assertIsNotNone(result)

    def test_save_score(self):
        create_database()

        save_score("Test User",4,5)
        conn = sqlite3.connect("quiz_score.db")
        cursor=conn.cursor()

        cursor.execute("""
        SELECT player_name,score,total_questions, percentage
        FROM scores
        WHERE player_name=?
        ORDER BY id DESC
        LIMIT 1
    """, ("Test User",))
        result=cursor.fetchone()
        conn.close()
        self.assertEqual(result,("Test User",4,5,80))
if __name__=="__main__":
    unittest.main()



