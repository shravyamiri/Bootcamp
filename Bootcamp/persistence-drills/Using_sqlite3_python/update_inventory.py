import sqlite3
from datetime import datetime

# Step 1: Setup database and tables
def setup_inventory_db():
    with sqlite3.connect("inventory.db") as conn:
        cursor = conn.cursor()

        # Create products table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                inventory_count INTEGER NOT NULL CHECK(inventory_count >= 0)
            )
        """)

        # Create inventory log table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory_log (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                change_amount INTEGER,
                reason TEXT,
                timestamp TEXT,
                FOREIGN KEY(product_id) REFERENCES products(id)
            )
        """)

        # Add sample product if not already present
        cursor.execute("SELECT COUNT(*) FROM products")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO products (name, inventory_count) VALUES (?, ?)", ("Widget", 50))
            conn.commit()


# Step 2: Transactional function for inventory update with logging
def update_inventory(product_id, change_amount, reason):
    try:
        with sqlite3.connect("inventory.db") as conn:
            cursor = conn.cursor()
            conn.execute("BEGIN")  # Start transaction

            # Get current inventory
            cursor.execute("SELECT inventory_count FROM products WHERE id = ?", (product_id,))
            result = cursor.fetchone()
            if not result:
                raise ValueError("Product not found.")

            new_inventory = result[0] + change_amount
            if new_inventory < 0:
                raise ValueError("Inventory cannot go negative.")

            # Update inventory count
            cursor.execute("UPDATE products SET inventory_count = ? WHERE id = ?", (new_inventory, product_id))

            # Insert log
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO inventory_log (product_id, change_amount, reason, timestamp)
                VALUES (?, ?, ?, ?)
            """, (product_id, change_amount, reason, timestamp))

            conn.commit()
            print(f"Inventory updated. New count: {new_inventory}")

    except Exception as e:
        conn.rollback()
        print("Transaction failed. Rolled back.")
        print("Error:", e)


# Step 3: Display inventory and logs
def display_inventory():
    with sqlite3.connect("inventory.db") as conn:
        cursor = conn.cursor()
        print("\nCurrent Inventory:")
        for row in cursor.execute("SELECT * FROM products"):
            print(row)

def display_logs():
    with sqlite3.connect("inventory.db") as conn:
        cursor = conn.cursor()
        print("\nInventory Logs:")
        for row in cursor.execute("SELECT * FROM inventory_log ORDER BY timestamp DESC"):
            print(row)


# Example Usage
if __name__ == "__main__":
    setup_inventory_db()

    display_inventory()
    update_inventory(1, -10, "Order Shipped")
    display_inventory()
    display_logs()

    print("\nAttempting invalid inventory deduction (too much):")
    update_inventory(1, -100, "Error Test")
    display_inventory()
    display_logs()
