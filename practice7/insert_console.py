from connect import get_connection

def insert_from_console():
    name = input("Name: ")
    phone = input("Phone: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO phonebook(name, phone) VALUES (%s, %s)",
                (name, phone)
            )

    print("Inserted!")
