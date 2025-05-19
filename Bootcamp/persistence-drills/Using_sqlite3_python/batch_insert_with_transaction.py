import sqlite3

def setup_products_table():
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL CHECK(price > 0)
            )
        ''')
        conn.commit()

def batch_insert_products(products):
    """
    Inserts a list of product tuples (name, price) into the products table.
    If any insertion fails, the transaction is rolled back.
    """
    try:
        with sqlite3.connect("store.db") as conn:
            cursor = conn.cursor()
            conn.execute("BEGIN")  # Start transaction

            for product in products:
                name, price = product

                # Optional validation (not mandatory for transaction rollback, but good practice)
                if not isinstance(name, str) or not isinstance(price, (int, float)) or price <= 0:
                    raise ValueError(f"Invalid product data: {product}")

                cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))

            conn.commit()
            print("All products inserted successfully.")

    except Exception as e:
        conn.rollback()
        print("Transaction rolled back due to error:", e)

# Main Execution
if __name__ == "__main__":
    setup_products_table()

    # Example product list: (name, price)
    products_to_insert = [
        ("Laptop", 1200.99),
        ("Mouse", 25.50),
        ("Keyboard", 45.00),
        ("Monitor", 250.00),
        ("FaultyProduct", -5)  # This will trigger rollback
    ]

    batch_insert_products(products_to_insert)
