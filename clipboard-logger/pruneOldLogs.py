import sqlite3
import sys
import datetime

DB_NAME = "clipboard.db"

def prune_logs_older_than(days=7):
    """
    Deletes rows from clipboard_logs where timestamp is older than `days` days.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Current time
    now = datetime.datetime.now()
    # Calculate cutoff datetime
    cutoff = now - datetime.timedelta(days=days)
    cutoff_str = cutoff.strftime("%Y-%m-%d %H:%M:%S")

    # Use SQLite datetime comparison (assuming your timestamps are in format YYYY-MM-DD HH:MM:SS)
    cursor.execute("""
        DELETE FROM clipboard_logs
        WHERE timestamp < ?
    """, (cutoff_str,))
    
    rows_deleted = cursor.rowcount  # number of rows removed
    conn.commit()
    conn.close()

    return rows_deleted

def main():
    """
    Usage: python prune_old_logs.py [days]
    Default is 7 days if not specified.
    """
    if len(sys.argv) > 1:
        try:
            days = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid integer for days.")
            sys.exit(1)
    else:
        days = 7

    removed = prune_logs_older_than(days)
    print(f"Removed {removed} entries older than {days} days.")

if __name__ == "__main__":
    main()
