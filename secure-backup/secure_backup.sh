#!/bin/bash

# === Secure File Backup Script ===
# Backs up a sensitive file with timestamped filenames
# and automatically deletes backups older than 30 days if more than 30 total backups exist.

# === CONFIGURE YOUR SOURCE AND BACKUP LOCATIONS ===
SOURCE="$HOME/path/to/your/source/file.dat"
BACKUP_DIR="$HOME/path/to/your/backup/location"
TIMESTAMP=$(date "+%Y-%m-%d_%H-%M-%S")

# === Create Backup Directory (if it doesn't exist) ===
mkdir -p "$BACKUP_DIR"

# === Perform the Backup ===
cp "$SOURCE" "$BACKUP_DIR/securefile_$TIMESTAMP.dat"
echo "Backup complete: $BACKUP_DIR/securefile_$TIMESTAMP.dat"

# === Auto-Prune Old Backups ===
# This logic ensures we don't prune too early and accidentally delete all backups.
# Step 1: Count how many backup files currently exist
total_files=$(find "$BACKUP_DIR" -type f -name "securefile_*.dat" | wc -l)

# Step 2: Only delete files if we have at least 30 total backups (fail-safe)
if [ "$total_files" -ge 30 ]; then
    echo "[$(date)] Pruning backups older than 30 days..."
    find "$BACKUP_DIR" -type f -name "securefile_*.dat" -mtime +30 -exec rm {} \;
else
    echo "[$(date)] Only $total_files backups found. Skipping pruning to protect backup history."
fi
