import time
import pyperclip
import sqlite3
from datetime import datetime

DB_NAME = "clipboard.db"

def initialize_db(db_name=DB_NAME):
    """Create the database and table if it doesn't already exist."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clipboard_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

def log_clipboard_content(content, db_name=DB_NAME):
    """Insert a new clipboard record into the database."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO clipboard_logs (content, timestamp)
        VALUES (?, ?);
    """, (content, time_str))
    
    conn.commit()
    conn.close()

def main():
    """Main loop to monitor the clipboard and log new entries."""
    initialize_db()

    last_content = ""
    while True:
        current_content = pyperclip.paste()
        
        # If there's something in the clipboard and it's new content, log it.
        if current_content and current_content != last_content:
            log_clipboard_content(current_content)
            last_content = current_content
        
        time.sleep(1)  # check clipboard every 1 second

if __name__ == "__main__":
    main()
