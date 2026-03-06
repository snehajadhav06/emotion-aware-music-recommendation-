import sqlite3
from datetime import datetime

def init_db():

    conn = sqlite3.connect("musicbot.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emotion TEXT,
        song TEXT,
        artist TEXT,
        feedback TEXT,
        timestamp DATETIME
    )
    """)

    conn.commit()
    conn.close()


def save_feedback(emotion, song, artist, feedback):

    conn = sqlite3.connect("musicbot.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO user_history (emotion, song, artist, feedback, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (emotion, song, artist, feedback, datetime.now()))

    conn.commit()
    conn.close()


def get_user_emotion_history():

    conn = sqlite3.connect("musicbot.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT emotion, song, feedback
        FROM user_history
        ORDER BY timestamp DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

