"""
Implement a class ComboLock that works like the combination lock in a gym locker, as shown here. The lock is
constructed with a combination - three numbers between 0 and 39. The reset method resets the dial so that it points to 0. 
The turnLeft and turnRight methods turn the dial by a given number of ticks to the left or right. The open method attempts to open the lock. 
The lock opens if the user first turned it tight to the first number in the combination, then left to the second, then right to the third.
"""

##
#  This module defines the Combination Lock class. Inputs are the secret combination. Then use .turnRight/.turnLeft to move the dial
#  to the left or right. Combination lock is restricted between 0-39. If you try to set a secret number < 0, then it will be forced to 0, and
#  if you try to set a secret number > 39, it will be forced to 39. When you have moved to the dial you want, then use .saveDial to save that number.
#  Now proceed with .turnRight/.turnLeft for the second number, and use the same procedure with the last number. When you have dialed in for all 3 numbers
#  you can try to open the combination lock using .open.
#

class ComboLock:
    ## A constructor which initializes the combination lock with the secrets
    #
    def __init__(self, secret1, secret2, secret3):
        self._secret1 = self.secret(secret1)
        self._secret2 = self.secret(secret2)
        self._secret3 = self.secret(secret3)
        self._number1 = 0
        self._number2 = 0
        self._number3 = 0
        self._dial = 0
    
    ## Method which restrict the secret numbers between 0-39
    #  if secret < 0 then it returns 0, if secret > 39 it returns 39
    #
    def secret(self, secret):
        if secret > 39:
            return 39
        elif secret < 0:
            return 0
        return secret

    ## Method which resets the dial of the combination lock
    #
    def reset(self):
        self._dial = 0
    
    ## Method which returns the value of the dial
    #
    def getDial(self):
        return self._dial

    ## Method which turns the dial by a given of numbers to the left restricted to lower number 0
    #
    def turnLeft(self, ticks):
        if self._dial <= 0:
            self._dial = 0
            print(f"The dial number is: {self._dial}") 
        else:
            self._dial = self._dial - ticks
            print(f"The dial number is: {self._dial}") 
        
    ## Method which turns the dial by a given of numbers to the right restricted to upper number 39
    #
    def turnRight(self, ticks):
        if self._dial >= 39:
            self._dial = 39
            print(f"The dial number is: {self._dial}") 
        else:
            self._dial = self._dial + ticks
            print(f"The dial number is: {self._dial}") 

    ## Method which saves the dial for the corresponding number.
    #
    def saveDial(self):
        if self._number1 == 0:
            self._number1 = self._dial
        elif self._number2 == 0:
            self._number2 = self._dial
        elif self._number3 == 0:
            self._number3 = self._dial
        print(f"Dial is saved as: {self._dial}")
        
    ## Method which tries to open the combo lock. It will only be opened if all 3 numbers are equal to the secret numbers.
    #
    def open(self):
        if (self._number1 == self._secret1) and (self._number2 == self._secret2) and (self._number3 == self._secret3):
            print("Combo lock unlocked!")
        else:
            print("Incorrect combination, reset dial and try again.")

# Tester program. 
x = ComboLock(4, 2, 6)
x.turnRight(1)
x.turnRight(1)
x.turnRight(1)
x.turnRight(1)
x.saveDial()
x.turnLeft(1)
x.turnLeft(1)
x.saveDial()
x.turnRight(1)
x.turnRight(1)
x.turnRight(1)
x.turnRight(1)
x.saveDial()
x.open()
