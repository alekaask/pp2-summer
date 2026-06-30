from connect import create_table
from insert_console import insert_from_console
from insert_csv import insert_from_csv
from update import update_user
from search import search
from delete import delete_user

def menu():
    create_table()

    while True:
        print("\n1. Insert (console)")
        print("2. Insert (CSV)")
        print("3. Update")
        print("4. Search")
        print("5. Delete")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_user()
        elif choice == "4":
            search()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            break

if __name__ == "__main__":
    menu()
