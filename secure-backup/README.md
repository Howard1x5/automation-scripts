README.md 

# Secure File Backup Script

This script backs up a sensitive file with a timestamped filename, then automatically removes backups older than 30 days. It is designed to be simple, secure, and easy to schedule using cron.

---

## Features

- Copies a file from a specified location to a designated backup folder
- Appends a timestamp to every backup for version tracking
- Automatically deletes backup files older than 30 days
- Minimal and portable — pure Bash

---

## 🛠 Setup Instructions

### 1. Edit the Script

Before using the script, open `secure_backup.sh` and update these two lines:

```bash
SOURCE="$HOME/path/to/your/source/file.dat"
BACKUP_DIR="$HOME/path/to/your/backup/location"

Example:

SOURCE="$HOME/Documents/Secrets/mydatafile.dat"
BACKUP_DIR="$HOME/Backups/SecureFile/"

2. Test the Script

Make the script executable:

chmod +x secure_backup.sh

Then run it manually:

./secure_backup.sh

You should see output like:

Backup complete: /home/youruser/Backups/SecureFile/securefile_2025-03-22_14-55-31.dat

3. Test Auto-Pruning Logic

To confirm that backups older than 30 days are removed:

    Create a test file with an old modification time:

touch -d "35 days ago" ~/path/to/your/backup/location/securefile_fakeold.dat

    Run the script again:

./secure_backup.sh

    Verify that securefile_fakeold.dat was deleted:

ls ~/path/to/your/backup/location/

Only recent backups should remain.

4. Automate with Cron

To run the script automatically every day at 10:30 AM:

    Open your crontab:

crontab -e

    Add this line at the bottom:

# === Secure File Daily Backup ===
30 10 * * * /full/path/to/secure_backup.sh >> /home/youruser/backup.log 2>&1

# NOTE
## Make sure to replace /full/path/to/secure_backup.sh with the actual location of the script.