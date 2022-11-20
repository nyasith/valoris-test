import sqlite3
DATABASE_NAME = "valoris.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME, timeout=10)
    return conn

