import sqlite3
import os

class Database:

    def __init__(self):
        # Use '/tmp' directory for SQLite on Vercel to enable read/write access
        db_path = '/tmp/users.db' if 'VERCEL' in os.environ else 'users.db'
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    email TEXT PRIMARY KEY,
                    name TEXT,
                    password TEXT
                )
            ''')

    def insert(self, name, email, password):
        try:
            with self.conn:
                self.conn.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            return 1
        except sqlite3.IntegrityError:
            return 0

    def search(self, email, password):
        cursor = self.conn.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        return cursor.fetchone() is not None
