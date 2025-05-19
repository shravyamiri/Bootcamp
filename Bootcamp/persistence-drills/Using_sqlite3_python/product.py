import sqlite3
import os

class Product:
    def __init__(self, db_name="store.db"):
        self.db_name = db_name
        self._create_tables()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_tables(self):
        try:
            with self._connect() as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS categories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE
                    )
                """)
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL CHECK(price > 0),
                        category_id INTEGER,
                        FOREIGN KEY (category_id) REFERENCES categories(id)
                    )
                """)
        except sqlite3.Error as e:
            print("Error creating tables:", e)

    def add_product(self, name, price, category_id=None):
        if not isinstance(name, str) or not isinstance(price, (int, float)) or price <= 0:
            print("Invalid product data.")
            return
        try:
            with self._connect() as conn:
                conn.execute("BEGIN")
                conn.execute(
                    "INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)",
                    (name, price, category_id)
                )
                conn.commit()
                print(f"Product '{name}' added.")
        except sqlite3.Error as e:
            conn.rollback()
            print("Error adding product:", e)

    def update_product_price(self, product_id, new_price):
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            print("Invalid price.")
            return
        try:
            with self._connect() as conn:
                conn.execute("BEGIN")
                conn.execute(
                    "UPDATE products SET price = ? WHERE id = ?",
                    (new_price, product_id)
                )
                conn.commit()
                print(f"Product ID {product_id} price updated to ₹{new_price}")
        except sqlite3.Error as e:
            conn.rollback()
            print("Error updating price:", e)

    def delete_product(self, product_id):
        try:
            with self._connect() as conn:
                conn.execute("BEGIN")
                conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
                conn.commit()
                print(f"Product ID {product_id} deleted.")
        except sqlite3.Error as e:
            conn.rollback()
            print("Error deleting product:", e)

    def list_products(self):
        try:
            with self._connect() as conn:
                cursor = conn.execute("SELECT * FROM products")
                products = cursor.fetchall()
                for prod in products:
                    print(prod)
        except sqlite3.Error as e:
            print("Error fetching products:", e)

    def search_by_name(self, name_fragment):
        try:
            with self._connect() as conn:
                cursor = conn.execute(
                    "SELECT * FROM products WHERE name LIKE ?",
                    (f"%{name_fragment}%",)
                )
                results = cursor.fetchall()
                if results:
                    print("Matching Products:")
                    for row in results:
                        print(row)
                else:
                    print("No matching products found.")
        except sqlite3.Error as e:
            print("Error searching products:", e)

    def get_products_with_categories(self):
        try:
            with self._connect() as conn:
                cursor = conn.execute("""
                    SELECT products.id, products.name, products.price, categories.name
                    FROM products
                    LEFT JOIN categories ON products.category_id = categories.id
                """)
                results = cursor.fetchall()
                for row in results:
                    print(f"Product ID: {row[0]}, Name: {row[1]}, Price: ₹{row[2]}, Category: {row[3]}")
        except sqlite3.Error as e:
            print("Error joining tables:", e)

    def total_inventory_value(self):
        """Calculate and return the total value of all products in stock."""
        try:
            with self._connect() as conn:
                cursor = conn.execute("SELECT SUM(price) FROM products")
                total = cursor.fetchone()[0]
                total = total if total is not None else 0.0
                print(f"Total inventory value: ₹{total:.2f}")
                return total
        except sqlite3.Error as e:
            print("Error calculating total inventory value:", e)
            return 0.0
