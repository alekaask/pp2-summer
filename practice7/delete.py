from connect import get_connection

def delete_user():
    value = input("Enter name or phone to delete: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM phonebook WHERE name=%s OR phone=%s",
                (value, value)
            )

    print("Deleted!")
