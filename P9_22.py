# -*- coding: utf-8 -*-
"""
Implement a class Portfolio. This class has two objects, checking and savings, of the type BankAccount
that was developed in Worked Example 9.1. Implement four methods:
    * def deposit(self, amount, account)
    * def withdraw(self, amount, account)
    * def transfer(self, amount, account)
    * def getBalance(self, account)
Here the account string is "S" or "C". For the deposit or withdrawal, it indicates which account is affected.
For a transfer, it indicates the account from which the money is taken; the money is automatically transferred
to the other account.

"""

# Set working directory to where the BankAccount class from working example 9.1 is located. This can also
# be pulled from my repository under the name "W9_1.py".
from W9_1 import BankAccount

##
#  This module defines the Portfolio class.
# 

class Portfolio:
    
    ## Initializes with a checking- and savings account. If no values are input the default is zero
    #
    def __init__(self, checkingAccount = 0.0, savingsAccount = 0.0):
        self._checkingAccount = BankAccount(checkingAccount)
        self._savingsAccount= BankAccount(savingsAccount)
    
    ## Method which lets you deposit to the checking or savings account
    #
    def deposit(self, amount, account):
        if account == "C":
            self._checkingAccount.deposit(amount)
            print(f"Amount deposited to checking account: ${amount} ")
        elif account == "S":
            self._savingsAccount.deposit(amount)
            print(f"Amount deposited to savings account: ${amount} ")
    


    ## Method which lets you withdraw from the checking or savings account
    # If the customer tries to withdraw more than is available a penalty of $ will be applied
    # 
    def withdraw(self, amount, account):
        if account == "C":
            self._checkingAccount.withdraw(amount)
            if amount > self._checkingAccount.getBalance():
                print("Withdrawn amount from checking account is larger than its balance, penalty of $10 applied")
            else: 
                print(f"Successfully withdrawn ${amount} from checking account")
        elif account == "S":
            self._savingsAccount.withdraw(amount)
            if amount > self._savingsAccount.getBalance():
                print("Withdrawn amount from savings account is larger than its balance, penalty of $10 applied")
            else:
                print(f"Successfully withdrawn ${amount} from savings account")

    
    ## Method which lets you transfer an amount between the checking and savings account
    # "account" indicates the account which is affected
    #
    def transfer(self, amount, account):
        if account == "C":
            balance = self._checkingsAccount.getBalance()
            self._savingsAccount.withdraw(amount)
            if amount > balance:
                print("Transferred amount from checking account is larger than its balance, penalty of $10 applied")
            else:
                self._checkingsAccount.deposit(amount)
                print(f"Successfully transferred ${amount} from checking account to savings account")

        elif account == "S":
            balance = self._savingsAccount.getBalance()
            self._savingsAccount.withdraw(amount)
            if amount > balance:
                print("Transferred amount from savings account is larger than its balance, penalty of $10 applied")
            else:
                self._checkingAccount.deposit(amount)
                print(f"Successfully transferred ${amount} from savings account to checkings account")
        
    ## Method which lets you see the balance of the checking or savings account, defined by "C" and "S"
    #    
    def getBalance(self, account):
        if account == "C":
            balance = self._checkingAccount.getBalance()
            print(f"Balance of checking account: ${balance}")
        elif account == "S":
            balance = self._savingsAccount.getBalance()
            print(f"Balance of savings account: ${balance}")
        

### Tester Program ###
# Testing deposit and getBalance    
x = Portfolio(0,0)
x.deposit(100, "S")
x.deposit(100, "C")
x.getBalance("S")
x.getBalance("C")

# Testing withdraw method
x.withdraw(10, "S")
x.getBalance("S")
x.withdraw(100, "S")
x.getBalance("S")

# Test the transfer method
x = Portfolio(0,0)
x.deposit(100, "S")
x.deposit(100, "C")
x.getBalance("C")
x.getBalance("S")
x.transfer(60, "S")
x.getBalance("C")
x.getBalance("S")
x.transfer(60, "S")
x.getBalance("C")
x.getBalance("S")

# Everything works correctly!