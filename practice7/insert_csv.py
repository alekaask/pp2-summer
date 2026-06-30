import csv
from connect import get_connection

def insert_from_csv():
    with get_connection() as conn:
        with conn.cursor() as cur:
            with open("contacts.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    cur.execute(
                        "INSERT INTO phonebook(name, phone) VALUES (%s, %s)",
                        (row[0], row[1])
                    )

    print("CSV inserted!")
