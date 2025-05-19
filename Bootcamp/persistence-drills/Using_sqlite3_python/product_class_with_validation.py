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
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL
                    )
                ''')
        except sqlite3.Error as e:
            print("Error creating table:", e)

    def _validate_product(self, name, price):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must be a non-empty string.")
        if not (isinstance(price, int) or isinstance(price, float)) or price <= 0:
            raise ValueError("Product price must be a positive number.")

    def add_product(self, name, price):
        try:
            self._validate_product(name, price)
            with self._connect() as conn:
                conn.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
                print(f"Product '{name}' added successfully.")
        except ValueError as ve:
            print("Validation Error:", ve)
        except sqlite3.Error as e:
            print("Database Error:", e)

    def update_product(self, product_id, new_price):
        try:
            if not (isinstance(new_price, int) or isinstance(new_price, float)) or new_price <= 0:
                raise ValueError("New price must be a positive number.")
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
                conn.commit()
                if cursor.rowcount == 0:
                    print(f"No product found with ID {product_id}.")
                else:
                    print(f"Product ID {product_id} updated.")
        except ValueError as ve:
            print("Validation Error:", ve)
        except sqlite3.Error as e:
            print("Database Error:", e)

    def list_products(self):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products")
                products = cursor.fetchall()
                for product in products:
                    print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")
        except sqlite3.Error as e:
            print("Error reading products:", e)

# Example usage
if __name__ == "__main__":
    p = Product()
    p.add_product("Laptop", 65000)
    p.add_product("", 1000)        # Should raise validation error
    p.add_product("Phone", -5000)  # Should raise validation error

    p.list_products()

    p.update_product(1, 70000)     # Valid
    p.update_product(1, -200)      # Should raise validation error
