# Safe Input Logger

## Overview

Safe Input Logger is a Python-based command-line application designed to securely record and manage user input logs. The application stores user-entered data along with timestamps, allowing users to maintain organized records, search through logs, view statistics, and manage log files efficiently.

This project demonstrates the use of Python file handling, modular programming, user interaction, and basic log management techniques.

---

## Features

* User-specific input logging
* Automatic timestamp generation
* View complete log history
* Search logs using keywords
* Display log statistics
* Clear log records when required
* Simple and interactive command-line interface

---

## Technologies Used

* Python 3
* File Handling
* Date and Time Module (`datetime`)
* Operating System Module (`os`)

---

## Project Structure

```text
safe-input-logger/
│
├── main.py
├── input_log.txt
└── README.md
```

---

## How It Works

1. The user enters a username.
2. The application records user inputs with the current timestamp.
3. Each entry is stored in a log file.
4. Users can:

   * View all logs
   * Search specific entries
   * Check statistics
   * Clear logs
5. The program continues running until the user chooses to exit.

---

## Menu Options

### 1. Start Logging

Records user input and stores it with a timestamp.

### 2. View Logs

Displays all saved log records.

### 3. Search Logs

Searches log entries using a keyword.

### 4. Statistics

Displays:

* Total number of records
* Log file size

### 5. Clear Logs

Deletes all stored log records after confirmation.

### 6. Exit

Closes the application safely.

---

## Sample Log Entry

```text
[2026-06-24 18:45:12] [Najeeb] Learning Python file handling
```

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Python programming
* File operations
* Data logging concepts
* Timestamp management
* Command-line application development
* Modular code organization

---

## Future Improvements

* Export logs to CSV format
* User authentication system
* Log encryption for enhanced security
* Advanced filtering and reporting
* Graphical User Interface (GUI)

---

## Author

Najeeb Lone

B.Tech Computer Science Engineering Student

Passionate about Cybersecurity, Python Development, and Continuous Learning.
