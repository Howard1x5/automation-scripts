# Clipboard Logger with SQLite

This project contains a small Python tool that continuously monitors your system clipboard and logs new text entries into a local SQLite database. It’s useful for reviewing or searching past clipboard history.

---

## Features

- **Real-Time Monitoring**: Detects clipboard changes in real time.
- **SQLite Storage**: Logs entries in a lightweight database (`clipboard.db`), with timestamps for each entry.
- **Query and Sorting**: Includes a script to query logs, sorted by date or alphabetically.
- **Pruning Old Data**: An optional script allows you to delete entries older than a specified number of days.
- **(Optional) Sensitive Data Masking**: Demonstrates how to redact or skip certain data patterns (e.g., passwords).

---

## Requirements

- **Python 3.7+**  
- **pyperclip** for clipboard access (`pip install pyperclip`)
- **sqlite3** (builtin with Python)
- *(Optional)* [pynput](https://pypi.org/project/pynput/) if you want to add hotkey functionality

Install dependencies via:

```bash
pip install pyperclip

Or, if you have a requirements.txt:

pip install -r requirements.txt

Usage
1. Run the Clipboard Logger

    Clone or download this repository.

    Navigate to the folder (e.g., clipboard-logger).

    (Optional) Create & activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install pyperclip

Run the logger:

    python clipboard_logger.py

    This starts an infinite loop that checks the clipboard every second.

To stop the script at any time, press Ctrl + C in the terminal window.
2. Query Logs

Use query_logs.py to list entries from the database in different orders:

python query_logs.py [alphabetical|timestamp]

    alphabetical: Sorts entries by the content column.

    timestamp (default): Sorts entries by the time they were logged (oldest to newest).

For example:

python query_logs.py alphabetical

displays all entries sorted by their text content alphabetically.
3. Prune Old Logs

Use prune_old_logs.py to remove entries older than a specified number of days:

python prune_old_logs.py [days]

    If you provide no argument, it defaults to 7 days.

    For example:

    python prune_old_logs.py 30

    will delete entries older than 30 days.

Viewing Logs Directly

If preferred, you can still open clipboard.db via the SQLite CLI:

sqlite3 clipboard.db "SELECT * FROM clipboard_logs;"

    Sort by content alphabetically:

sqlite3 clipboard.db "SELECT * FROM clipboard_logs ORDER BY content ASC;"

Sort by timestamp:

    sqlite3 clipboard.db "SELECT * FROM clipboard_logs ORDER BY timestamp ASC;"

Roadmap

    Duplicate Filtering: Optionally skip logging repeated content within a short time window.

    Sensitive Data Masking: Detect and redact potential secrets or high-entropy strings.

    Hotkey Support: Add a hotkey to remove the last entry from the DB if you accidentally capture a password.

    Background Service: Turn this script into a system daemon so it runs without an open terminal.

    GUI: Create a small interface to display, search, or recopy past entries.