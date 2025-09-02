import sqlite3, os
DB_FILE = "chat_log.db"

def get_conn():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS log (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            session TEXT,
            ts      TEXT,
            question TEXT,
            answer   TEXT,
            ok       INTEGER DEFAULT NULL
        )
    """)
    conn.commit()
    return conn
