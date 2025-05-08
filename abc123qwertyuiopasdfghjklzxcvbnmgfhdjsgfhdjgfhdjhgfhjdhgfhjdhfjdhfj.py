import sqlite3
import datetime

def create_database():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_number INTEGER PRIMARY KEY,
            customer_name TEXT,
            balance REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number INTEGER,
            transaction_type TEXT,
            amount REAL,
            transaction_date TEXT,
            FOREIGN KEY (account_number) REFERENCES accounts (account_number)
        )
    """)

    conn.commit()
    conn.close()

def create_account(customer_name, account_number,initial_balance):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO accounts (account_number, customer_name, balance) VALUES (?, ?, ?)",
                   (account_number, customer_name, initial_balance))

    conn.commit()
    conn.close()

def deposit(account_number, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, account_number))
    cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount, transaction_date) VALUES (?, ?, ?, ?)", (account_number, "Deposit", amount, datetime.datetime.now()))

    conn.commit()
    conn.close()

def withdraw(account_number, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
    balance = cursor.fetchone()[0]

    if balance >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_number = ?", (amount, account_number))
        cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount, transaction_date) VALUES (?, ?, ?, ?)", (account_number, "Withdrawal", amount, datetime.datetime.now()))
        conn.commit()
        print("Withdrawal successful")
    else:
        print("Insufficient funds.")
    conn.close()

def get_account_balance(account_number):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
    balance = cursor.fetchone()
    conn.close()
    if balance:
        return balance[0]
    else:
        return None

def get_transaction_history(account_number):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT transaction_type, amount, transaction_date FROM transactions WHERE account_number = ?", (account_number,))
    transactions = cursor.fetchall()
    conn.close()
    return transactions

create_database()
create_account("John Doe", 123456, 1000.0)
deposit(123456, 500.0)
withdraw(123456, 200.0)
withdraw(123456, 3000.0)
print(get_account_balance(123456))
print(get_transaction_history(123456))
