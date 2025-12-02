import os
import sqlite3
from config import DB_PATH

def create_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(256) UNIQUE NOT NULL,
            password VARCHAR(256) NOT NULL,
            first_name VARCHAR(256),
            last_name VARCHAR(256),
            nick_name VARCHAR(256)
            );
    """)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()