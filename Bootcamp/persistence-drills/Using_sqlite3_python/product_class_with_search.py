import sqlite3

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name
        self._create_products_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_products_table(self):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL
                    )
                ''')
                conn.commit()
        except sqlite3.OperationalError as e:
            print("Error creating table:", e)

    def add_product(self, name, price):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
                conn.commit()
                print(f"Product '{name}' added.")
        except sqlite3.Error as e:
            print("Error adding product:", e)

    def update_product(self, product_id, new_price):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
                conn.commit()
                if cursor.rowcount == 0:
                    print(f"No product found with ID {product_id}.")
                else:
                    print(f"Product ID {product_id} updated.")
        except sqlite3.Error as e:
            print("Error updating product:", e)

    def delete_product(self, product_id):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
                conn.commit()
                if cursor.rowcount == 0:
                    print(f"No product found with ID {product_id}.")
                else:
                    print(f"Product ID {product_id} deleted.")
        except sqlite3.Error as e:
            print("Error deleting product:", e)

    def list_products(self):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products")
                rows = cursor.fetchall()
                if rows:
                    print("Products:")
                    for row in rows:
                        print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}")
                else:
                    print("No products found.")
        except sqlite3.Error as e:
            print("Error fetching products:", e)

    def search_products_by_name(self, name_fragment):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                like_pattern = f"%{name_fragment}%"
                cursor.execute("SELECT * FROM products WHERE name LIKE ?", (like_pattern,))
                results = cursor.fetchall()
                if results:
                    print(f"Products matching '{name_fragment}':")
                    for product in results:
                        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")
                else:
                    print(f"No products found matching '{name_fragment}'.")
        except sqlite3.Error as e:
            print("Error searching for products:", e)

# Example usage
if __name__ == "__main__":
    p = Product()
    p.add_product("Keyboard", 799.00)
    p.add_product("Gaming Keyboard", 1599.00)
    p.add_product("Mouse", 499.00)

    p.list_products()
    p.search_products_by_name("keyboard")
