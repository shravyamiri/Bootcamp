import sqlite3

def update_product_price(product_id, new_price):
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
        conn.commit()

        if cursor.rowcount == 0:
            print(f"No product found with ID {product_id}.")
        else:
            print(f"Product ID {product_id} updated with new price: ${new_price:.2f}")

        conn.close()
    except sqlite3.Error as e:
        print("Error updating product:", e)

# Example usage
if __name__ == "__main__":
    update_product_price(1, 1199.99)  # Change 1 and 1199.99 as needed
