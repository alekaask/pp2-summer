from connect import get_connection

def update_user():
    name = input("Enter name to update: ")
    new_phone = input("New phone: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE phonebook SET phone=%s WHERE name=%s",
                (new_phone, name)
            )

    print("Updated!")
