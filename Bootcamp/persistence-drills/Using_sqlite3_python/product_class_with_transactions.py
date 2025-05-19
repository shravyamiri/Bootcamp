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
                conn.execute("BEGIN")
                conn.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
                conn.commit()
                print(f"Product '{name}' added successfully.")
        except (sqlite3.Error, ValueError) as e:
            print("Error adding product:", e)
            conn.rollback()

    def update_product(self, product_id, new_price):
        try:
            if not (isinstance(new_price, int) or isinstance(new_price, float)) or new_price <= 0:
                raise ValueError("New price must be a positive number.")
            with self._connect() as conn:
                conn.execute("BEGIN")
                cursor = conn.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
                if cursor.rowcount == 0:
                    print(f"No product found with ID {product_id}.")
                else:
                    print(f"Product ID {product_id} updated.")
                conn.commit()
        except (sqlite3.Error, ValueError) as e:
            print("Error updating product:", e)
            conn.rollback()

    def delete_product(self, product_id):
        try:
            with self._connect() as conn:
                conn.execute("BEGIN")
                cursor = conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
                if cursor.rowcount == 0:
                    print(f"No product found with ID {product_id}.")
                else:
                    print(f"Product ID {product_id} deleted.")
                conn.commit()
        except sqlite3.Error as e:
            print("Error deleting product:", e)
            conn.rollback()

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
    p.add_product("TV", 25000)
    p.add_product("AC", 35000)
    p.update_product(1, 28000)
    p.delete_product(3)
    p.list_products()
