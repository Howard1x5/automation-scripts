```
# Clipboard Logger with SQLite

This project contains a small Python script that continuously monitors your system clipboard and logs any new text entries into a local SQLite database. It’s useful for reviewing or searching past clipboard history.

---

## Features

- **Real-Time Monitoring**: The script detects clipboard changes in real time.
- **SQLite Storage**: Logs are stored in `clipboard.db`, including timestamps for each entry.
- **Easy Queries**: You can sort or filter logs by date or alphabetically (using either the included utility functions or SQLite CLI).
- **Cross-Platform**: Works on Windows, macOS, and Linux (with [pyperclip](https://pypi.org/project/pyperclip/)).

---

## Requirements

- Python 3.7+  
- [pyperclip](https://pypi.org/project/pyperclip/) library for clipboard access  
- SQLite (built into Python’s standard library)

Install dependencies via:

```
pip install pyperclip
```

Or if you have a `requirements.txt`:

```
pip install -r requirements.txt
```

---

## Usage

1. **Clone/Download** this repository.
2. **Navigate** to the `clipboard-logger` folder (or wherever you placed the script).
3. **Run** the Python script:
   ```
   python clipboard_logger.py
   ```
   The script will:
   - Initialize/verify `clipboard.db` exists.
   - Enter an infinite loop, checking the clipboard for changes.
   - Insert new clipboard text and a timestamp into the database whenever it detects new content.
4. **Stop** the script at any time by pressing `Ctrl + C`.

---

## Viewing Logs

1. **Directly via SQLite CLI**:
   ```
   sqlite3 clipboard.db "SELECT * FROM clipboard_logs;"
   ```
   - Sort by content alphabetically:
     ```
     sqlite3 clipboard.db "SELECT * FROM clipboard_logs ORDER BY content ASC;"
     ```
   - Sort by date/time:
     ```
     sqlite3 clipboard.db "SELECT * FROM clipboard_logs ORDER BY timestamp ASC;"
     ```
2. **Python Utility**:
   - You can create or use a separate Python script to query and sort the logs (examples in the repo).
   - Example snippet:
     ```python
     import sqlite3
     def get_logs(db_name="clipboard.db"):
         conn = sqlite3.connect(db_name)
         cursor = conn.cursor()
         cursor.execute("SELECT * FROM clipboard_logs ORDER BY timestamp ASC;")
         rows = cursor.fetchall()
         conn.close()
         return rows
     ```

---

## Roadmap

- **Duplicate Filtering**: Optionally skip logging repeated content within a set timeframe.
- **Sensitive Data Masking**: Detect and redact potential secrets (e.g., passwords).
- **GUI or CLI Query**: Add a user-friendly interface for searching, sorting, or exporting logs.
- **Tray/Background Service**: Convert to a daemon or system tray app for always-on logging without a visible terminal.

---