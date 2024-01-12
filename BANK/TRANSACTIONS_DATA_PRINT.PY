import sqlite3

def display_transactions():
    conn = sqlite3.connect('bank_database.db')
    cursor = conn.cursor()

    # Fetch all rows from the TRANSACTIONS table
    cursor.execute("SELECT * FROM TRANSACTIONS")
    transactions = cursor.fetchall()

    if not transactions:
        print("No transactions found.")
    else:
        print("\n=== TRANSACTIONS ===")
        print(f"{'Time':<15}{'Date':<15}{'Username':<15}{'Account Number':<15}{'Transaction Amount':<20}{'Current Balance':<20}")
        print("=" * 100)
        for transaction in transactions:
            print(f"{transaction[0]:<15}{transaction[1]:<15}{transaction[2]:<15}{transaction[3]:<15}{transaction[4]:<20}{transaction[5]:<20}")

    conn.close()

# Example usage
display_transactions()
