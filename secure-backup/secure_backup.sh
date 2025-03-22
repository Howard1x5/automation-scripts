#!/bin/bash

# === Secure File Backup Script ===
# Backs up a sensitive file with timestamped filenames
# and automatically deletes backups older than 30 days.

SOURCE="$HOME/path/to/your/source/file.dat"
BACKUP_DIR="$HOME/path/to/your/backup/location"
TIMESTAMP=$(date "+%Y-%m-%d_%H-%M-%S")

mkdir -p "$BACKUP_DIR"
cp "$SOURCE" "$BACKUP_DIR/securefile_$TIMESTAMP.dat"
echo "Backup complete: $BACKUP_DIR/securefile_$TIMESTAMP.dat"

# === Auto-Prune Old Backups ===
find "$BACKUP_DIR" -type f -name "securefile_*.dat" -mtime +30 -exec rm {} \;

