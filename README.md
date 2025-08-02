# File Integrity Checker

This Python script monitors a directory for file changes by computing and comparing SHA-256 hashes of all files. It detects new, modified, and deleted files.

## Features

- Scans all files in the specified directory (recursively)
- Computes SHA-256 hashes for each file
- Stores hashes in `file_hashes.json`
- Detects and reports new, modified, and deleted files

## Usage

1. Place `FIC.py` in the directory you want to monitor, or set the `MONITOR_DIR` variable in the script.
2. Run the script:

    ```sh
    python FIC.py
    ```

3. On first run, it creates `file_hashes.json` with the current state.
4. On subsequent runs, it reports any detected changes.

## Configuration

- **MONITOR_DIR**: Change this variable in the script to monitor a different directory.
- **HASH_FILE**: Change this variable to use a different file for storing hashes.

## Requirements

- Python 3.x

## How it works

- The script walks through all files in the monitored directory.
- It skips the hash file itself.
- It computes SHA-256 hashes and compares them to the previous run.
- It prints a summary of changes and updates the hash file.
