from connect import get_connection

def search():
    keyword = input("Search name: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook WHERE name ILIKE %s",
                (f"%{keyword}%",)
            )

            rows = cur.fetchall()

            for row in rows:
                print(row)
