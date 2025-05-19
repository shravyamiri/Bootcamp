import sqlite3

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name
        self._setup_tables()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _setup_tables(self):
        try:
            with self._connect() as conn:
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS categories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )
                ''')
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL,
                        category_id INTEGER,
                        FOREIGN KEY (category_id) REFERENCES categories(id)
                    )
                ''')
        except sqlite3.Error as e:
            print("Error setting up tables:", e)

    def add_category(self, name):
        try:
            with self._connect() as conn:
                conn.execute("INSERT INTO categories (name) VALUES (?)", (name,))
                print(f"Category '{name}' added.")
        except sqlite3.Error as e:
            print("Error adding category:", e)

    def add_product(self, name, price, category_id):
        try:
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Name must be a non-empty string.")
            if price <= 0:
                raise ValueError("Price must be positive.")
            with self._connect() as conn:
                conn.execute(
                    "INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)",
                    (name, price, category_id)
                )
                print(f"Product '{name}' added.")
        except (sqlite3.Error, ValueError) as e:
            print("Error adding product:", e)

    def list_products_with_categories(self):
        try:
            with self._connect() as conn:
                cursor = conn.execute('''
                    SELECT p.id, p.name, p.price, c.name
                    FROM products p
                    LEFT JOIN categories c ON p.category_id = c.id
                ''')
                rows = cursor.fetchall()
                for row in rows:
                    print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}, Category: {row[3]}")
        except sqlite3.Error as e:
            print("Error fetching products with categories:", e)

# Example usage
if __name__ == "__main__":
    p = Product()
    p.add_category("Electronics")
    p.add_category("Home Appliances")
    p.add_product("TV", 25000, 1)
    p.add_product("Washing Machine", 18000, 2)
    p.list_products_with_categories()
