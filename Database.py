import sqlite3
from datetime import datetime

DB_NAME = "brain_tumor.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_name TEXT NOT NULL,
            prediction TEXT NOT NULL,
            confidence REAL NOT NULL,
            advice TEXT NOT NULL,
            prediction_time TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_prediction(image_name, prediction, confidence, advice):
    conn = get_connection()
    cursor = conn.cursor()

    prediction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO predictions (image_name, prediction, confidence, advice, prediction_time)
        VALUES (?, ?, ?, ?, ?)
    """, (image_name, prediction, confidence, advice, prediction_time))

    conn.commit()
    conn.close()


def fetch_all_predictions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, image_name, prediction, confidence, advice, prediction_time
        FROM predictions
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_prediction(record_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM predictions WHERE id = ?", (record_id,))

    conn.commit()
    conn.close()


def clear_all_predictions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM predictions")

    conn.commit()
    conn.close()


# Create table automatically when file runs/imports
create_table()