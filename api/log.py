import sqlite3
import os
from datetime import datetime

DB_PATH = "data/requests.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            sepal_length REAL,
            sepal_width REAL,
            petal_length REAL,
            petal_width REAL,
            prediction INTEGER
        )
    """)
    conn.commit()
    conn.close()

def log_prediction(sl, sw, pl, pw, prediction):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO predictions (timestamp, sepal_length, sepal_width, petal_length, petal_width, prediction)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (datetime.utcnow().isoformat(), sl, sw, pl, pw, prediction)
    )
    conn.commit()
    conn.close()
