import sqlite3

def delete_product_by_id(product_id):
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()

        if cursor.rowcount == 0:
            print(f"No product found with ID {product_id}.")
        else:
            print(f"Product with ID {product_id} has been deleted.")

        conn.close()
    except sqlite3.Error as e:
        print("Error deleting product:", e)

# Example usage
if __name__ == "__main__":
    delete_product_by_id(1)  # Change 1 to the ID of the product you want to delete
