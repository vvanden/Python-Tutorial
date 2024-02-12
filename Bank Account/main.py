#Objectives
#Create account
#Depositing money.
#Withdrawing money.
#Checking the balance.
#Getting the account type.
#Getting the account number.
#Getting the holder name.
#Keeping a transaction history.

class BankAccount(object):
    def __init__(self, name, accountNumber, accountType, balance = 0):
        self.name = name
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.balance = balance
        self.filename=str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"

    def deposit():
        pass

    def withdrawl():
        pass

    def record_transaction(self, type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = f"{timestamp} - {type}: ${amount}\n"
        with open(self.filename, "a") as file:
            file.write(transaction)

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
            return str(accountType)  # Ensure name is a string
        except ValueError:
            print("Invalid input. Please enter a valid name.")

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

#look through requests while req_active = True
while req_active:
    input("Press Enter to continue...")
    clearterm()
    print("*****************************************************")
    print("**                WELCOME TO MY BANK               **")
    print("*****************************************************")
    print("1: Create account")
    print("2: Deposit")
    print("3: Withdrawl")
    print("4: View Balance")
    print("5: View User ID")
    print("6: View User Name")
    print("7: View Account Type")
    print("8: View Transaction History")
    print("9: Exit")
    req = input("Selection: ").lower()
    if req == "1":
        clearterm()
        print("**CREATE ACCOUNT**")
        name = get_name()
        accountType = get_account_type()
        accountNumber = generate_id()
    if req == "2":
        print("**DEPOSIT**")
        pass
    if req == "3":
        print("**WITHDRAWL**")
        pass
    if req == "4":
        print("**VIEW BALANCE**")
        pass
    if req == "5":
        print("**VIEW USER ID**")
        pass
    if req == "6":
        print("**VIEW USER NAME**")
        pass
    if req == "7":
        print("**VIEW ACCOUNT TYPE**")
        pass
    if req == "8":
        print("**VIEW TRANSACTION HISTORY**")
        pass
    elif req == "9":
        print("**EXIT**")
        req_active = False
    else:
        continue