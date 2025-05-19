import sqlite3

def create_database():
    try:
        # Connect to SQLite database (creates store.db if it doesn't exist)
        conn = sqlite3.connect('store.db')
        print("Database 'store.db' created and connected successfully.")
        conn.close()
    except sqlite3.Error as e:
        print("Error creating database:", e)

if __name__ == "__main__":
    create_database()
