import sqlite3
import random
from datetime import datetime

class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}.\nCurrent balance: ${self.balance}")
        self.update_transactions(amount, "Deposit")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.\nWithdrawal not allowed.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}.\nCurrent balance: ${self.balance}")
            self.update_transactions(amount, "Withdrawal")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")

    def update_transactions(self, amount, transaction_type):
        timestamp = datetime.now().strftime("%H:%M:%S")
        date = datetime.now().strftime("%Y-%m-%d")

        conn = sqlite3.connect('bank_database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO TRANSACTIONS VALUES (?, ?, ?, ?, ?, ?)",
                       (timestamp, date, self.account_holder, self.account_number, amount, self.balance))

        conn.commit()
        conn.close()


def create_account():
    username = input("Enter username: ")

    # Generate a random 8-digit account number
    account_number = random.randint(10000000, 99999999)

    # Check if the account number is unique
    while account_exists(account_number):
        account_number = random.randint(10000000, 99999999)

    initial_balance = float(input("Enter initial balance: "))

    # Insert account details into the database
    conn = sqlite3.connect('bank_database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ACCOUNTS VALUES (?, ?, ?)", (username, account_number, initial_balance))
    conn.commit()
    conn.close()

    print(f"Account created successfully!\nAccount Number: {account_number}")


def account_exists(account_number):
    conn = sqlite3.connect('bank_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ACCOUNTS WHERE ACCOUNT_NUMBER=?", (account_number,))
    result = cursor.fetchone()
    conn.close()
    return result is not None


def banking_operations():
    account_number = input("Enter account number: ")

    if account_exists(account_number):
        conn = sqlite3.connect('bank_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ACCOUNTS WHERE ACCOUNT_NUMBER=?", (account_number,))
        account_data = cursor.fetchone()
        conn.close()

        account = BankAccount(account_data[0], account_data[1], account_data[2])

        menu_options = {
            "1": lambda: account.deposit(float(input("Enter deposit amount: "))),
            "2": lambda: account.withdraw(float(input("Enter withdrawal amount: "))),
            "3": account.display_balance,
        }

        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "4":
                print("Exiting banking operations. Goodbye!")
                break
            elif choice in menu_options:
                menu_options[choice]()
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")
    else:
        print("Account not found.")

def main():
    while True:
        print("1. Create Account\n2. Banking Operations")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            banking_operations()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
