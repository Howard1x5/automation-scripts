import sqlite3
import sys

DB_NAME = "clipboard.db"

def query_logs(order_by="timestamp"):
    """
    Retrieves rows from clipboard_logs, sorted by the given field.
    order_by can be 'timestamp' or 'alphabetical'.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    if order_by == "alphabetical":
        cursor.execute("SELECT id, content, timestamp FROM clipboard_logs ORDER BY content ASC;")
    else:
        # Default to timestamp ascending
        cursor.execute("SELECT id, content, timestamp FROM clipboard_logs ORDER BY timestamp ASC;")
    
    rows = cursor.fetchall()
    conn.close()
    
    return rows

def main():
    """
    Usage:
      python query_logs.py [alphabetical|timestamp]
    Defaults to 'timestamp' if no arg is given.
    """
    if len(sys.argv) > 1:
        sort_mode = sys.argv[1]  # "alphabetical" or "timestamp"
    else:
        sort_mode = "timestamp"
    
    valid_modes = ["alphabetical", "timestamp"]
    if sort_mode not in valid_modes:
        print(f"Invalid mode. Valid options: {valid_modes}")
        sys.exit(1)
    
    logs = query_logs(order_by=sort_mode)
    # Print a basic header
    print(f"{'ID':<5} {'CONTENT':<50} {'TIMESTAMP':<20}")
    print("-" * 80)
    for row in logs:
        row_id, content, tstamp = row
        print(f"{row_id:<5} {content:<50} {tstamp:<20}")

if __name__ == "__main__":
    main()
