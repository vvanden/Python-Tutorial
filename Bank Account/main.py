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
    def __init__(self, name, accountType, accountNumber, balance = 0):
        self.filename=str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
        print(self.filename)

    def deposit():
        pass

    def withdrawl():
        pass

import os

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
        print("**CREATE ACCOUNT**")
        BankAccount("Janice", "Chequing", "99")
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