"""
Design a Customer class to handle a customer loyalty marketing campaign. After
accumulating $100 in purchases, the customer receives a $10 discount on the next
purchase. 

Provide methods:
 • def makePurchase(self, amount)
 • def discountReached(self)

Provide a test program and test a scenario in which a customer has earned a discount
and then made over $90, but less than $100 in purchases. This should not result in a
second discount. Then add another purchase that results in the second discount.
"""

##
#  This module defines the Customer class.
#

class Customer:
    
    ## A constructor which initializes with the customers first purchase, or default set to zero if customer only signs up to loyalty program without a purchase
    def __init__(self, initialPurchase = 0):
        self._totalAmount = initialPurchase
        
    ## Method in which a customer purchases a good and a discount of $10 is applied if the customer has previously accumulated $100 in purchases
    def makePurchase(self, amount):
        if self.discountReached() == True:
            print(f"Discount of $10 applied on purchase, total purchasing cost was now: ${amount - 10} whereas cost without discount would have been ${amount}")
            self._totalAmount = amount - 10
        else:
            self._totalAmount = self._totalAmount + amount

    ## Method in which a discount is set to "True" (Boolean) if the accumulated purchases exceed $100
    def discountReached(self):
        if self._totalAmount >= 100:
            return True
        else:
            return False

    ## Method in which we can see how much we have accumulated in spending
    def totalAmount(self) :
        return print(f"Discount will apply when purchases exceed $100, you have now spent: ${self._totalAmount}")
         



# Test program in which a customer has earned a discount and then made over $90, but less than $100 in purchases.
x = Customer(50)    # Customers first purchase when he applies for the loyalty program is $50
x.totalAmount()     # totalAmount method shows us that the customer has spent $50
x.makePurchase(45)  # Customer makes another purchase which brings up the total amount spent to $95
x.totalAmount()     # Verifying that the customer has spent $95
x.makePurchase(10)  # Customer has now spent $105 and a discount will be applied for the next purchase
x.totalAmount()     # Verifying that the customer has spent $105
x.makePurchase(15)  # Discount applied properly, and total purchasing cost
x.totalAmount()     # Verifying that the "discount-counter" has been reset and includes the amount spent (less than the discount applied)
x.makePurchase(105) # New purchase to see that the discount will function properly
x.totalAmount()     # Customer has now spent $110 and new discount will be applied on next purchase
x.makePurchase(10)  # This purchase equals the discount value and we verify that the cost should be equal to 0.
