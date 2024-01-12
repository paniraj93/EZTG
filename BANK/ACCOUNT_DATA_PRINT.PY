import sqlite3

def display_accounts():
    conn = sqlite3.connect('bank_database.db')
    cursor = conn.cursor()

    # Fetch all rows from the ACCOUNTS table
    cursor.execute("SELECT * FROM ACCOUNTS")
    accounts = cursor.fetchall()

    if not accounts:
        print("No accounts found.")
    else:
        print("\n=== ACCOUNTS ===")
        print(f"{'Username':<15}{'Account Number':<15}{'Balance':<15}")
        print("=" * 45)
        for account in accounts:
            print(f"{account[0]:<15}{account[1]:<15}{account[2]:<15}")

    conn.close()

# Example usage
display_accounts()
