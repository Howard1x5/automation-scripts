#!/bin/bash

# === Crontab Backup Script ===
# Backs up the current user's crontab into a timestamped file.
# Intended for Linux/macOS systems using crontab.
# Edit BACKUP_DIR as needed.

BACKUP_DIR="$HOME/Backups/System/crontab_backups"
TIMESTAMP=$(date "+%Y-%m-%d_%H-%M-%S")
FILENAME="crontab_backup_$TIMESTAMP.txt"

mkdir -p "$BACKUP_DIR"
crontab -l > "$BACKUP_DIR/$FILENAME"

echo "Crontab backed up to $BACKUP_DIR/$FILENAME"