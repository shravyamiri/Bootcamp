import sqlite3

def create_customers_table():
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        conn.commit()

def insert_customers_transaction(customers):
    try:
        with sqlite3.connect("store.db") as conn:
            cursor = conn.cursor()
            conn.execute("BEGIN")  # Start transaction

            for name, email in customers:
                cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))

            conn.commit()
            print("Transaction committed. All customers added successfully.")

    except sqlite3.IntegrityError as e:
        print("Integrity error:", e)
        conn.rollback()
        print("Transaction rolled back due to an error.")
    except sqlite3.Error as e:
        print("Database error:", e)
        conn.rollback()
        print("Transaction rolled back due to an error.")

# Main Execution
if __name__ == "__main__":
    create_customers_table()

    customers_to_add = [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com"),
        ("Duplicate", "alice@example.com")  # This will trigger a UNIQUE constraint violation
    ]

    insert_customers_transaction(customers_to_add)
