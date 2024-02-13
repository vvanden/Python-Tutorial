#Objectives
#Create account
#Depositing money.
#Withdrawing money.
#Checking the balance.
#Getting the account type.
#Getting the account number.
#Getting the holder name.
#Keeping a transaction history.

class BankAccount:
    def __init__(self, name, accountNumber, accountType, balance = 0):
        self.name = name
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.balance = balance
        self.filename=str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"

    def record_transaction(self, type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = f"{timestamp} - {type}: ${amount}\n"
        with open(self.filename, "a") as file:
            file.write(transaction)

    def read_transactions():
        try:
            file=open(self.filename, "r") ## open a file in read mode
        except FileNotFoundError:
            print("Wrong file or file path")
        if os.stat(self.filename).st_size == 0:
            print("Transactions history is empty.")
        else:
            print(file.read())
        file.close()

def deposit(self, amount):
    amount = input("Deposit Amount: ")

def withdrawl():
    pass

def clearterm():
    os.system('CLS')

def get_name():
    while True:
        name = input("Name: ")
        if not name:
            print("Invalid input. Please enter a valid name.")
            continue
        try:
            return str(name)  # Ensure name is a string
        except ValueError:
            print("Invalid input. Please enter a valid name.")

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
            return str(accountType)  # Ensure name is a string
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

#set working directory
work_dir = 'C:/Users/vvanden/Documents/Python/Python-Tutorial/Bank Account'

#confirm working directory
try:
    os.chdir(work_dir)
except WindowsError:
    print("WindowsError, confirm folder locaiton")
    quit()

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
    print("*****************************************************")
    print("**                WELCOME TO MY BANK               **")
    print("*****************************************************")
    print("1: Create account")
    print("2: Select account")
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
        print("**SELECT ACCOUNT**")
        account_name = input ("Input account name: ")
        account = find_account_by_name(account_name)
        if account:
            print("Account Selected:")
            print(f"Account Name: {account.name}")
            print(f"Account Type: {account.accountType}")
        else:
            print(f"Account with name '{name}' not found.")
    if req == "3":
        clearterm()
        print("**DEPOSIT**")
        accounts.record_transaction("deposit", amount)
    if req == "4":
        clearterm()
        print("**WITHDRAWL**")
        pass
    if req == "5":
        clearterm()
        print("**VIEW BALANCE**")
        if account is not None:
            print(f"User ID: ${account.balance}")
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
        read_transactions()
    elif req == "10":
        clearterm()
        print("**EXIT**")
        req_active = False
    else:
        continue