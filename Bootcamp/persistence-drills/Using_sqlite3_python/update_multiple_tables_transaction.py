import sqlite3

def setup_tables():
    with sqlite3.connect("store.db") as conn:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS order_details (
                detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER NOT NULL,
                product_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders(order_id)
            )
        ''')

        # Insert test data if tables are empty
        cursor.execute("SELECT COUNT(*) FROM orders")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO orders (customer_name, status) VALUES ('John Doe', 'Pending')")
            conn.commit()
            order_id = cursor.lastrowid
            cursor.execute("INSERT INTO order_details (order_id, product_name, quantity) VALUES (?, 'Widget', 5)", (order_id,))
            conn.commit()

def update_order_and_details(order_id, new_status, detail_id, new_quantity):
    try:
        with sqlite3.connect("store.db") as conn:
            cursor = conn.cursor()
            conn.execute("BEGIN")

            # Update orders table
            cursor.execute("UPDATE orders SET status = ? WHERE order_id = ?", (new_status, order_id))

            # Update order_details table
            cursor.execute("UPDATE order_details SET quantity = ? WHERE detail_id = ?", (new_quantity, detail_id))

            # Uncomment to simulate an error and test rollback
            # raise Exception("Simulated failure")

            conn.commit()
            print("Transaction committed. Order and details updated successfully.")

    except Exception as e:
        conn.rollback()
        print("Transaction rolled back due to error:", e)

# Main Execution
if __name__ == "__main__":
    setup_tables()

    # Update existing records (adjust IDs as needed)
    update_order_and_details(order_id=1, new_status="Shipped", detail_id=1, new_quantity=10)
