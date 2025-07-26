import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("data/predictions.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            sl REAL,
            sw REAL,
            pl REAL,
            pw REAL,
            prediction INTEGER
        )
    """)
    conn.commit()
    conn.close()

def log_prediction(sl, sw, pl, pw, prediction):
    conn = sqlite3.connect("data/predictions.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO logs (timestamp, sl, sw, pl, pw, prediction)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (datetime.utcnow().isoformat(), sl, sw, pl, pw, prediction))
    conn.commit()
    conn.close()
