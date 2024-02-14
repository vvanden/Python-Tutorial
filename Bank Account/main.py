class BankAccount(object):
    def __init__(self, name, accountNumber, accountType, balance = 0):
        self.name = name
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.balance = balance
        self.filename=str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"

def read_transactions(filename):
    try:
        with open(filename, "r") as file:  # Use with to ensure file closing
            if os.stat(filename).st_size == 0:
                print("Transactions history is empty.")
            else:
                print(file.read())
                file.close()
    except FileNotFoundError:
        print("Error, there is no transaction history for this account.")

def record_transaction(type, amount, filename):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction = f"{timestamp} - {type}: ${amount}\n"
    with open(filename, "a") as file:
        file.write(transaction)

def deposit(accountNumber, amount):
    for account in accounts:
        if account.accountNumber == accountNumber:
            cur_balance = account.balance
            account.balance = cur_balance + amount
            record_transaction("Deposit", amount, account.filename)
            print("Deposit complete.")
    return None
    
def withdrawl(accountNumber, amount):
    for account in accounts:
        if account.accountNumber == accountNumber:
            cur_balance = account.balance
            account.balance = cur_balance - amount
            record_transaction("Withdrawl", amount, account.filename)
            print("Withdrawl complete.")
    return None

def clearterm():
    os.system('CLS')

def get_name():
    while True:
        first_name = input("First Name: ")
        if not first_name:
            print("Invalid input. Please enter a valid first name.")
            continue
        try:
            pass
        except ValueError:
            print("Invalid input. Please enter a valid first name.")
        last_name = input("Last Name: ")
        if not last_name:
            print("Invalid input. Please enter a valid last name.")
            continue
        try:
            pass
        except ValueError:
            print("Invalid input. Please enter a valid last name.")
        name = first_name + ", " + last_name
        return str(name)  # Ensure name is a string

def get_account_type():
    while True:
        accountType = input("Account Type (C)hequing, (S)avings: ").lower()
        if not accountType:
            print("Invalid input. Please enter a valid account type.")
            continue
        elif accountType != "c" and accountType != "s":
            print("Invalid input. Please enter a valid account type.")
            continue
        try:
            if accountType == "c":
                accountType = "Chequing"
            else:
                accountType = "Savings"
            return str(accountType)
        except ValueError:
            print("Invalid input. Please enter a valid name.")

def leading_uppercase(string):
    if not string:
        return ""
    return string[0].upper() + string[1:]

def find_account_by_name(name):
    for account in accounts:
        if account.name == name:
            return account
    return None   

def generate_id():
    accountNumber = uuid.uuid4()
    return accountNumber

import os
import uuid
import datetime

#set initial state
req_active = True

#bank account
accounts = []

#default account
account = BankAccount("NULL", "NULL", "NULL")

#look through requests while req_active = True
while req_active:
    input("Press Enter to continue...")
    clearterm()
    if (account.accountNumber == "NULL"):
        print("*******************")
        print("WELCOME TO MY BANK")
        print("*******************")
    else:
        print("*******************")
        print("WELCOME TO MY BANK")
        print(f"Hi: {account.name}")
        print("*******************")
    print("1: Create account")
    print("2: Select account by Name")
    print("3: Deposit")
    print("4: Withdrawl")
    print("5: View Balance")
    print("6: View User ID")
    print("7: View User Name")
    print("8: View Account Type")
    print("9: View Transaction History")
    print("10: Exit")
    req = input("Selection: ").lower()
    if req == "1":
        clearterm()
        print("**CREATE ACCOUNT**")
        name = get_name()
        name_upper = leading_uppercase(name)
        accountNumber = generate_id()
        accountType = get_account_type()
        accounts.append(BankAccount(name_upper, accountNumber, accountType))
    if req == "2":
        clearterm()
        print("**SELECT ACCOUNT BY NAME**")
        account_name = get_name()
        account = find_account_by_name(account_name)
        if account:
            print("Account Selected:")
            print(f"Account Name: {account.name}")
            print(f"Account Type: {account.accountType}")
            print(f"Account Number: {account.accountNumber}")
        else:
            print(f"Account with name not found.")
    if req == "3":
        clearterm()
        print("**DEPOSIT**")
        if account.accountNumber == "NULL":
            print(f"Account not found, please select account.")
            continue
        else:
            try:
                amount = float(input("Deposit amount: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            except:
                raise Exception("Unexpected error.")
        
        if amount > 0:
            deposit(account.accountNumber, amount)
        else:
            print("Deposit amount must be at least $0.01.")
            continue
    if req == "4":
        clearterm()
        print("**WITHDRAWL**")
        if account.accountNumber == "NULL":
            print(f"Account not found, please select account.")
            continue
        else:
            try:
                amount = float(input("Withdrawl amount: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            except:
                raise Exception("Unexpected error.")
        
        if amount > 0:
            if account.balance >= amount:
                withdrawl(account.accountNumber, amount)
            else:
                print(f"Insufficient funds, your current account balance is: ${account.balance}")
                continue
        else:
            print("Withdrawal amount must be at least $0.01.")
            continue

    if req == "5":
        clearterm()
        print("**VIEW BALANCE**")
        if account is not None:
            print(f"Balance: ${account.balance}")
        else:
            print(f"Account not selected, please create or select an account.")
    if req == "6":
        clearterm()
        print("**VIEW USER ID**")        
        if account is not None:
            print(f"User ID: {account.accountNumber}")
        else:
            print(f"Account not selected, please create or select an account.")
    if req == "7":
        clearterm()
        print("**VIEW USER NAME**")
        if account is not None:
            print(f"User Name: {account.name}")
        else:
            print(f"Account not selected, please create or select an account.")
    if req == "8":
        clearterm()
        print("**VIEW ACCOUNT TYPE**")
        if account is not None:
            print(f"Account Type: {account.accountType}")
        else:
            print(f"Account not selected, please create or select an account.")
    if req == "9":
        clearterm()
        print("**VIEW TRANSACTION HISTORY**")
        read_transactions(account.filename)
    elif req == "10":
        clearterm()
        print("**EXIT**")
        req_active = False
    else:
        continue