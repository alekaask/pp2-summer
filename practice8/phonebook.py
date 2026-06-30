import csv
from connect import get_connection


def search_pattern(pattern):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
            rows = cur.fetchall()
            if not rows:
                print("No results found")
            else:
                for row in rows:
                    print(row)


def upsert_user(name, phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    print("Inserted or updated successfully")


def bulk_insert_csv(filename):
    names, phones = [], []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) != 2:
                print(f"Skipping invalid row: {row}")
                continue
            names.append(row[0])
            phones.append(row[1])

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL bulk_insert_users(%s, %s)", (names, phones))
            for notice in conn.notices:
                print(notice.strip())
    print("Bulk insert completed")


def get_paginated(page, limit):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_paginated(%s, %s)", (page, limit))
            rows = cur.fetchall()
            if not rows:
                print("No data on this page")
            else:
                for row in rows:
                    print(row)


def delete_user(value):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_user_proc(%s)", (value,))
    print("Deleted (if existed)")


def menu():
    while True:
        print("\n===== PHONEBOOK MENU =====")
        print("1. Search")
        print("2. Insert/Update (Upsert)")
        print("3. Bulk Insert (CSV)")
        print("4. Pagination")
        print("5. Delete")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            search_pattern(input("Enter search pattern: "))
        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            upsert_user(name, phone)
        elif choice == "3":
            bulk_insert_csv("contacts.csv")
        elif choice == "4":
            page = int(input("Page number: "))
            limit = int(input("Rows per page: "))
            get_paginated(page, limit)
        elif choice == "5":
            delete_user(input("Enter name or phone: "))
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
