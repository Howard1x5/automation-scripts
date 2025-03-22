# Secure Local Backup

This script creates a secure local backup of a password manager database file.  
It ensures the file is:
- Backed up with a timestamped filename
- Stored in an encrypted or access-controlled local directory
- Optionally pruned to remove backups older than a certain number of days

## Usage

```bash
bash secure_backup.sh
