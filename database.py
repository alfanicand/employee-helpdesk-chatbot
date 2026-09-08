import sqlite3
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "employee_chatbot.db"


def get_connection():
    """Membuat koneksi ke database SQLite."""
    return sqlite3.connect(DATABASE_PATH)


def get_all_faq():
    """Mengambil seluruh data FAQ dari database."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT intent, keywords, answer
        FROM faq
        ORDER BY id
    """)

    faq_data = cursor.fetchall()
    connection.close()

    return faq_data


def save_chat_log(user_message, detected_intent, bot_response):
    """Menyimpan percakapan ke database."""
    connection = get_connection()
    cursor = connection.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO chat_logs (
            user_message,
            detected_intent,
            bot_response,
            created_at
        )
        VALUES (?, ?, ?, ?)
    """, (
        user_message,
        detected_intent,
        bot_response,
        created_at
    ))

    connection.commit()
    connection.close()
