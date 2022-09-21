
"""
Class that simulates a bank account. Customers can deposit and withdraw funds. If sufficient funds are not available for
withdrawal, a $10 overdraft penalty is charged. At the end of the month, interest is added to the account. The interest rate 
can vary every month
"""

##
#  This module defines the bankAccount class.
#

class BankAccount:
    
    ## Constructs a bank account with a given balance.
    # @param initialBalance the initial account balance (default = 0.0)
    #
    def __init__(self, initialBalance = 0.0):
        self._balance = initialBalance
    
    ## This method returns the balance
    #
    def getBalance(self):
        return self._balance
    
    ## This method allows the customer to deposit 
    #
    def deposit(self, amount):
        self._balance = self._balance + amount
    
    ## This method allows the customer to withdraw, but charges a penalty if the amount is larger than the balance
    #
    def withdraw(self, amount):
        PENALTY = 10.0
        if amount > self._balance:
            self._balance = self._balance - PENALTY
        else:
            self._balance = self._balance - amount
    
    ## This method adds interest to the balance
    #
    def addInterest(self, rate):
        amount = self._balance * rate / 100.0
        self._balance = self._balance + amount

