import sqlite3

def insert_product(name, price):
    try:
        if not isinstance(name, str) or not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Invalid input: name must be a string and price must be a positive number.")

        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        insert_query = "INSERT INTO products (name, price) VALUES (?, ?)"
        cursor.execute(insert_query, (name, price))

        conn.commit()
        print(f"Product '{name}' inserted successfully.")
        conn.close()
    except (sqlite3.Error, ValueError) as e:
        print("Error inserting product:", e)

# Example usage
if __name__ == "__main__":
    insert_product("Laptop", 999.99)
