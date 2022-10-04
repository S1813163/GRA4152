
"""
Change the CheckingAccount class in How To 10.1 so that a $1 fee is levied for deposits
or withdrawals in excess of three free monthly transactions. Place the code for
computing the fee into a separate method that you call from the deposit and withdraw
methods.

"""

##
#  This module defines the BankAccount with zero balance
#

class BankAccount:
    ## Constructs a bank account with zero balance
    #
    def __init__(self):
        self._balance = 0.0
        
    ## Makes a deposit into this account
    #  @param amount the amount of the deposit
    #
    def deposit(self,amount):
        self._balance = self._balance + amount
        
    ## Makes a withdrawal from this account, or charges a penalty if
    #  sufficient funds are not available.
    #  @param amount the amount of the withdrawal
    #
    def withdraw(self, amount):
        self._balance = self._balance - amount
        
    ## Carries out the end of month processing that is appropriate for this account.
    #
    def monthEnd(self):
        raise NotImplementedError
    
    ## Gets the current balance of this bank account
    #  @return the current balance
    # 
    def getBalance(self):
        return self._balance
    
##
#  This module defines the SavingsAccount which earns interest on the minimum balance
#

class SavingsAccount(BankAccount):
    ## Constructs a savings account with zero balance.
    #
    def __init__(self, interestRate = 0.0):
        super().__init__()
        self._minBalance = 0
        self._interestRate = interestRate
    
    ## Sets the interest rate for this account
    #  @param rate the monthly interest rate in percent
    def setInterestRate(self, rate):
        self._interestRate = rate
    
    ## These methods overrides the superclass methods
    #
    def withdraw(self, amount):
        super().withdraw(amount)
        balance = self.getBalance()
        if balance < self._minBalance:
            self._minBalance = balance
    
    def monthEnd(self):
        interest = self._minBalance * self._interestRate / 100
        self.deposit(interest)
        self._minBalance = self.getBalance()

##
#  This module defines the CheckingAccount which has a limited number of free deposits and withdrawals
#

class CheckingAccount(BankAccount):
    ## Constructs a checking account with zero balance.
    #
    def __init__(self):
        super().__init__()
        self._transactions = 0
    
    ## This method computes the total transactions and the fee if transactions > free transactions
    #
    def fee(self):
        FREE_TRANSACTIONS = 3
        TRANSACTION_FEE   = 1
        self._transactions = self._transactions + 1
        
        if self._transactions > FREE_TRANSACTIONS:
            return TRANSACTION_FEE
        else:
            return 0
    
    ## These methods overrides the superclass methods
    #  @param amount the amount of the withdrawal
    #
    def withdraw(self, amount):        
        # fee method is called on withdraw method
        super().withdraw(amount + self.fee())
    
    # @param amount the amount of the deposit
    #    
    def deposit(self, amount):    
        # fee method is called on deposit method
        super().deposit(amount - self.fee())
    
    # Method which resets transaction counter
    #    
    def monthEnd(self):
        self._transactions = 0


# Tester programme
q = CheckingAccount()
q.deposit(100)
q.deposit(100)
q.deposit(100)
q.getBalance()   # Expected balance = 300
q.deposit(100)
q.getBalance()   # Expected balance = 399
q.withdraw(100)  
q.getBalance()   # Expected balance = 298
q.monthEnd()     # Resets transaction counter
q.deposit(100)   
q.getBalance()   # Expected balance = 398
q.deposit(100)
q.deposit(100)
q.deposit(100)
q.getBalance()   # Expected balance = 697
