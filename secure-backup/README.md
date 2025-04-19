README.md 

# Secure File Backup Script

This script backs up a sensitive file with a timestamped filename and includes an auto-pruning safeguard to delete old backups only when enough backups exist. It's designed for privacy-conscious automation on Linux/macOS systems.

---

## Features

- Copies a sensitive file to a backup directory with a timestamp
- Automatically creates the backup directory if missing
- Appends timestamp to every backup for version control
- Automatically deletes backups older than 30 days, but only if 30 or more backups exist
- Portable — written in pure Bash

---

## Setup Instructions

### 1. Edit the Script

Before using the script, open `secure_backup.sh` and update the following:

```bash
SOURCE="$HOME/path/to/your/source/file.dat"
BACKUP_DIR="$HOME/path/to/your/backup/location"
```
Example:
```bash
SOURCE="$HOME/Documents/Secrets/mydatafile.dat"
BACKUP_DIR="$HOME/Backups/SecureFile/"
```
### 2. Test the Script

Make the script executable:
```bash
chmod +x secure_backup.sh
```
Then run it manually:
```bash
./secure_backup.sh
```
You should see output like:
```bash
Backup complete: /home/youruser/Backups/SecureFile/securefile_YYYY-MM-DD_HH-MM-SS.dat
```
### 3. Test Auto-Pruning Safeguard

To simulate and verify the prune logic:

Create a fake backup file older than 30 days:
```bash
touch -d "35 days ago" ~/path/to/your/backup/location/securefile_fakeold.dat
```
Run the script again:
```bash
./secure_backup.sh
```
It will only delete backups older than 30 days if 30 or more total backups exist.

### 4. Automate with Cron

To run the script automatically every day at 10:30 AM:

Open your crontab:
```bash
crontab -e
```
Add this line at the bottom:
```bash
# === Secure File Daily Backup ===
30 10 * * * /full/path/to/secure_backup.sh >> /home/youruser/backup.log 2>&1
```
Make sure to replace /full/path/to/secure_backup.sh with the actual location of the script.