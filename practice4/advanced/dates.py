# This file contains interactive date and time exercises.

from datetime import datetime, timedelta


# This function subtracts five days from the current date.
def subtract_five_days():
    current_date = datetime.now().date()
    print(current_date - timedelta(days=5))
    # Example output: 2026-06-21


# This function prints yesterday, today, and tomorrow.
def print_dates():
    today = datetime.now().date()
    print("Yesterday:", today - timedelta(days=1))
    print("Today:", today)
    print("Tomorrow:", today + timedelta(days=1))
    # Example output depends on the current date.


# This function removes microseconds from the current datetime.
def drop_microseconds():
    now = datetime.now()
    print(now.replace(microsecond=0))
    # Example output: 2026-06-26 20:30:15


# This function calculates the difference between two dates in seconds.
def date_difference_seconds():
    date1 = datetime(2024, 1, 1, 12, 0, 0)
    date2 = datetime(2024, 1, 2, 12, 0, 0)
    print((date2 - date1).total_seconds())
    # Example output: 86400.0


# This function runs the interactive menu for the date exercises.
def main():
    while True:
        print("\nDate Menu")
        print("1. Subtract five days from today")
        print("2. Show yesterday, today, and tomorrow")
        print("3. Remove microseconds")
        print("4. Difference between two dates in seconds")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            subtract_five_days()
        elif choice == "2":
            print_dates()
        elif choice == "3":
            drop_microseconds()
        elif choice == "4":
            date_difference_seconds()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
