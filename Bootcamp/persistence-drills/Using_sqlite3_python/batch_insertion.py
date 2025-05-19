import sqlite3
import csv

class Product:
    def __init__(self, db_name="store.db"):
        self.db_name = db_name
        self.create_tables()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                # Create categories table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS categories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )
                ''')
                # Create products table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL,
                        category_id INTEGER,
                        FOREIGN KEY (category_id) REFERENCES categories(id)
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            print("Error creating tables:", e)

    def add_product(self, name, price, category_id=None):
        if not isinstance(name, str) or not isinstance(price, (int, float)) or price <= 0:
            print("Invalid data: name must be string and price must be positive number.")
            return
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)",
                               (name, price, category_id))
                conn.commit()
                print("Product added successfully.")
        except sqlite3.Error as e:
            print("Database error:", e)

    def update_product(self, product_id, new_price):
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            print("Invalid price. Must be a positive number.")
            return
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
                if cursor.rowcount == 0:
                    print("No product found with given ID.")
                else:
                    conn.commit()
                    print("Product updated successfully.")
        except sqlite3.Error as e:
            print("Database error:", e)

    def delete_product(self, product_id):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
                if cursor.rowcount == 0:
                    print("No product found with given ID.")
                else:
                    conn.commit()
                    print("Product deleted successfully.")
        except sqlite3.Error as e:
            print("Database error:", e)

    def list_products(self):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        except sqlite3.Error as e:
            print("Database error:", e)

    def search_products(self, name_fragment):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products WHERE name LIKE ?", (f'%{name_fragment}%',))
                results = cursor.fetchall()
                for result in results:
                    print(result)
        except sqlite3.Error as e:
            print("Search error:", e)

    def get_products_with_categories(self):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT p.id, p.name, p.price, c.name as category
                    FROM products p
                    LEFT JOIN categories c ON p.category_id = c.id
                ''')
                results = cursor.fetchall()
                for row in results:
                    print(row)
        except sqlite3.Error as e:
            print("Join query error:", e)

    def get_total_product_value(self):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT SUM(price) FROM products")
                total = cursor.fetchone()[0]
                print("Total value of all products:", total if total else 0)
                return total if total else 0
        except sqlite3.Error as e:
            print("Aggregation error:", e)

    def export_to_csv(self, filename="products_export.csv"):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products")
                rows = cursor.fetchall()
                with open(filename, mode="w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Name", "Price", "Category_ID"])
                    writer.writerows(rows)
                print(f"Data exported to {filename}")
        except (sqlite3.Error, IOError) as e:
            print("Export error:", e)

    def add_products_batch(self, products):
        """
        Add multiple products in one transaction.
        :param products: List of tuples (name, price, category_id)
        """
        valid_products = []
        for product in products:
            if (len(product) == 3 and isinstance(product[0], str)
                and isinstance(product[1], (int, float)) and product[1] > 0):
                valid_products.append(product)
            else:
                print(f"Invalid product skipped: {product}")

        if not valid_products:
            print("No valid products to insert.")
            return

        try:
            with self._connect() as conn:
                conn.execute("BEGIN")
                conn.executemany(
                    "INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)",
                    valid_products
                )
                conn.commit()
                print(f"{len(valid_products)} products inserted successfully.")
        except sqlite3.Error as e:
            conn.rollback()
            print("Database error during batch insert:", e)
