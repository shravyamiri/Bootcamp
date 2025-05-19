import sqlite3

# Step 1: Set up the database and accounts table
def setup_accounts():
    with sqlite3.connect("bank.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                balance REAL NOT NULL CHECK(balance >= 0)
            )
        ''')

        # Add test accounts (if they don't already exist)
        cursor.execute("SELECT COUNT(*) FROM accounts")
        if cursor.fetchone()[0] == 0:
            accounts = [
                (1, 'Alice', 1000.00),
                (2, 'Bob', 500.00)
            ]
            cursor.executemany("INSERT INTO accounts (account_id, name, balance) VALUES (?, ?, ?)", accounts)
            conn.commit()

# Step 2: Function to transfer funds between accounts
def transfer_funds(from_account_id, to_account_id, amount):
    try:
        with sqlite3.connect("bank.db") as conn:
            cursor = conn.cursor()
            conn.execute("BEGIN")  # Start transaction

            # Fetch balances
            cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (from_account_id,))
            from_row = cursor.fetchone()
            if not from_row:
                raise ValueError(f"Account {from_account_id} does not exist.")
            if from_row[0] < amount:
                raise ValueError("Insufficient funds.")

            cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (to_account_id,))
            to_row = cursor.fetchone()
            if not to_row:
                raise ValueError(f"Account {to_account_id} does not exist.")

            # Perform debit and credit
            cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, from_account_id))
            cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, to_account_id))

            conn.commit()
            print(f"Transferred ${amount:.2f} from account {from_account_id} to {to_account_id}.")

    except Exception as e:
        conn.rollback()
        print("Transaction failed. Rolled back.")
        print("Error:", e)

# Step 3: Function to display account balances
def display_balances():
    with sqlite3.connect("bank.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts")
        for row in cursor.fetchall():
            print(f"Account {row[0]} ({row[1]}): Balance = ${row[2]:.2f}")

# Example Usage
if __name__ == "__main__":
    setup_accounts()

    print("Before transfer:")
    display_balances()

    print("\nAttempting transfer of $200 from Alice to Bob:")
    transfer_funds(1, 2, 200)

    print("\nAfter transfer:")
    display_balances()

    print("\nAttempting invalid transfer of $2000 from Bob to Alice (should fail):")
    transfer_funds(2, 1, 2000)

    print("\nFinal balances:")
    display_balances()
