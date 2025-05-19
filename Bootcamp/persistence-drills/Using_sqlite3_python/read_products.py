import sqlite3

def fetch_all_products():
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        if rows:
            print("ID | Name         | Price")
            print("----------------------------")
            for row in rows:
                print(f"{row[0]:<3} | {row[1]:<12} | ${row[2]:.2f}")
        else:
            print("No products found.")

        conn.close()
    except sqlite3.Error as e:
        print("Error reading data:", e)

# Example usage
if __name__ == "__main__":
    fetch_all_products()
