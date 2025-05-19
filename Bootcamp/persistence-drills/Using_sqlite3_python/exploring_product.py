import sqlite3
import csv

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name
        self._create_tables()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_tables(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL CHECK(price > 0),
                    category_id INTEGER
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            """)

    def add_product(self, name, price, category_id=None):
        if not isinstance(name, str) or not isinstance(price, (int, float)) or price <= 0:
            print("Invalid product data")
            return
        try:
            with self._connect() as conn:
                conn.execute("BEGIN")
                conn.execute("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)", (name, price, category_id))
                conn.commit()
                print("Product added successfully.")
        except sqlite3.Error as e:
            conn.rollback()
            print("Database error during add:", e)

    def update_price(self, product_id, new_price):
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            print("Invalid price")
            return
        try:
            with self._connect() as conn:
                conn.execute("BEGIN")
                conn.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
                conn.commit()
                print("Price updated successfully.")
        except sqlite3.Error as e:
            conn.rollback()
            print("Database error during update:", e)

    def delete_product(self, product_id):
        try:
            with self._connect() as conn:
                conn.execute("BEGIN")
                conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
                conn.commit()
                print("Product deleted successfully.")
        except sqlite3.Error as e:
            conn.rollback()
            print("Database error during delete:", e)

    def list_products(self):
        try:
            with self._connect() as conn:
                cursor = conn.execute("SELECT id, name, price FROM products")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        except sqlite3.Error as e:
            print("Database error during list:", e)

    def search_products(self, name_fragment):
        try:
            with self._connect() as conn:
                cursor = conn.execute("SELECT id, name, price FROM products WHERE name LIKE ?", (f"%{name_fragment}%",))
                return cursor.fetchall()
        except sqlite3.Error as e:
            print("Database error during search:", e)
            return []

    def get_products_with_categories(self):
        try:
            with self._connect() as conn:
                cursor = conn.execute("""
                    SELECT p.id, p.name, p.price, c.name as category 
                    FROM products p 
                    LEFT JOIN categories c ON p.category_id = c.id
                """)
                return cursor.fetchall()
        except sqlite3.Error as e:
            print("Database error during join:", e)
            return []

    def get_total_inventory_value(self):
        try:
            with self._connect() as conn:
                cursor = conn.execute("SELECT SUM(price) FROM products")
                total = cursor.fetchone()[0]
                return total if total is not None else 0
        except sqlite3.Error as e:
            print("Database error during aggregation:", e)
            return 0

    def export_to_csv(self, filename="products_export.csv"):
        """Export all products to a CSV file."""
        try:
            with self._connect() as conn:
                cursor = conn.execute("SELECT id, name, price, category_id FROM products")
                rows = cursor.fetchall()

                if not rows:
                    print("No data to export.")
                    return

                with open(filename, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Name", "Price", "Category ID"])  # CSV header
                    writer.writerows(rows)

                print(f"Data exported to {filename} successfully.")
        except sqlite3.Error as e:
            print("Database error during export:", e)
        except Exception as ex:
            print("File error during export:", ex)
