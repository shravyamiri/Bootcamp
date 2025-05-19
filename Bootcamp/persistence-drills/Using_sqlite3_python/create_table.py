import sqlite3

def create_products_table():
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        # SQL command to create the products table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL CHECK (price > 0)
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'products' created successfully.")
        conn.close()
    except sqlite3.Error as e:
        print("Error creating table:", e)

if __name__ == "__main__":
    create_products_table()
