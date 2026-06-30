import psycopg2
from config import load_config


def get_connection():
    config = load_config()
    return psycopg2.connect(**config)


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    phone TEXT UNIQUE NOT NULL
                )
            """)
