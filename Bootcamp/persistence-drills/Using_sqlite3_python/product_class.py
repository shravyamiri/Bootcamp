import sqlite3

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name
        self._create_products_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_products_table(self):
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

    def add_product(self, name, price):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            conn.commit()
            print(f"Product '{name}' added.")

    def update_product(self, product_id, new_price):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"No product found with ID {product_id}.")
            else:
                print(f"Product ID {product_id} updated to price {new_price}.")

    def delete_product(self, product_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"No product found with ID {product_id}.")
            else:
                print(f"Product ID {product_id} deleted.")

    def list_products(self):
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

# Example usage
if __name__ == "__main__":
    p = Product()
    p.add_product("Keyboard", 1499.99)
    p.add_product("Mouse", 499.99)
    p.list_products()
    p.update_product(1, 1299.99)
    p.delete_product(2)
    p.list_products()
