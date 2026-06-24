from datetime import datetime
import os

LOG_FILE = "input_log.txt"

total_entries = 0


def log_input(username):
    global total_entries

    print("\nType 'exit' to stop logging.\n")

    while True:
        text = input("Enter Text: ")

        if text.lower() == "exit":
            break

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a") as file:
            file.write(f"[{timestamp}] [{username}] {text}\n")

        total_entries += 1
        print("✓ Saved")


def view_logs():
    print("\n===== LOG HISTORY =====\n")

    if not os.path.exists(LOG_FILE):
        print("No logs found.")
        return

    with open(LOG_FILE, "r") as file:
        print(file.read())


def search_logs():
    keyword = input("Enter keyword to search: ")

    if not os.path.exists(LOG_FILE):
        print("No logs found.")
        return

    found = False

    with open(LOG_FILE, "r") as file:
        for line in file:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

    if not found:
        print("No matching records found.")


def clear_logs():
    confirm = input("Delete all logs? (yes/no): ")

    if confirm.lower() == "yes":
        open(LOG_FILE, "w").close()
        print("All logs cleared.")
    else:
        print("Operation cancelled.")


def show_statistics():
    if not os.path.exists(LOG_FILE):
        print("No data available.")
        return

    with open(LOG_FILE, "r") as file:
        lines = file.readlines()

    print("\n===== STATISTICS =====")
    print("Total Records :", len(lines))
    print("File Size     :", os.path.getsize(LOG_FILE), "bytes")


def main():

    username = input("Enter Username: ")

    while True:

        print("\n===== ADVANCED SAFE INPUT LOGGER =====")
        print("1. Start Logging")
        print("2. View Logs")
        print("3. Search Logs")
        print("4. Statistics")
        print("5. Clear Logs")
        print("6. Exit")

        choice = input("Choose Option: ")

        if choice == "1":
            log_input(username)

        elif choice == "2":
            view_logs()

        elif choice == "3":
            search_logs()

        elif choice == "4":
            show_statistics()

        elif choice == "5":
            clear_logs()

        elif choice == "6":
            print("\nProgram Closed.")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()