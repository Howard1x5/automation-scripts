#!/bin/bash

# === Local Backup Script for Sensitive File ===
# Automatically backs up a sensitive file with timestamped versions.
# Safe to share publicly - no identifying paths or tool names.

SOURCE="$HOME/Documents/Secure/securefile.dat"  # Rename your actual file
BACKUP_DIR="$HOME/Backups/SecureBackups"
TIMESTAMP=$(date "+%Y-%m-%d_%H-%M-%S")

mkdir -p "$BACKUP_DIR"
cp "$SOURCE" "$BACKUP_DIR/securefile_$TIMESTAMP.dat"

echo "Backup complete: $BACKUP_DIR/securefile_$TIMESTAMP.dat"
